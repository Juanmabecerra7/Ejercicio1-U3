from ManejaFacultades import ManejaFacultades

 
if __name__=="__main__":
    MF = ManejaFacultades()
    MF.test()
    print(str(MF))
    n=1
    while n != 0:
        print("1: dado un codigo de una facultad se le mostrara informacion")
        print("2: dado un nombre de una carrera, motrar informacion")
        print ("3: salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            codigo = input ("ingrese el codigo de una facultad: ")
            MF.punto1(codigo)
        elif opcion == 2:
            nombre = input("inrese el nombre de una carrera: ")
            MF.punto2(nombre)
        elif opcion == 3:
            exit()
        else:
            print (" OPCION INCORRECTA ")
            
