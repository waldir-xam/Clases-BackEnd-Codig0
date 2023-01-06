# Programacion oriendata a Objetos
# Abstraccion
# Clase : Control del TV
# encender
# apagar
# cambiar_canal
# bajar_volumen
""" class Mueble:
    precio = 0.00
    tipo = ""
    color = "" """

# Con constructor


"""     def __init__(self, tipo, precio=0.00, color=""):
        self.precio = precio
        self.tipo = tipo
        self.color = color """

# Metodo de instancia
"""     def indicarTipo(self):
        print(f"El tipo es {self.tipo}")
"""

# Instancia de una clase
# sofa_cama = Mueble()
# sofa_cama = Mueble(tipo="Sofa cama")
# sofa_cama.indicarTipo()

# silla = Mueble()
# silla = Mueble(tipo="Silla")
# silla.indicarTipo()

# Encapsulamiento
""" class Usuario:
    def __init__(self, usuario, contrasenia):
        self.usuario = usuario
        self.__contrasenia = contrasenia
        self.contrasenia = self.__encriptarConstrasenia()
        self.__rol = ""
 """
# Primera forma
"""     def __getAtributo(self):
        return self.__rol

    def __setAtributo(self, valor):
        self.__rol = valor
    rol_dos = property(__getRol, __setRol) """

##### Segunda Forma
# Getter
"""     @property
    def rol_dos(self):
      return self.__rol """

# Setter
"""     @rol_dos.setter
    def rol_dos(self.valor):
      self.__rol=valor


    def __encriptarConstrasenia(self):
        return f"PASS!{self.__contrasenia}"

    def mostrarContrasenia(self):
        return self.__contrasenia


pepito = Usuario("pepito", "123456")
print(pepito.usuario)
print(pepito.contrasenia)
print(pepito.mostrarContrasenia()) """

# Herencia

# clase padre
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        def hablar(self):
            pass


# clase hijo
class Perro(Mascota, ClaseDos):
    def __init__(self, nombre, edad, duenio):
        super(Mascota).__init__(
            nombre, edad
        )  # si la clase hijo va a heredar mas de un padre de pone super(nombreClasePadre)
        ClaseDos().__init__()
        self.duenio = duenio

    def hablar(self):
        print("Guau!")


# clase hijo
class Gato(Mascota):
    def hablar(self):
        print("Miau!")


dino = Perro("Dino", 3)
print(dino.nombre)
print(dino.edad)
dino.hablar()

mimi = Gato("mimi", 2)
print(mimi.nombre)
print(mimi.edad)
mimi.hablar()


# Polimorfismo
