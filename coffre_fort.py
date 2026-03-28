from cryptography.fernet import Fernet
import os

# On génère et sauvegarde la clé secrète (le "cadenas")
def generer_cle():
    cle = Fernet.generate_key()
    with open("ma_cle.key", "wb") as fichier_cle:
        fichier_cle.write(cle)
    print("✅ Clé générée avec succès dans 'ma_cle.key'. Ne la perds pas !")

# On charge la clé existante
def charger_cle():
    return open("ma_cle.key", "rb").read()

# On chiffre un fichier cible
def chiffrer_fichier(nom_fichier, cle):
    f = Fernet(cle)
    
    # On lit le fichier original
    with open(nom_fichier, "rb") as fichier:
        donnees_originales = fichier.read()
        
    # On chiffre les données
    donnees_chiffrees = f.encrypt(donnees_originales)
    
    # On écrase le fichier avec la version chiffrée
    with open(nom_fichier, "wb") as fichier:
        fichier.write(donnees_chiffrees)
        
    print(f"🔒 Le fichier '{nom_fichier}' est maintenant chiffré et illisible !")

#  TEST 
if __name__ == "__main__":
    
    generer_cle()
    
    
    cle_actuelle = charger_cle()
    
    
    chiffrer_fichier("votre_fichier.txt", cle_actuelle)
    pass
