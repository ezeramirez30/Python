import tkinter as tk
from calculos import calculoEdad

window= tk.Tk()
window.geometry("400x300")
window.title("Calculo edad")

hello= tk.Label(text="Ingrese su fecha de nacimiento\n en formato DD/MM/AAAA", font=("nonito",16))
hello.pack()
def edad():
    fecha=eFechaNac.get()
    lista=fecha.replace("-","/")
    barras=lista.count("/")
    if barras==2:
        lista=fecha.split("/")
        try:
            edad=calculoEdad(int(lista[0]), int(lista[1]), int(lista[2]))
            salida["text"]=edad
            salidaError["text"]=""
            if edad<0:
                salidaError["text"]="Usted todavia no nacio"
                salida["text"]=""
        except:
            salidaError["text"]="Formato de fecha incorrecto"
            salida["text"]=""
    else:
        salidaError["text"]="Formato de fecha incorrecto"
        salida["text"]=""
    
eFechaNac=tk.Entry(width=20)
eFechaNac.pack()
button= tk.Button(text="Calcular edad", command= edad)
button.pack()

salida=tk.Label(text="", font=("nonito",16))
salida.pack()

salidaError=tk.Label(text="", font=("nonito",16), fg="Red")
salidaError.pack()


tk.mainLoop()
