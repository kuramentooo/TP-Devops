# TP1
#Docker et Docker Compose

##Requirement
Par-feu VM docker sur Azure
	- ouvrir le port 5000 : app flask\ 
	- ouvrir le port 3000 : grafana\
	- ouvrir le port 9090 : prometheus\

## Etape 1

git clone https://github.com/kuramentooo/TP-Devops.git

## Etape 2

Changer l'adresse IP dans le fichier prometheus/prometheus.yml

## Etape 3

lancer en etant dans TP-Devops/TP1/, "sudo docker compose up -d"

## Etape 4

Ce connecter a grafane avec 'votre.ip:3000'
Ajouter DataSource prometheus avec l'ip:port de votre prometheus, puis save&test
Ajouter un dashboard avec la requete "flask_http_request_duration_seconds_count"
save le dashboard



