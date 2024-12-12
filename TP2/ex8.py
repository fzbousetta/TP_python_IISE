class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.amis = []  

    def ajouter_ami(self, ami):
    
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami} est ajouté à la liste des amis de {self.nom}.")

    def afficher_amis(self):
    
        if self.amis:
            print("Liste des amis de:",self.nom  )
            for ami in self.amis:
                print(ami)

personne1 = Personne("fz", 21)
personne1.ajouter_ami("samira")
personne1.ajouter_ami("fatema")
personne1.ajouter_ami("noha")  
personne1.afficher_amis()
    