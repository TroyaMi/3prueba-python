# crear variable que contenga un texto y mostrar el tipo de la variable

def main():

    Texto = "Ingenieria de sistemas"
    print(Texto)
    print(type(Texto))

 

#crear otra variable que almacene la longitud de la variable anterior
    Facultad = "Ingenieria de sistemas"
    print(Facultad)
    print(len(Facultad))

#crear otra variable que almacene la primera variable pero en mayusculas.
    Profesion = "Ingenieria de sistemas"
    print(Profesion)
    print(Profesion.upper())

#crear otra variable que concatene la variable mayusculas y la variable de longitud

    concatenacion = "Ingenieria" + " de" + " sistemas"
    print(concatenacion)
    print(len(concatenacion))


main()