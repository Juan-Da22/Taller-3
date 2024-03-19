import random

class Persona:
    SEXO_POR_DEFECTO = 'H'
    BAJO_PESO = -1
    PESO_IDEAL = 0
    SOBREPESO = 1
    
    def __init__(self, nombre="", edad=0, sexo=SEXO_POR_DEFECTO, peso=0.0, altura=0.0):
        self._nombre = nombre
        self._edad = edad
        self._DNI = self.generar_DNI()
        self._sexo = sexo
        self._peso = peso
        self._altura = altura
        
    def calcular_IMC(self):
        imc = self._peso / (self._altura ** 2)
        if imc < 20:
            return self.BAJO_PESO
        elif 20 <= imc <= 25:
            return self.PESO_IDEAL
        else:
            return self.SOBREPESO
    
    def es_mayor_de_edad(self):
        return self._edad >= 18
    
    def comprobar_sexo(self, sexo):
        if sexo.upper() in ['H', 'M']:
            return sexo.upper()
        else:
            return self.SEXO_POR_DEFECTO
    
    def generar_DNI(self):
        dni_numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        dni_letra = 'TRWAGMYFPDXBNJZSQVHLCKE'[int(dni_numeros) % 23]
        return dni_numeros + dni_letra
    
    def mostrar_nombre(self):
        return self._nombre
    
    def mostrar_edad(self):
        return self._edad
    
    def mostrar_sexo(self):
        return self._sexo
    
    def mostrar_peso(self):
        return self._peso
    
    def mostrar_altura(self):
        return self._altura
    
    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Sexo: {self._sexo}, Peso: {self._peso}, Altura: {self._altura}, DNI: {self._DNI}"

class Ejecutable:

    def ingresar_datos():
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        sexo = input("Ingrese el sexo (H/M): ").upper()
        peso = float(input("Ingrese el peso (kg): "))
        altura = float(input("Ingrese la altura (m): "))
        return nombre, edad, sexo, peso, altura
    
    def ejecutar():
        nombre, edad, sexo, peso, altura = Ejecutable.ingresar_datos()
        persona1 = Persona(nombre, edad, sexo, peso, altura)
        persona2_datos = Ejecutable.ingresar_datos()
        persona2 = Persona(*persona2_datos)
        persona3 = Persona()
        persona3._nombre = "Juan"
        persona3._edad = 30
        persona3._sexo = "H"
        persona3._peso = 80.0
        persona3._altura = 1.75
        
        for persona in [persona1, persona2, persona3]:
            imc = persona.calcular_IMC()
            if imc == Persona.BAJO_PESO:
                print(f"{persona.mostrar_nombre()} está por debajo de su peso ideal.")
            elif imc == Persona.PESO_IDEAL:
                print(f"{persona.mostrar_nombre()} está en su peso ideal.")
            elif imc == Persona.SOBREPESO:
                print(f"{persona.mostrar_nombre()} tiene sobrepeso.")
            
            if persona.es_mayor_de_edad():
                print(f"{persona.mostrar_nombre()} es mayor de edad.")
            else:
                print(f"{persona.mostrar_nombre()} no es mayor de edad.")
                
            print(persona)

Ejecutable.ejecutar()