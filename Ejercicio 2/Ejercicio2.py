class Animal:
    def comer(self):
        print('El animal esta comiendo')

class Mamifero(Animal):
    def amamantar(self):
        print('EL animal esta amamantando')


class Ave(Animal):
    def volar(self):
        print('El animal esta volando')


class Murcielago(Mamifero,Ave):
        pass


muric = Murcielago()

muric.amamantar()
muric.comer()
muric.volar()

