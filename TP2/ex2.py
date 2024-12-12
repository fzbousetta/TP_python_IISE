class Voiture:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee

    def afficher_info(self):
        print(f"marque: {self.marque},modele:{self.modele},age:{self.annee}")


voiture1=Voiture('m','A',2020)
voiture2=Voiture('m','g',2024)
voiture1.afficher_info()
voiture2.afficher_info()