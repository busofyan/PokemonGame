from Pokemon import Pokemon
class Nebulak(Pokemon):

    def __init__(self, name="Nebulak"):
        super().__init__()
        self.name = name
        self.first_evolv = "Alpollo"
        self.second_evolv = "Gengar"
        self.pokedex = 92
        self.geisterball_att = 6


    def geisterball(self, Pokemon):
        self.attack("Geisterball",Pokemon,75,15)

    def tackle(self, Pokemon):
        self.attack("Tackle",Pokemon,80,8)

    def aquaknarre(self, Pokemon):
        self.attack("Aquaknarre",Pokemon,90,12)

    def kratzer(self, Pokemon):
        self.attack("Kratzer",Pokemon,95,8)