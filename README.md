# Groupe-M-t-o-5

Projet Meteo en direct.


les installations : 

python 
apache 
maria db (mysql) 
Quelques bibliothèques pour l'ESP.
Thonny (un ide pour micropython)

Les prérequis : 

ESP8266 (A connecter au wifi pour envoyer les données a l'api)
raspberry pi 4 (hebergeur API BDD apache API) 
Ecran LCD I2C 2x16 (Pour afficher l'ip, la date et l'heure ainsi que les derniers relevés sur l'écran a base d'une torunante toutes les 3 secondes)
GY-21 HTU21 Capteur de température.
CP2104 : Connecteur usb au pc afin d'importer les fichiers sur l'esp + coder a l'interieur de celui ci en micropython


Comment on a procédé :


On a commencé par installer l'os sur le raspberry pour créer le serveur, on l'a configuré a l'aide du menu "secret" (CTRL SHIFT X) pour le configurer sur le réseau wifi et initialiser la connexion SSH

Pendant ce temps la, on a fait le branchement de tout les composants entre eux.

On a ensuite commencé le site web afin d'afficher les releves du capteur a l'aide de l'api et du serveur.
Pour se faire, nous collectons 5 valeurs afin d'en faire une moyenne et eviter les erreurs du capteur pour avoir une courbe bien représentative.
Sur le site web, nous pouvons retrouver les 5 derniers relevés de températures ainsi que d'humidité ainsi qu'un graphique se mettant à jour toutes les 3 secondes en affichant les données d'humidité ainsi que celles des températures.

Nous avons dans un même temps codé sur l'esp afin de pouvoir récuperer ces données de températures et d'humidité à l'aide du capteur pour les transmettre à l'API

Pendant ce temps, l'API à été developpé afin de pouvoir récupérer ces données, les transmettre à la base de données, les reprendre et les renvoyer au site web.
L'API sert donc de passerelle entre tout les éléments.

Pour se faire, il nous à fallu de nombreuses heures de recherche ainsi que de grandes quantités de tests.

Nous espérons que ce projet vous plaira.






