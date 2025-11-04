class Client:
    def __init__(self,nom, age, niveau):
        self.nom = nom
        self.age = age 
        self.niveau = niveau
    def to_dict(self):
        return{self.nom,self.age,self.niveau}