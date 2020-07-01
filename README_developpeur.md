
#Technologie

Pour ce projet, nous utilisons la bibliothèque Flask, pour le côté serveur, en tandem avec la bibliothèque Flask-socketio, qui permet une implémentation de socketIo dans flask
Côté client, nous utilisons du javascript avec socketIO, et les slides sont faites en utilisant le framework Reveal.js.

#Rooms

Le but de ce projet est de pouvoir assurer plusieurs cours différents en parallèle sur le même serveur.
Pour cela, il est indispensable de séparer les messages qui sont envoyés d'un cours à l'autre, ainsi, on évite par exemple que le changement de slides d'un prof modifie la slide d'un élève qui participe à un autre cours.

Nous avons choisis pour cela de faire des "rooms", cela permet de contenir tous les messages envoyés par socketIO dans un seul espace par cours.

Le scénario est simple : 
on stocke une liste d'urls de slides, et l'indice de la liste correspondant à la slide d'un cours correspond également à l'id de la room dans laquelle s'éffectue le cours.
Ce numéro est aussi le titre de la page html du cours

Ainsi, quand un élève ou un prof se connecte à une page, on lit le titre de cette page, et on envoie un message par socket "join" contenant le numéro de la room, ce qui connecte le client à cette room depuis le serveur.

Pour créer une nouvelle room, on append à la liste des urls, le nouvel url contenant les slides du cours, et on se voit attribuer un id pour la room, qui est le numéro courant dans la liste des urls.

#Proxy

Le proxy nous permet de modifier le DOM d'une page distante, ici le DOM des pages sur lesquels sont contenues les slides.
Le proxy fonctionne en transformant les liens distants url/index.html en /proxy/<room-id>/index.html

On notera que <room-id> représente le numéro de la room.

Pour se faire, on sépare d'abord l'url rentré par l'utilisateur professeur en deux chaines de caractères : 
une chaine appelée site, contenant dans notre example la chaine de caractères url, Ainsi qu'une chaine de charactères html, contenant par example index.html

Cela est réalisé pour différencier les dossiers, relatifs à la chaîne de caractères url, dans lesquels sont stockés les fichiers htmls, mais aussi les fichiers css et js, et le dossier reveal,
des fichiers, relatifs à index.html ou autres, qui représentent les présentations.

En effet, il est plus souhaitable qu'un professeur stocke ses fichiers html dans le même dossier, pour ne pas avoir à recopier plusieurs fois le dossier reveal par exemple.

