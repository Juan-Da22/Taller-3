class Electrodomestico:
    PRECIO_BASE = 100
    COLOR_POR_DEFECTO = "blanco"
    CONSUMO_ENERGETICO_POR_DEFECTO = 'F'
    PESO_POR_DEFECTO = 5
    
    def __init__(self, precio=PRECIO_BASE, peso=PESO_POR_DEFECTO, color=COLOR_POR_DEFECTO, consumo_energetico=CONSUMO_ENERGETICO_POR_DEFECTO):
        self._precio_base = precio
        self._peso = peso
        self._color = self.comprobar_color(color)
        self._consumo_energetico = self.comprobar_consumo_energetico(consumo_energetico) 
    
    def comprobar_consumo_energetico(self, letra):
        letras_validas = ['A', 'B', 'C', 'D', 'E', 'F']
        if letra.upper() in letras_validas:
            return letra.upper()
        else:
            return self.CONSUMO_ENERGETICO_POR_DEFECTO
    
    def comprobar_color(self, color):
        colores_validos = ['blanco', 'negro', 'rojo', 'azul', 'gris']
        if color.lower() in colores_validos:
            return color.lower()
        else:
            return self.COLOR_POR_DEFECTO
    
    def precio_final(self):
        incremento = 0
        if self._consumo_energetico == 'A':
            incremento += 300
        elif self._consumo_energetico == 'B':
            incremento += 80
        elif self._consumo_energetico == 'C':
            incremento += 60
        elif self._consumo_energetico == 'D':
            incremento += 50
        elif self._consumo_energetico == 'E':
            incremento += 30
        elif self._consumo_energetico == 'F':
            incremento += 10
            
        if self._peso >= 0 and self._peso < 20:
            incremento += 10
        elif self._peso >= 20 and self._peso < 50:
            incremento += 50
        elif self._peso >= 50 and self._peso < 80:
            incremento += 80
        elif self._peso >= 80:
            incremento += 100
            
        return self._precio_base + incremento

class Lavadora(Electrodomestico):
    CARGA_POR_DEFECTO = 5
    
    def __init__(self, precio=Electrodomestico.PRECIO_BASE, peso=Electrodomestico.PESO_POR_DEFECTO, color=Electrodomestico.COLOR_POR_DEFECTO, consumo_energetico=Electrodomestico.CONSUMO_ENERGETICO_POR_DEFECTO, carga=CARGA_POR_DEFECTO):
        super().__init__(precio, peso, color, consumo_energetico)
        self._carga = carga
    
    def precio_final(self):
        precio_final = super().precio_final()
        if self._carga > 30:
            precio_final += 50
        return precio_final

class Television(Electrodomestico):
    RESOLUCION_POR_DEFECTO = 20
    SINTONIZADOR_TDT_POR_DEFECTO = False
    
    def __init__(self, precio=Electrodomestico.PRECIO_BASE, peso=Electrodomestico.PESO_POR_DEFECTO, color=Electrodomestico.COLOR_POR_DEFECTO, consumo_energetico=Electrodomestico.CONSUMO_ENERGETICO_POR_DEFECTO, resolucion=RESOLUCION_POR_DEFECTO, sintonizador_TDT=SINTONIZADOR_TDT_POR_DEFECTO):
        super().__init__(precio, peso, color, consumo_energetico)
        self._resolucion = resolucion
        self._sintonizador_TDT = sintonizador_TDT
    
    def precio_final(self):
        precio_final = super().precio_final()
        if self._resolucion > 40:
            precio_final *= 1.3
        if self._sintonizador_TDT:
            precio_final += 50
        return precio_final

class Ejecutable:
    def main(self):
        electrodomesticos = [
            Electrodomestico(120, 10, "negro", "A"),
            Lavadora(200, 20, "rojo", "B", 35),
            Television(300, 25, "azul", "C", 50, True),
            Electrodomestico(),
            Lavadora(),
            Television()
        ]
        
        precio_total_electrodomesticos = 0
        precio_total_lavadoras = 0
        precio_total_televisiones = 0
        
        for electrodomestico in electrodomesticos:
            precio_final = electrodomestico.precio_final()
            precio_total_electrodomesticos += precio_final
            if isinstance(electrodomestico, Lavadora):
                precio_total_lavadoras += precio_final
            elif isinstance(electrodomestico, Television):
                precio_total_televisiones += precio_final
        
        print("Precio total de todos los electrodomésticos:", precio_total_electrodomesticos)
        print("Precio total de todas las lavadoras:", precio_total_lavadoras)
        print("Precio total de todas las televisiones:", precio_total_televisiones)

# Ejemplo de uso
if __name__ == "__main__":
    ejecutable = Ejecutable()
    ejecutable.main()
