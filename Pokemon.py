import random

class Pokemon(object):

    def __init__(self):
        self.name = None
        self.first_evolv = None
        self.second_evolv = None
        self.pokedex = None
        self.maxlebenspunkte = 60
        self.lebenspunkte = self.maxlebenspunkte
        self.trainer = None
        self.level = 1
        self.angriffswert = 1
        self.maxerfahrung = 3
        self.erfahrung = 0

    def __del__(self):
        print(f"Du hast {self.name} gelöscht.")

    def attack(self,attackname,Pokemon,hitPos,angriffswert):
        if Pokemon==self:
            print (f"{self.name} kann sich nicht selbst angreifen.")
        elif Pokemon.lebenspunkte <= 0:
            print(f"Du kannst nicht angreifen. {Pokemon.name} wurde schon besiegt.")
        elif self.lebenspunkte <= 0:
            print(f"Du kannst nicht angreifen. Dein Pokemon {self.name} wurde besiegt.")
        else:
            if self.hitPos(hitPos) == True:
                print(f"{self.name} attakiert {Pokemon.name} mit {attackname} und verursacht {int(self.angriffswert*angriffswert)} Schaden:")
                Pokemon.lebenspunkte = Pokemon.lebenspunkte - int(self.angriffswert*angriffswert)
                if Pokemon.lebenspunkte > 0:
                    print(f"{Pokemon.name} hat noch {Pokemon.lebenspunkte} Lebenspunkte.")
                else:
                    Pokemon.lebenspunkte = 0
                    print(f"{Pokemon.name} wurde besiegt.")
                    self.erfahrung+=1
                    print(f"{self.name} erhält einen Erfahrungspunkt.")
                    if self.erfahrung==self.maxerfahrung:
                        self.lvlUp()
                        self.erfahrung = 0
            else:
                print(f"{self.name} hat {Pokemon.name} verfehlt.")

    def schrei(self,Pokemon):
        if Pokemon==self:
            print (f"{self.name} kann sich nicht selbst angreifen.")
        elif Pokemon.lebenspunkte <= 0:
            print(f"Du kannst nicht angreifen. {Pokemon.name} wurde schon besiegt.")
        elif self.lebenspunkte <= 0:
            print(f"Du kannst nicht angreifen. Dein Pokemon {self.name} wurde besiegt.")
        else:
            if self.hitPos(95) == True:
                print(f"{self.name} verwendet Schrei und steigert seinen Angrifsswert um 5.")
                self.angriffswert = self.angriffswert + 5
            else:
                print(f"{self.name} hat mit Schrei verfehlt.")

    def changeTrainer(self, trainer):
        self.trainer = trainer

    def lvlUp(self):
        if self.level < 100:
            self.level += 1
            self.lebenspunkte = int(self.lebenspunkte+1.03**self.level)
            print(f"{self.name} erreicht Level: {self.level}")
            if self.level == 20 and self.first_evolv != None:
                print(f"Hey! {self.name} entwickelt sich zu: ")
                self.name = self.first_evolv
                print(self.name)
            elif self.level == 40 and self.first_evolv != None:
                print(f"Hey! {self.name} entwickelt sich zu: ")
                self.name = self.second_evolv
                print(self.name)
        else:
            print(f"{self.name} hat bereits die höchste Levelstufe: {self.level} erreicht.")

    def showStats(self):
        print(
            f"Name: {self.name}\nLevel: {self.level}\nPokedex-Nr: {self.pokedex}\nLebenspunkte: {self.lebenspunkte}\nErfahrungspunkte: {self.erfahrung}\nTrainer: {self.trainer}")

    def hitPos(self, possibility):
        pos = random.randrange(0, 100, 1)
        if pos <= possibility:
            return True
        return False