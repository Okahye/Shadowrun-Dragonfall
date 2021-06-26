# Shadowrun-Dragonfall

Branche secondaire de la traduction en français de Dragonfall

Toutes les traductions automatiques non vérifiées manuellement (56% du total) qui avaient été générées au départ (probablement 2015) ont été remplacées par des traductions de google translate (décembre 2020) de bien meilleure qualité

## Instructions pour jouer en français

1. <https://github.com/Okahye/Shadowrun-Dragonfall/raw/master/DragonfallExtended.mo> version compilée contenant 49% de dialogues en français vérifiés manuellement et le reste en anglais
2. <https://github.com/pepin-de-landen/Shadowrun-Dragonfall/blob/master/FullFrench.mo> traduction complète (version compilée) où les dialogues non vérifiés sont françisés automatiquement par Google Translate (51% d'entre eux sont potentiellement incorrects)

Comment installer la traduction ?

1. Allez dans \Shadowrun Dragonfall Director’s Cut\Dragonfall_Data\StreamingAssets\ContentPacks\DragonfallExtended\data\
2. Créez un répertoire "loc" puis
3. Créez un répertoire "fr" dans le répertoire loc
4. Copiez le fichier "DragonfallExtended.mo" dans le répertoire "fr" (ou le fichier "FullFrench.mo" sous le nom "DragonfallExtended.mo")
5. ou bien le fichier "FullFrench.mo" avec  44% de traductions vérifiées et 56% de traductions automatiques issues de Google Translate

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
