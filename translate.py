#!/usr/bin/python3

import polib
import sys
from googletrans import Translator
translator = Translator()#service_urls=['translate.google.fr']



def batch_query(po,batch=100):
    english =[]
    oldfrench =[]
    entree = []
    pb=0
    for entry in po.fuzzy_entries():
        #entry.flags.remove('fuzzy')
        if entry.msgid == entry.msgstr:
            english.append(entry.msgid)
            oldfrench.append(entry.msgstr)
            entree.append(entry)
            pb+=1
            if pb > batch:
                break
    french =[]
    try:
        french = translator.translate(english,src='en',dest='fr')
        print(french[0])
    except:
        print('requête échouée')
        sys.exit()


    for i in range(len(french)):
        print('-----------------------')
        print(english[i])
        # print('       -------         ')
        # print(oldfrench[i])
        print('       -------         ')
        print(french[i].text)
        print('-----------------------')
        entree[i].msgstr=french[i].text

def nbechecs(po):
    nb=0
    for entry in po.fuzzy_entries():
        if entry.msgid == entry.msgstr:
            nb+=1
    return nb

if __name__ == "__main__":
    po = polib.pofile('DragonfallExtended.po')

    nb_entries = len(po)
    print('nb_entries=',nb_entries)
    print('translated entries  =',po.percent_translated())
    print('untranslated entries=',len(po.untranslated_entries()))
    print('fuzzies entries     =',len(po.fuzzy_entries()))
    
    echecs=nbechecs(po)
    while(echecs>0):
        print('nbechecs=',echecs)
        batch_query(po,2)
        echecs=nbechecs(po)
        sys.exit()

    po.save('DragonfallExtendedCompletedAuto.po')
