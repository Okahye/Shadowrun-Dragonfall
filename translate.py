#!/usr/bin/python3

import polib
import sys
import time
from googletrans import Translator
translator = Translator(raise_exception=True,service_urls=['translate.google.sm','translate.google.it'])#,timeout=5 ,user_agent='Mozilla/6.0 (Windows NT 9.0; Win64; x64)')#
#print(translator.translate('테스트')._response.http_version)

DEBUG = False
NBBATCHDONE=0

def manual_translate(english):
    import subprocess
    import re
    french = []
    for e in english:
        command='translate -s en -d fr "'+e.replace('"','\\"').replace('$','\\$')+'"'
        #print(command)
        res = subprocess.check_output(command,text = True,shell=True)
        #print(res)
        match=re.search(r'\[fr\]\s+(.*)\[pron.\]', res, re.DOTALL)

        if match:
            print('\n----------------------\n',match.group(1),'\n----------------------\n')
            french.append(match.group(1))
        else:
            print("\nechec regex:",res,"\n")
            french.append(e)
        #sys.exit()
    return french

def batch_query(po,entries):
    english =[]
    oldfrench =[]
    entree = []
    french =[]
    pb=0
    size=0
    for entry in entries:
        if entry.msgid == entry.msgstr:# and entry.msgid.find(' ')>=0: #pour ne pas refaire ceux qui ont marché et éviter les mots uniques
            english.append(entry.msgid)
            oldfrench.append(entry.msgstr)
            entree.append(entry)
            size+=len(entry.msgid)
            if DEBUG:
                french.append(entry.msgstr)
    print('batch size query=',size)   
    if size==0: #rien à traiter dans ce batch
        return 0
    if size>=5000:
        print("batch size>5000 abort before to be banned, previous batch done=",NBBATCHDONE)
        #sys.exit()
    
    french=manual_translate(english)       
    # try:
    #     if DEBUG:
    #         print('translate debug')
    #     else:
    #         french = translator.translate(english,src='en',dest='fr')                  
    #     print('\n-----------------------\n',french[0],'\n-----------------------\n')
    # except:
    #     print('\n-----------------------\n',french[0],'\n-----------------------\n')
    #     print('requête échouée, batch done',NBBATCHDONE)
    #     po.save('DragonfallExtendedCompletedAuto.po')
    #     sys.exit()


    for i in range(len(french)):
        #print('-----------------------')
        #print(english[i])
        # print('       -------         ')
        # print(oldfrench[i])
        #print('       -------         ')
        #print(french[i].text)
        #print('-----------------------')
        if DEBUG:
            entree[i].msgstr=french[i]
        else:
            entree[i].msgstr=french[i]#.text
    return size


if __name__ == "__main__":
    if len(sys.argv)>1:
        print('DEBUG ON')
        DEBUG=True
    
    po = polib.pofile('DragonfallExtended.po')

    nb_entries = len(po)
    print('nb_entries=',nb_entries)
    print('translated entries  =',po.percent_translated())
    print('untranslated entries=',len(po.untranslated_entries()))
    print('fuzzies entries     =',len(po.fuzzy_entries()))
    
    entries = po.fuzzy_entries()
    batch_size=200#18
    batch=0
    size=0
    
    while(batch+batch_size<len(entries)):
        print('batch=',batch,' totalsizequery=',size)
        # if size >= 5000:
        #     print('>5000 cars processed: wait 1 minute to see')
        #     po.save('DragonfallExtendedCompletedAuto.po')
        #     time.sleep(5)
        size+=batch_query(po,entries[batch:batch+batch_size])
        batch+=batch_size
        if not DEBUG:
            time.sleep(5)
        NBBATCHDONE+=1
        if size>0:
            po.save('DragonfallExtendedCompletedAuto.po')
        print('nb_batches saved=',NBBATCHDONE," data=",size)
    #batch_query(po,entries[-batch_size:])  

    po.save('DragonfallExtendedCompletedAuto.po')
    print('nb_batch traités=',NBBATCHDONE)
