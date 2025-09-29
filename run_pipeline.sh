#!/bin/bash

# Exécuter lint
echo "Exécution de lint..."
make lint
if [ $? -eq 0 ]; then
    echo "Lint OK, lancement du pipeline..."
    # Exécuter toutes les tâches du Makefile si lint est OK
    make all
else
    echo "Erreur lint, pipeline arrêté"
fi
