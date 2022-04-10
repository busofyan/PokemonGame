from Pokemon import Pokemon
class Nebulak(Pokemon):

    def __init__(self):
        super().__init__()
        self.name = "Nebulak"
        self.geisterball_att = 6

    def geisterball(self,Pokemon):
        if Pokemon==self:
            print (f"{self.name} kann sich nicht selbst angreifen.")
        elif Pokemon.lebenspunkte <= 0:
            print(f"Du kannst nicht angreifen. {Pokemon.name} wurde schon besiegt.")
        elif self.lebenspunkte <= 0:
            print(f"Du kannst nicht angreifen. Dein Pokemon {self.name} wurde besiegt.")
        else:
            if self.hitPos(80) == True:
                print(f"{self.name} attakiert {Pokemon.name} mit Geisterball und verursacht {int(self.angriffswert*self.geisterball_att)} Schaden:")
                Pokemon.lebenspunkte = Pokemon.lebenspunkte - int(self.angriffswert*self.geisterball_att)
                if Pokemon.lebenspunkte > 0:
                    print(f"{Pokemon.name} hat noch {Pokemon.lebenspunkte} Lebenspunkte.")
                else:
                    Pokemon.lebenspunkte = 0
                    print(f"{Pokemon.name} wurde besiegt.")
            else:
                print(f"{self.name} hat {Pokemon.name} verfehlt.")