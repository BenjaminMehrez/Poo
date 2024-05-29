class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')


name = input('Como es tu nombre: ')
edad = int(input('Pasame tu edad: '))
grado = input('Cual es tu grado: ')

estudiante1 = Estudiante(name,edad,grado)

estudiante1.estudiar()