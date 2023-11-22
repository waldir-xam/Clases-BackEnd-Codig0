# foreach -for
meses = ["enero", "febrero", "marzo"]

""" for mes in meses:
  print(mes)
 """

# Obtener el indice y el valor
""" for index, value in enumerate(meses):
    print(index, value)
 """


# for(x=0;x>10;x++)
# 1 valor donde empeiza
# 2 hasta dnde finalziada
# 3 de cuanto en cuanto incremen tara

edad = 31
year_born = 1991

for value in range(edad):
    year_born += 1
    print(f"Em el anio {year_born} tenias {value+1} anios")
