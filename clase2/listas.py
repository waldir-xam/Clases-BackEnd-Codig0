# Ayya => JS
# lista (LIst)

# valores      0           1          2
personas = ["Brayan", "Bruno", "Daniel ", "Eduardo"]
# print(personas[1])

# funciones
# append => agrega un valor a la lsita (se agrega al ultimo)
personas.append("Diego")
print(f"append->{personas}")

# inset => agrega un valor a la lsita, le indicaremos que indice o posicion estara
personas.insert(0, "eduardo")
print(f"insert->{personas}")

# extend->unir dos listas
personas_nuevas = ["giovany", "henry", "isabel", "jean"]
personas.extend(personas_nuevas)
print(f"extend->{personas}")

# remove ->eliminar un valor de la lista
personas.remove("Bruno")
print(f"remove->{personas}")

# pop->eliminar el valor indicado por el indice
personas.pop(5)
print(f"pop->{personas}")

# sort ->ordenar los valores de una lista
# reverse = False =>menor a mayor
# reverse = True => mayor amenor
personas.sort(reverse=True)
print(f"sort->{personas}")

# count->retorna las veces que existe el
eduardo_contador = personas.count("Eduardo")
print(f"count->{eduardo_contador}")

# len ->cuenta los elementos de uan vairable/length
print(f"Total de Personas: {len(personas)}")
