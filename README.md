# Bienvenue à la Taverne !

Entrez donc et prenez part à nos diverses activités  ! 

## Fonctionnement

Le site est composé de 3 pages différentes:
- Taverne
- Détail Client
- Détail Activité

### Taverne
*(page d'accueil)*  
La taverne est l'endroit où l'on peut voir et intéragir avec tous les clients et les activités.

### Détail Client
*(Accessible en cliquant sur le nom d'un client)*  
Affiche le détail complet du client:
- Prénom
- Photo
- Titre (du bar)
- Etat
- Lieu (ou activité)

Il est possible d'y changer l'activité d'un client. Attention cependant, un client ne peut pas aller se balader librement comme il le souhaite. Chaque activité (excepté les toilettes) ne peuvent être occupées que par une personne à la fois. Et il n'est pas question de laisser quelqu'un d'ivre jouer au poker ou faire des bras de fer !  

Le parcours d'un client doit obligatoirement suivre le parcours suivant:  
Toilettes (qui sont dans l'entrée) -> Poker -> Bras de fer -> Table  

Un client peut avoir 4 états:
- Sobre (en sortant des toilettes)
- Euphorique (en sortant victorieux du poker)
- Assoiffé (après avoir gagné son bras de fer)
- Ivre (après avoir passé un moment à la table)

Si on essaye de forcer un client qui n'est pas dans le bon état à entrer dans une activité, on voit apparaître un message d'erreur.  
De même, on ne peut pas forcer plusieurs clients dans un seul même lieu sous peine de voir appaître là aussi un message d'erreur.  
*(sauf si on a les super pouvoirs d'admin bien sûr)*  

### Détail Activité
*(Accessible en cliquant sur le nom d'une activité)*  
Affiche le détail complet de l'activité:
- Titre
- Photo
- Disponibilité / Occupant

Chaque activité a au maximum un occupant, mis à part les toilettes (magiques) qui sont disponibles à l'infini.  


## Compte admin
- Utilisateur: boxboxjason
- Mot de passe: data driven


## Détails Techniques
- Serveur Django
- Base de données sqlite3
- Rendu visuel HTML / css
- Adresse par défaut (en local): 127.0.0.1:8000
- Adresse publique: https://boxboxjason.pythonanywhere.com
- Adresse par défaut panel admin (en local): 127.0.0.1:8000/admin
- Adresse publique panel admin: https://boxboxjason.pythonanywhere.com/admin

(Evitez de vous amuser à tout casser dessus)  
