class Parteh:
    def __init__(self, name):
        self.name = name
    def __masarapnafood(self):
        print(f"Espesyal na pagkain: {self.name}")
    def NocheBuenas(self):
        print("Lechon Manok, Lumpia, Bibingka")
        self.__masarapnafood()
    def MediasNoche(self):
        print("Carbonara, Pork Belly, Pizza")
        self.__masarapnafood()

kare2x = Parteh("Kare-kare")
kare2x.NocheBuenas()
sisig = Parteh("Sisig")
sisig.MediasNoche()