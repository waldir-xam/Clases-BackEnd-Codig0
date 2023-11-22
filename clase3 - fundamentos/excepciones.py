# try catch -> javascript

try:
    numero = int(input("ingresa un numero"))
    resultado = 10 / numero
    print(resultado)
except TypeError:
    print("Ocurrio un error, al converitr el dato en entero.")
except ValueError:
    print("Ocurrio un error, el valor ingresado es un texto, debe usarse un numero")
except Exception as e:
    print(e.__class__, e)
    print("Ocurrio un essos, comunicate con soporte")
else:  # se va a ejecutar a monstar, cuadno haya un error
    print(f"No hubo un error->{resultado}")
finally:  # se va a ejecutar o mostar, aunque haya o no haya error
    print("siempre")
