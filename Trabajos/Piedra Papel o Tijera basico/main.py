import random
from juego import piedraPapelTijera #desde archivo, importo funcion
scoreMaquina=0
scoreUsuario=0
selecU=0

while selecU!=4:
    selecU=int(input("Ingrese 1 para piedra, 2 para papel o 3 para tijera o 4 para salir: "))
    try:
        if selecU==4:
            print("Fin del juego")
        selecPc=random.randint(1,3)
        ganador=piedraPapelTijera(selecU, selecPc)
        if ganador=="Usuario":
            scoreUsuario+=1
        elif ganador=="Maquina":
            scoreMaquina+=1
        print("Score usuario:",scoreUsuario)
        print("Score maquina:",scoreMaquina)
    except:
        print("Solo se pueden ingresar valores numericos, intente otra vez")

if scoreUsuario<scoreMaquina:
    print("Gano la maquina")
elif scoreUsuario>scoreMaquina:
    print("Gano el usuario")
elif scoreUsuario==scoreMaquina:
    print("Empataron")

