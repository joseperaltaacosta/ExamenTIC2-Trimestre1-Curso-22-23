'''4-.Crea una función que NO reciba ningún parámetro y que imprima por pantalla las opciones: 1-Sumar 2-Salir'''
def ejer1():
    print("1-Sumar\n2-Salir")

'''5-.Crea una función que reciba dos números y devuelva la suma de estos números.'''
def ejer2(num1:int,num2:int):
    suma=num1+num2
    return(suma)

'''6-.El programa principal tiene que mostrar el menú de la función y hasta que se pulse la opción 2-Salir el programa tiene que funcionar.
salir=0
while salir!=2:
    print("1-Sumar\n2-Salir")
    salir=int(input("Pulsa 1 para sumar o 2 para salir:"))'''

'''7-.Si se pulsa la opción 1, el programa pide al usuario dos números y con la ayuda de la función sumar mostrar por pantalla el resultado.
salir=0
while salir!=2:
    print("1-Sumar\n2-Salir")
    salir=int(input("Pulsa 1 para sumar o 2 para salir:"))
    if salir!=2:
        num1=0
        num2=0
        num1=int(input("Dime un numero:"))
        num2=int(input("Dime otro numero:"))
        print(num1,"+",num2,"=",num1+num2)'''

'''8-.Cuando el usuario introduce dos números se puede equivocar e introducir caracteres con lo que el programa se interrumpe.
 Realiza los cambios necesarios para controlar estos errores.'''
salir=0
while salir!=2:
    try:
        while salir!=2:
            print("1-Sumar\n2-Salir")
            salir=int(input("Pulsa 1 para sumar o 2 para salir:"))
            if salir==1:
                num1=0
                num2=0
                num1=int(input("Dime un numero:"))
                num2=int(input("Dime otro numero:"))
                suma=num1+num2
                print("La suma es:",suma)
    except:
        print("Solo se pueden introducir numeros")
if salir==2:
    print("HAS TERMINADO")