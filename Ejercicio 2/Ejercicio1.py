class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def present(self):
        print(f'Hola soy {self.nombre} y tengo {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def pedirgrado(self):
        print(f'Grado del estudiante: {self.grado}')


person1 = Estudiante('Sergio', 24, 7)

person1.pedirgrado()