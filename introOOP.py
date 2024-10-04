class Persona:
    def __init__(self, nombre, edad, genero, ocupacion, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion
        self.nacionalidad = nacionalidad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

    def saludar(self, otra_persona):
        print(f"Hola, {self.nombre} te manda saludar {otra_persona.nombre}.")

    def informacion(self):
        print(
            f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}, Nacionalidad: {self.nacionalidad}")


# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 19, "Masculino", "Estudiante", "Mexicana")
persona2 = Persona("Victor", 10, "Masculino", "Docente", "Mexicana")
persona3 = Persona("Brenda", 19, "Femenino", "Secretaria", "Mexicana")

# Uso de los métodos
persona1.presentarse()
persona1.cambiar_ocupacion("Desarrollador de Software")
persona1.cumplir_anios()
persona1.saludar(persona2)
# Mostrar la información completa
persona1.informacion()

persona2.presentarse()
persona2.informacion()
persona3.presentarse()
persona3.informacion()