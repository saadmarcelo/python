class Mamifero():
    def __init__(self, patas, cauda):
        self.patas = patas
        self.cauda = cauda

    def  andar(self):
        print("O mamifero andou!")

class Cachorro(Mamifero):
    def __init__(self, patas, cauda, raca, macho):
        super().__init__(patas, cauda)
        self.raca = raca
        self.macho = macho
    def latir(self):
        print("Au Au!")
class Gato(Mamifero):
    def __init__(self, patas, cauda, cor, castrado):
        super().__init__(patas, cauda)
        self.cor = cor
        self.castrado = castrado
    def miar(self):
        print("Miau!")

goku = Cachorro(4, True, "Maltes", True)

print(goku.cauda)
print(goku.raca)

goku.andar()
goku.latir()