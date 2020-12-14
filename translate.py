#!/usr/bin/python3

import polib
import sys
import time
from googletrans import Translator
translator = Translator(raise_exception=True)#service_urls=['translate.google.fr']



def batch_query(po,entries):
    english =[]
    oldfrench =[]
    entree = []
    french =[]
    pb=0
    size=0
    for entry in entries:
        if entry.msgid == entry.msgstr: #pour ne pas refaire ceux qui ont marché
            english.append(entry.msgid)
            oldfrench.append(entry.msgstr)
            entree.append(entry)
            size+=len(entry.msgid)
            #french.append(entry.msgstr)
    print('batch size query=',size)   
    if size==0: #rien à traiter dans ce batch
        return 0
    if size>=5000:
        sys.exit()
    
    try:
        #toto =[]
        french = translator.translate(english,src='en',dest='fr')
        print(french[0])
    except:
        print('requête échouée')
        po.save('DragonfallExtendedCompletedAuto.po')
        sys.exit()


    for i in range(len(french)):
        #print('-----------------------')
        #print(english[i])
        # print('       -------         ')
        # print(oldfrench[i])
        #print('       -------         ')
        #print(french[i].text)
        #print('-----------------------')
        #entree[i].msgstr=french[i]
        entree[i].msgstr=french[i].text
    return size


if __name__ == "__main__":
    po = polib.pofile('DragonfallExtended.po')

    nb_entries = len(po)
    print('nb_entries=',nb_entries)
    print('translated entries  =',po.percent_translated())
    print('untranslated entries=',len(po.untranslated_entries()))
    print('fuzzies entries     =',len(po.fuzzy_entries()))
    
    entries = po.fuzzy_entries()
    batch_size=5
    batch=590
    size=0
    while(batch+batch_size<len(entries)):
        print('batch=',batch,' totalsizequery=',size)
        size+=batch_query(po,entries[batch:batch+batch_size])
        batch+=batch_size
        time.sleep(2)
    #batch_query(po,entries[-batch_size:])  

    po.save('DragonfallExtendedCompletedAuto.po')
