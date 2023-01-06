# Funcion open (file,mode)
# MODE:
#r -> Leer - Lectura
# x-> Crea el archivo, si existe ya el archivo retorna un error
archivo = open("prueba.txt","r")

#al abrir un archivo en modo lectura tenemmos 2 funciones:
#read()-> Retornara el contenido del archivo
#print(archivo.read())
#readlines()->Retorna una lista con los valores por linea
#print(archivo.readlines())

for linea in archivo:
  print(linea)