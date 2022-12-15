from random import randint #para importar desde la librearia random, randint
def loto():
    valid=0
    lista=[]
    cont=1
    while cont<=6:
        num=randint(0,41)
        valid=lista.count(num) #comprueba que no sea repetido
        if valid==0:
            lista.append(num)
            cont+=1
    lista.sort()
    return lista
#Para retornar cuantos aciertos hay
def aciertos(numeros,loto):
    aciertos=0
    for n in numeros:
        acierto=loto.count(n)#si n(n=numero en numeros) esta en loto, acierta
        aciertos+=acierto#aciertos cuenta la cantidad de aciertos
    return acierto