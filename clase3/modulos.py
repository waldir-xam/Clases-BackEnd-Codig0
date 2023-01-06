# METODO 1 - NO RECOMENDADO
""" 
import camelcase

clase = camelcase.CamelCase()
texto = "hola mundo"
print(clase.hump(texto))
 """

# METODOD 2 - RECOMENDADO
from camelcase import CamelCase
from funciones import saludar

clase = CamelCase()
texto = "hola mundo"
print(clase.hump(texto))

saludar("waldir")
