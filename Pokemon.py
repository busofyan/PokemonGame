import random

class Pokemon(object):

    def __init__(self):
        self.name = None
        self.pokedex = None
        self.maxlebenspunkte = 60
        self.lebenspunkte = self.maxlebenspunkte
        self.trainer = None
        self.level = 1
        self.angriffswert = 1.2

    def changeTrainer(self, trainer):
        self.trainer = trainer

    def lvlUp(self):
        if self.level < 100:
            self.level += 1
            self.lebenspunkte = int(self.lebenspunkte+1.03**self.level)
            print(f"{self.name} erreicht Level: {self.level}")
            if self.level == 20:
                print(f"Hey! {self.name} entwickelt sich zu: ")
                self.name = "Schillok"
                print(self.name)
            elif self.level == 40:
                print(f"Hey! {self.name} entwickelt sich zu: ")
                self.name = "Turtok"
                print(self.name)
        else:
            print(f"{self.name} hat bereits die höchste Levelstufe: {self.level} erreicht.")

    def showStats(self):
        print(
            f"Name: {self.name}\nLevel: {self.level}\nPokedex-Nr: {self.pokedex}\nLebenspunkte: {self.lebenspunkte}\nTrainer: {self.trainer}")

    def hitPos(self, possibility):
        pos = random.randrange(0, 100, 1)
        if pos <= possibility:
            return True
        return False

    def entwickeln(self):
        if self.level == 20 and self.name == "Schiggy":
            print(f"{self.name} hat sich entwickelt zu: ")
            self.name = "Schillok"
            print(self.name)
        elif self.level == 40 and self.name == "Schillok":
            print(f"{self.name} hat sich entwickelt zu: ")
            self.name = "Turtok"
            print(self.name)
        else:
            print(f"{self.name} ist noch nicht soweit, sich zu entwickeln.")

    def trank(self):
        if self.lebenspunkte>=self.maxlebenspunkte:
            print(f"{self.name} hat bereits volle Lebenspunkte.")
        else:
            self.lebenspunkte = self.lebenspunkte + int(self.maxlebenspunkte/2)
            if self.lebenspunkte>=self.maxlebenspunkte:
                self.lebenspunkte=self.maxlebenspunkte
            print(f"Du hast {self.name} einen Trank gegeben. {self.name}'s Lebenspunkte betragen {self.lebenspunkte}/{self.maxlebenspunkte}.")