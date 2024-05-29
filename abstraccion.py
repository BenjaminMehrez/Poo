from abc import ABC, abstractclassmethod


class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad 
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad}')


class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f'{self.nombre} esta estudiando: {self.actividad}')


class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f'{self.nombre} esta trabajando en el rubro de: {self.actividad}')


jordan = Trabajador('Jordan', 26, 'masculino', 'Web Designe')
benjamin = Estudiante('Benjamin', 21, 'masculino', 'Programacion')

jordan.presentarse()
jordan.hacer_actividad()
benjamin.presentarse()
benjamin.hacer_actividad()