"""
    Projet de demo pour la création d'un CD
"""

from flask import Flask
import os

# Récupération des ENV's
PORT = os.environ.get("PORT","80")
HOST = os.environ.get("HOST","0.0.0.0")

app = Flask("demo")

@app.get("/")
def hello():
    """Fonction appelé pour le chemin par default

    Returns:
        str: un message de la plus grande importance
    """
    return "Hello world ! Je suis vivant !"

if __name__ == "__main__":
    app.run(host=HOST,port=PORT)