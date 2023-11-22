# MODE:
# a-> Modifica el contenido del archivo, manteniendo lo cambios anteriores
# w-> Reemplaza todo el contennido del archivo

##archivo = open ("prueba.txt" ,"a")
#una vez abierto el archivo tenem,os dos fncio nes a utilizar:
#write -> enviar un solo valor
# /n -> agrega un salto de linea
##archivo.write("waldir apaza\n")
#writelines -> enviar mas de un valor (lista)
#archivo.close()

with opens ("prueba.txt","a") as archivo:
  archivo.write("Eduardo\n")