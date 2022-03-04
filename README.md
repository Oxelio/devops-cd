# Demo-CD

## Présentation

Ce projet a pour but de mettre en place un système de CD pour le déploiement d'une application python sur AZURE.

## Utilisation

## Liens utiles

## Bonne manière de faire
- README.md
- LICENCE
- git flow init
- créer app.py
- créer le workflows

## Manière de faire pour le changelog
'''git
git pull origin main
git checkout develop
git merge main
git add .
git commit -m "[type(fix/feat)]:[message]"
git push origin develop
git checkout main
git merge develop
git push origin main
'''
Normalement on merge et push pas comme ça sur la main mais pour l'exemple nous allons faire comme ça

## Autre truc

docker build -t "deathnote-cd:v1.0" .
docker tag deathnote-cd:v1.0 deathnoteregistry.azurecr.io/deathnote-cd:v1.0
az login
az acr login --name [nom de notre registry azure]
docker push [registry]/[image_docker]
[docker push deathnoteregistry.azurecr.io/deathnote-cd:v1.0]