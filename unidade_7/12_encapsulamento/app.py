class Aviao():
    __asas = 2

    def __init__(self, marca):
        self.marca = marca
    def mostrar_asas(self):
        print("O Avião tem %d asas" % self.__asas)


aviao = Aviao("Avioes hora de codar")
print(aviao.marca)

aviao.mostrar_asas()