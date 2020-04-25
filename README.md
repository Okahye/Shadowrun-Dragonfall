# Shadowrun-Dragonfall
Branche principale de la traduction en français de Dragonfall

Fichier de traduction : https://github.com/Okahye/Shadowrun-Dragonfall/blob/master/DragonfallExtended.html
(Faites download pour visualiser le en local)

## 1 - Instructions de traduction

**Attention, il n'est pas possible de travailler en simultané sur le fichier**
Merci donc de respecter ces instructions pour vos sessions de traduction.

Avant de commencer, vérifiez que vous êtes bien à jour !
**git pull origin master**

A la fin de chaque session, n'oubliez pas d'uploader vos modifications avant de laisser la main à quelqu'un d'autre.
1. Sauvegardez votre fichier DragonfallExtended.po sous Poeditor pour générer le fichier .mo
2. Sous Poeditor Faites "Fichier" et "Exporter en HTML" et sauvegardez DragonfallExtended.html dans le même répertoire.
3. Commit via **git commit -a**  ou équivalent via **git add -A** puis **git commit**, pour plus de clarté le message du commit peut indiquer les segments traduits ou relus (commit -m "Segments: XXXX à XXXX") mais ce n'est pas absolument obligatoire.
4. Push via **git push**


## 2 - Instructions pour tester in-game

Lien vers la traduction actuelle (version compilée) :
https://github.com/Okahye/Shadowrun-Dragonfall/raw/master/DragonfallExtended.mo

Comment installer la traduction ?
1. Allez dans \Shadowrun Dragonfall Director’s Cut\Dragonfall_Data\StreamingAssets\ContentPacks\DragonfallExtended\data\
2. Créez un répertoire "loc" puis
3. Créez un répertoire "fr" dans le répertoire loc
4. Copiez le fichier "DragonfallExtended.mo" dans le répertoire "fr"

Note : Le chemin complet doit être \Shadowrun Dragonfall Director’s Cut\Dragonfall_Data\StreamingAssets\ContentPacks\DragonfallExtended\data\loc\fr\

Mais pour que les fichiers soient utilisés il faut passer son jeu en français (voir section suivante)

 Comment passer son jeu en français ?
1. Installez le jeu et lancez-le une première fois (permet d'initialiser les clefs dans l'éditeur de registre)
2. Ouvrez Regedit.exe
3. Allez dans HKEY_CURRENT_USER\Software\Harebrained Schemes\Dragonfall
4. Double-cliquez sur Settings.Language_h2828946908
5. Changez la valeur "NONE" en "FR"
6. Fermez regedit et lancez le jeu

Une fois dans le jeu, vous devriez voir les menus en français (youpi!). Mais attention !
Lorsque vous créez une nouvelle campagne, après la création du personnage, l'écran de chargement et les dialogues sont en anglais (damned!).
Bizarrement, le jeu ne prend pas en compte les fichiers de traduction lorsqu'on démarre une nouvelle campagne.
Pas de panique, il vous suffit de revenir au menu principal (ou de redémarrer le jeu) puis charger la partie sauvegardée automatiquement et le jeu passera en français.

Bon jeu à tous !
