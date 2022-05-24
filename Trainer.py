from Rucksack import Rucksack

class Trainer(object):

    def __init__(self,name):
        self.name = name
        self.orden = []
        self.rucksack=Rucksack()

    def fangen(self, Pokemon):
        if Pokemon.trainer==None:
            if Pokemon.hitPos(90) == True:
                Pokemon.trainer = self.name
                print(f"Du hast {Pokemon.name} gefangen.")
            else:
                print(f"Du hast {Pokemon.name} verfehlt.")
            self.rucksack.pokeball -= 1
        elif Pokemon.trainer==self.name:
            print(f"{Pokemon.name} gehört bereits dir.")
        else:
            print(f"Du kannst {Pokemon.name} nicht fangen. Es gehört bereits {Pokemon.trainer}.")

    def showStats(self):
        print(
            f"Name: {self.name}\nOrden: {self.orden}\nPokemon: {self.pokemon}\n")

    def heiltrank(self, Pokemon):
        if Pokemon.trainer != self.name:
            print(f"Das ist nicht dein Pokémon.")
        else:
            if self.rucksack.heiltrank != 0:
                if Pokemon.lebenspunkte>=Pokemon.maxlebenspunkte:
                    print(f"{Pokemon.name} hat bereits volle Lebenspunkte.")
                else:
                    self.rucksack.heiltrank -= 1
                    Pokemon.lebenspunkte = Pokemon.lebenspunkte + int(Pokemon.maxlebenspunkte/2)
                    if Pokemon.lebenspunkte>=Pokemon.maxlebenspunkte:
                        Pokemon.lebenspunkte=Pokemon.maxlebenspunkte
                    print(f"Du hast {Pokemon.name} einen Trank gegeben. {Pokemon.name}'s Lebenspunkte betragen {Pokemon.lebenspunkte}/{Pokemon.maxlebenspunkte}.")
            else:
                print("Du hast keine Heiltränke mehr übrig.")