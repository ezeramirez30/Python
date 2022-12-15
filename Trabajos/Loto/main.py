#hacer un programa que nos elija 6 numeros para jugar al loto
from loto import loto, aciertos
from guardar import guardar
numeros=[]
cont=0
while cont<6:
    aux=0
    try: #prueba hacer esto
        numero=int(input("Ingrese los numeros de su carton: "))
        while numero<0 or numero>41:
            print("Numero no valido")
            numero=int(input("Por favor, reingrese los numeros de su carton: "))
    except: #si no se puede hace esto
        print("El programa solo aceptas datos numericos del tipo entero")
        continue#devuelve el control al principio del while
    aux=numeros.count(numero)#para no ingresar numeros repetidos
    if aux==0:
        numeros.append(numero)
        cont+=1
numeros.sort()
print(numeros)
loto=loto()
print(loto)
print(aciertos(numeros,loto))
guardar(numeros,loto,aciertos(numeros,loto))