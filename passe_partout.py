from cryptography.fernet import Fernet
import os

def dechiffrer_fichier(nom_fichier, cle):
    
    f = Fernet(cle)
    
    with open(nom_fichier, "rb") as fichier:
        donnees_chiffrees = fichier.read()

    donnees_dechiffrees = f.decrypt(donnees_chiffrees)

    with open(nom_fichier, "wb") as fichier:
        fichier.write(donnees_dechiffrees)

    print(f"🔒 Le fichier '{nom_fichier}' est maintenant déchiffré et lisible !")

if __name__ == "__main__":
    
    #On charge la clé
    clef = open("ma_cle.key", "rb").read()
    
    #On déchiffre notre fichier secret
    dechiffrer_fichier("votre_fichier.txt", clef)
    
    pass
