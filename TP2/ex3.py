
class CompteBancaire:

    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde

    def deposer(self,montant):
        somme=self.solde + montant
        print(somme)
    
    def retirer(self,montant):
        if self.solde > montant :
           newsolde = self.solde - montant
           print (newsolde)
        else :
            print('Erreur: solde insuffisant')
        
    def afficher_solde(self):
        print(self.solde)

compte=CompteBancaire('th',10000)
compte.deposer(1000)
compte.retirer(15000)
compte.afficher_solde()