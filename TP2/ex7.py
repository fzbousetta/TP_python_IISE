class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        if isinstance(livre, Livre):
            self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :")
            for livre in self.livres:
                print(livre)
