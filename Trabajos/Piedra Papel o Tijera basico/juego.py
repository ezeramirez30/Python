def piedraPapelTijera(selecU, selecPc):
    ganador=""
    if selecU==selecPc:
        print("Empate, ambos eligieron: ",selecU)
        ganador=""
    elif selecU==1:
        if selecPc==2:
            print("Gana la pc ya que papel mata piedra")
            ganador="Maquina"
        elif selecPc==3:
            print("Gana el usuario ya que piedra mata tijera")
            ganador="Usuario"
    elif selecU==2:
        if selecPc==1:
            print("Gana el usuario porque papel mata piedra")
            ganador="Usuario"
        elif selecPc==3:
            print("Gana la pc ya que tijera mata papel")
            ganador="Maquina"
    elif selecU==3:
        if selecPc==1:
            print("Gana la pc ya que piedra mata tijera")
            ganador="Maquina"
        elif selecPc==2:
            print("Gana el usuario ya que tijera mata papel")
            ganador="Usuario"
    print(selecU, selecPc)
    return ganador