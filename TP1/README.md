# TP1
1. [Objecif](#Objectif)
2. [Mise en place](#Mise-en-place)
3. [Explication de dockerfile](#Explication-de-dockerfile)
4. [Explication docker-compose.yml](#Explication-docker-compose.yml)


## Objectif

L'objectif de ce TP est de mettre en place une app Flask et de récupérer, grace à Prometheus, diverses informations.\
Ces informations seront utilisées dans grafana pour construire un graph.

## Mise en place

### Requirement
Par-feu VM docker sur Azure\
	- ouvrir le port 5000 : app flask\
	- ouvrir le port 3000 : grafana\
	- ouvrir le port 9090 : prometheus\
Mettre Ubuntu a jour avec "sudo apt update && sudo apt upgrade -y"

### Etape 1

git clone https://github.com/kuramentooo/TP1.git

#### Installer Docker et Docker Compose
"sudo apt install docker docker-compose"

### Etape 2

Changer l'adresse IP dans le fichier prometheus/prometheus.yml

### Etape 3

Lancer en etant dans TP1/, "sudo docker-compose up -d"

### Etape 4

Ce connecter a grafane avec 'votre.ip:3000'\
Ajouter DataSource prometheus avec l'ip:port de votre prometheus, puis save&test\
Ajouter un dashboard avec la requete "flask_http_request_duration_seconds_count"\
Save le dashboard

## Explication de dockerfile

Dans le DockerfileFlask, on vient dire quelle version de python on veut utiliser>\
Ensuite on copy les differents fichiers que l'on souhaite avoir dans notre conteneur, ici on copy app.py et requierements.txt\
Ensuite avec pip on install ce qui se trouve dans requirements.txt, donc\
	- Flask==3.0.2\
	- docker==5.0.3\
	- docker-compose==1.29.2\
	- dockerpty==0.4.1\
	- prometheus-flask-exporter==0.23.0\
 	- prometheus_client==0.20.0\

## Explication docker-compose.yml

Dans le docker-compose on vient seter les informations pour conteneurs.\
Pour le conteneur flask app on dit d'utiliser le DockerfileFlask et d'utiliser le port 5000.\
Pour le conteneur prometheus on dit que si le conteneur flask_app est present, il sera accessible depuis le port 9090.\
Pour le conteneur gafana on dit dit que si le conteneur prometheus est present, il sera accessible depuis le port 3000.
