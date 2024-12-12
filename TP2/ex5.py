class Animal:
    def faire_du_bruit(self):
        return

class Chien(Animal):
    def faire_du_bruit(self):
        return "Woof"

class Chat(Animal):
    def faire_du_bruit(self):
        return "Meow"

chien = Chien()
chat = Chat()
print(chien.faire_du_bruit())
print( chat.faire_du_bruit())
