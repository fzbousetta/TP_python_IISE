class personne :
    def __init__(self,nom,prenom,age) :
        self.nom= nom
        self.prenom=prenom
        self.age=age

    def se_presenter(self) :
        print('nom :',self.nom,'prenom :',self.prenom,'age :',self.age)


class Etudiant(personne):

    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule=matricule

    def etudier(self):
        return f"{self.prenom} est un etudiant" 

etudiant1 = Etudiant("Bousetta", "Fatimazahra", 21, "D134535000")
print(etudiant1.se_presenter())
print(etudiant1.etudier())