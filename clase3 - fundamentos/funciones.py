# ejercicio
# crear una funciona qu reciba 2 numeros , donde el primer numero tendra un valor por defecto:10
# si la suma de ambos es un numero par, mostrar la mitad de dicha suma
# y si noes par, mostramos el resultado de dicha suma

# def numeros


# multiparametros
# signos (*-**)
# *args -> ns pertmite recibir parametros infinitos
# def alumnosInscritos(*args):
#   print(args)


# alumnosInscritos("bruno", "braya", "daniel", "diego", "giovany")

# **kwargs0>nos permite recibir parametros infinitos
# def cursosDeAlumnos(**kwargs):
#  print(kwargs)

# ejercicio 2
# crea una funcion que reciba N notas, y nos indique cuantas fueron desaprobadas y aprobadas, si la nota es mayor a 13 se considera aprobado

notas = [14, 9, 13, 11, 15, 8, 20, 6, 13, 17]


def lista_notas(notas):
    aprobados = 0
    desaprobados = 0
    for nota in notas:
        if nota > 13:
            aprobados += 1
        else:
            desaprobados += 1

    # Mostrar el resultado
    print(f"Aprobados: {aprobados}")
    print(f"Desaprobados: {desaprobados}")


lista_notas(notas)
