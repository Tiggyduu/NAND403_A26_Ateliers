Hello l'artiste!

Voici l'application qui ouvre une fenêtre dans Maya pour te permettre d'entrer un message personnalisé qui s'affichera dans une autre fenêtre. C'est un outil super utile dans le pipeline et tu dois l'installer obligatoirement, sinon je ne serai pas content. Heureusement pour toi, j'ai fait une belle documentation qui t'explique quoi faire :

//----------------------------------------------------------------------------------------------------//

Installation : 

// Créer un shelf pour vos outils

1. Ouvrir Maya

2. Dans l'onglet "shelf tabs", cliquez sur le symbole d'engrenage. 
 
    2.1 -> Naviguer le menu et appuyez sur "new shelf"

3. Une fenêtre "create new shelf" vous demandera d'entrer un nom pour votre nouvelle shelf
 
    3.1 -> Tapez "outils" ou un nom de votre choix
 
    3.2 -> Cliquez "ok"

** Vous avez maintenant votre propre shelf pour mettre vos outils



// Ajouter vos outils dans votre shelf

1. Ouvrez l'onglet "windows"
 
    1.1 -> Naviguer le menu vers "general editors"
 
    1.2 -> Appuyez sur "script editor"

2. Dans l'onglet "script editor", selectionnez "python"

3. Copiez le code fourni dans le fichier "application.py" (ctrl + a -> ctrl + c)

4. Collez le code dans l'onglet "python" du script editor (ctrl + v)

5. Sélectionnez le code dans le "script editor" (ctrl +a)

    5.1 -> faites un clic gauche soutenu sur le code

    5.2 -> Glissez le vers votre shelf

6. Une fenêtre "save script to shelf as type" s'ouvrira

    6.1 -> Sélectionnez "python"

** Votre outil est maintenant fonctionnel



// Ajouter un icon custom

1. Dans l'explorateur de fichier, trouver "User\Documents\maya\2025\prefs\icons"

    1.1 -> Ajoutez l'icon fourni dans ce dossier

// Vous pouvez placer l'icon ailleurs si vous préfeéez

2. Faites un clic droit sur l'icon par défaut de votre nouvel outil

    2.1 - > Cliquez "edit"

3. Une fenêtre "shelf editor" s'ouvrira

    3.1 -> Dans l'onglet "shelves", sélectionner votre shelf

    3.2 -> Dans l'onglet "shelf contents", sélectionnez l'outil

    3.3 -> Utilisez l'option "rename" pour donnez un nom à votre outil (ex: message board)

    3.4 -> Dans la section "icons preview", trouvez "icon name"

    3.5 -> Appuyer sur le symbole de dossier

    3.6 -> Naviguer vers "User\Documents\maya\2025\prefs\icons" (ou le path que vous avez choisi)

    3.7 -> Sélectionnez l'icon, puis appuyez sur "open"

    3.8 -> Fermez l'onglet "shelf editor"

** Votre outil a maintenant son propre icon custom

//----------------------------------------------------------------------------------------------------//

J'espère que ces instructions t'auront aidé. Fais bon usage de ce précieux code et n'oublie jamais : Le vrai outil, c'est les amis que tu t'es faits en cours de route.