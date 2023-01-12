# RPG

## Consigne : 

Concevoir un mini-RPG (inspiré de D&D), permettant de jouer dans un environnement, en rencontrant des personnages, des ennemis à combattre, en ayant des quêtes à accomplir ainsi que des objets à récolter.


## Design Patterns envisagés : 

- Factory : Création de personnages, ennemis, objets 
- Strategy : Gérer les actions ( combattre, loot, … ) 
- Observer : Mettre à jour les quêtes en cours, les stats etc en fonction des actions effectuées
- Singleton : Gérer l’accès à l’environnement de jeu, pour éviter les duplications et les conflits
- Decorator : Ajouter des compétences et des capacités spéciales aux persos, ennemis et objets.


## Classes prévues :

- Classe “GameEnv”, singleton pour l’accès à l'env, infos sur les persos, les ennemis et les objets présents dans l’environnement
- Classe abstraite “Entity”, classe de base pr tt les objets du jeu ( personnages, ennemis, objets), infos sur l’objet genre nom, stats, …
- Classe “LivingEntity” hérite de “Entity”, niveau, nom, stats, etc.
- Classe “Player”, hérite de la classe “LivingEntity”, xp, inventaire.
- Classe “NPC”, hérite de la classe “LivingEntity”, dialogues.
- Classe “Enemy”, hérite de “NPC”, et par extension de “LivingEntity” et de “Entity”.
- Classe “Item”, hérite de la classe “Entity”, utilisation, valeur…
- Classe “Quest”, infos sur les quêtes, objectifs à remplir, récompenses à obtenir.
- Classe abstraite “Action”, pour gérer les actions des persos, genre combattre, récolter des objets etc. D’autres classes en héritent ( Combat, Récolte ).
- Classe “Factory”, qui utilise le pattern Factory pour créer les objets du jeu.
- Classe “Decorator”, pour ajouter des compétences et des capacités aux persos, ennemis et objets.
- Classe “Observer”, pour mettre à jour les quêtes et stats en fonction des actions.
