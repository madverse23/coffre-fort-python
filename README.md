# File Encryptor (Coffre-Fort Cryptographique)

## Description
Ce projet est un outil de chiffrement et de déchiffrement de fichiers développé en Python. Il utilise la cryptographie symétrique pour sécuriser des données locales en les rendant totalement illisibles sans la clé d'origine. 

Ce script a été conçu dans une optique d'apprentissage de la cybersécurité et de la manipulation de flux de fichiers.

## Technologies & Bibliothèques
- Langage : Python 3
- Bibliothèque : `cryptography` (Module `Fernet`)
- Méthode : Cryptographie Symétrique

## Fonctionnalités
1. Génération de clé : Création d'une clé cryptographique unique (`.key`).
2. Chiffrement : Verrouillage d'un fichier cible (ex: `secret.txt`) pour protéger son contenu.
3. Déchiffrement : Restauration du fichier dans son état lisible d'origine à l'aide de la clé.

## Installation et Utilisation

1. Installer les prérequis :
Assurez-vous d'avoir Python installé, puis exécutez la commande suivante dans votre terminal :
`pip install cryptography`

2. Générer une clé (Première utilisation) :
Dans le script `coffre_fort.py`, exécutez le script. Un fichier `ma_cle.key` sera généré.

3. Chiffrer / Déchiffrer :
- Appelez la fonction `chiffrer_fichier("votre_fichier.txt", cle_actuelle)` dans le script `coffre_fort.py` pour verrouiller.
- Appelez la fonction `dechiffrer_fichier("votre_fichier.txt", cle_actuelle)` dans le script 'passe_partout.py' pour déverrouiller.

