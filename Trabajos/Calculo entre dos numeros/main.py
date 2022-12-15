import tkinter as tk

ventana= tk.Tk()
ventana.title("Sumar")
ventana.geometry("400x300")

numU=0
num2U=0 

def sumar():
    try:
        numU=float(num1.get())
        num2U=float(num2.get())
        resultado["text"]="El resultado de la suma es "+str(numU+num2U)
        etiquetaError["text"]=""
    except:
        etiquetaError["text"]="Solo se pueden ingresar datos numericos"
      
def restar():
    try:
        numU=float(num1.get())
        num2U=float(num2.get())
        resultado["text"]="El resultado de la resta es "+str(numU-num2U)
        etiquetaError["text"]=""
    except:
        etiquetaError["text"]="Solo se pueden ingresar datos numericos"

def multiplicar():
    try:
        numU=float(num1.get())
        num2U=float(num2.get())
        resultado["text"]="El resultado del producto es "+str(numU*num2U)
        etiquetaError["text"]=""
    except:
        etiquetaError["text"]="Solo se pueden ingresar datos numericos"

def dividir():
    try:
        numU=float(num1.get())
        num2U=float(num2.get())
        resultado["text"]="El resultado de la division es "+str(numU//num2U)
        etiquetaError["text"]=""
    except:
        etiquetaError["text"]="Solo se pueden ingresar datos numericos"

etiqueta=tk.Label(text="Ingrese un numero a sumar ", font="nolito") 
etiqueta.pack()

num1=tk.Entry() 
num1.pack()                          

etiqueta1=tk.Label(text="Ingrese un numero a sumar")
etiqueta1.pack()

num2=tk.Entry()
num2.pack()

buttonSumar= tk.Button(text="Sumar", command=sumar)
buttonSumar.pack()

buttonResta=tk.Button(text="Resta", command=restar)
buttonResta.pack()

buttonMulti= tk.Button(text="Producto", command=multiplicar)
buttonMulti.pack()

buttonDiv=tk.Button(text="Dividir", command=dividir)
buttonDiv.pack()

resultado= tk.Label(text="", bg="yellow")
resultado.pack()

etiquetaError=tk.Label(text="", fg="red")
etiquetaError.pack(side="bottom")

tk.mainloop()