from carte import *
from random import *

class JeuDeCarte:
    """Classe définissant un jeu de cartes caractérisée par
    - son nombre de cartes
    - son paquet de cartes"""

    def __CreerPaquet__(self):
        """Méthode privée pour créer le paquet de cartes classé
        par valeur et couleur : il est donc non mélangé"""
        monpaquet = []
        if self.__Nbcartes == 32:
            num_debut = 7
        else:
            num_debut = 2
        for coul in ["Carreau","Coeur", "Trèfle", "Pique"]:
            for i in range(num_debut,15,1):
                new_carte = carte.Carte(i,coul)
                monpaquet.append(new_carte)
        return monpaquet

    def __init__(self, nb): # Notre méthode constructeur
        """Constructeur de la classe JeuDeCarte"""
        self.__Nbcartes = nb
        self.__Paquet = self.__CreerPaquet__()

    def GetNbcarte(self):
        """Retourne le nombre de carte du jeu de cartes"""
        return self.__Nbcartes

    def GetPaquet(self):
        """Retourne le paquet de cartes"""
        return self.__Paquet

    def MelangerPaquet(self):
        """Mélange aléatoirement le paquet de cartes"""
        random.shuffle(self.__Paquet)
