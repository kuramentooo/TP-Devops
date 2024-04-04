# TP1

## Objectif

L'objectif de ce TP est de mettre en place une app Flask et de recuperer grace a Prometheus d'iverses informations.\
Ce informations seront utiliser dans grafana pour construire un graph.

## Mise en place

### Requirement
Par-feu VM docker sur Azure\
	- ouvrir le port 5000 : app flask\
	- ouvrir le port 3000 : grafana\
	- ouvrir le port 9090 : prometheus\
Mettre Ubuntu a jour avec "sudo apt update && sudo apt upgrade -y"\

### Etape 1

git clone https://github.com/kuramentooo/TP-Devops.git

#### Installer Docker et Docker Compose\
"sudo apt install docker docker-compose"

### Etape 2

Changer l'adresse IP dans le fichier prometheus/prometheus.yml

### Etape 3

Lancer en etant dans TP-Devops/TP1/, "sudo docker-compose up -d"

### Etape 4

Ce connecter a grafane avec 'votre.ip:3000'\
Ajouter DataSource prometheus avec l'ip:port de votre prometheus, puis save&test\
Ajouter un dashboard avec la requete "flask_http_request_duration_seconds_count"\
Save le dashboard

## Explication de dockerfile


