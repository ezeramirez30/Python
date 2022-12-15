#Para guardar la ca
def guardar(numeros,loto,aciertos):

    archivo=open("resultados","a")
    numerosS=""
    lotosS=""
    for numero in numeros:
        numerosS+=str(numero)+" "
    numerosS+="\n"#PARA SALTO DE LINEA
    for numero in loto:
        lotosS+=str(numero)+" "
    lotosS+="\n"
    archivo.write(numerosS)
    archivo.write(lotosS)
    archivo.write(str(aciertos)+"\n")
    archivo.close()