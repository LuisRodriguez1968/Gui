import tkinter as tk
import time

app=tk.Tk()
app.iconbitmap("icono.ico")
app.title("Aplicacion")
app.geometry("1000x500+300+50")
#app.minsize(900,600)
#app.maxsize(1100,700)
app.resizable(False,False)
app.configure(bg="lightblue")
app.attributes("-alpha",0.9)

marco=tk.Frame(app)
marco.configure(width=600,height=400,bd=25,bg="yellow")
submarco=tk.Frame(marco)
submarco.configure(width=400,height=300,bd=5,bg="red")

btn1=tk.Button(app,text="Botón de app")
btn2=tk.Button(marco,text="Botón de marco 1")
btn3=tk.Button(submarco,text="Botón de marco 1")

etqapp=tk.Label(app,text="Etiqueta de la app",bg="red",padx=10,pady=10) 

def actualizarHora():
    etqapp.config(text=time.strftime("%H:%M:%S"),fg="blue",bg="yellow",font=("Arial",12,"bold"))
    etqapp.after(1000,actualizarHora)

etqmarco=tk.Label(marco,text="Etiqueta del marco",bg="red",padx=10,pady=10) 
etqsubmarco=tk.Label(submarco,text="Etiqueta del submarco",bg="red",padx=10,pady=10) 

actualizarHora()

marco.pack()
submarco.pack()
btn1.pack()
btn2.pack()
btn3.pack()
etqapp.pack()
etqmarco.pack()
etqsubmarco.pack()
app.mainloop()
actualizarHora()