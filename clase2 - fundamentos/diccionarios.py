persona = {
    "nombre": "Brayan",
    "apellidos": "acuna ventosilla",
    "especialidades": [{"nombre": "Frontend"}, {"nombre": "Backend"}],
}


# persona.nombre
print(f'Nombre de la persona ->{persona["nombre"]}')
print(f'Segunda Especialidad ->{persona["especialidades"][1]["nombre"]}')

# agregar nuevo key (clave)
persona["edad"] = 30
print(f"Diccionario nuevo -> {persona}")

# update ->actualziar un diccionario
persona.update({"hobbies": ["jugar play"]})
print(f"update->{persona}")

# get->busca la clave (key) en mecnion, y retorna su valor
# print(persona["nombres"])
##print(persona.get("nombres"))

# items ->una lista de tuplas (key,value)
print(f"items->{persona.items()}")

#keys->una lista con todas las claves
print(f"items->{persona.keys()}")

#values->una lista de valores
print(f"items->{persona.values()}")

