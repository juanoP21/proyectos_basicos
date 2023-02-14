from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#Función Salir del aplicativo
def salir():
    raiz.destroy()

def borrar():
    reporteT.config(state="normal")
    reporteT.delete("1.0","end")
    reporteT.config(state="disable")
    varCantidadN.set("")
    varTotalR.set("")
    
def principal():
    reporte=""
    tr=0
    cn=0
    
    respuesta=messagebox.askyesno(message="¿Desea registrar una venta?",title="")
    
    while respuesta:
        
        
        nombre=simpledialog.askstring("", "¿Cual es su nombre?")
        na=simpledialog.askinteger("", "Cuantos adultos?")
        nn=simpledialog.askinteger("", "¿Cuantos niños?")
        
        localidad=simpledialog.askstring("", "¿Que localiad desea?").upper()
        
        while (localidad!="GENERAL" and localidad!="PREFERENCIAL"):
            messagebox.showerror(message="ERROR",title="")
            localidad=simpledialog.askstring("", "¿Que localiad desea?[general o preferencial]").upper()
        
        formato=simpledialog.askstring("","¿Que formato desea?[2d o 3d]").upper()
       
        while formato!="2D" and formato!="3D":
            messagebox.showerror(message="ERROR",title="")
            formato=simpledialog.askstring("","¿Que formato desea?[2d o 3d]").upper()
        valorBoleta=determinarValorBoleta(localidad,formato)
        pago=calcularPago(na,nn,valorBoleta)
        
        reporte= nombre+"\t"+str(na)+"\t"+str(nn)+"\t"+str(pago)+"\n"
        tr+=pago
        cn+=nn
    
        reporteT.config(state="normal")
        reporteT.insert(INSERT,reporte)
        reporteT.config(state="disable")
        
        respuesta=messagebox.askyesno(message="¿Desea registrar una venta?",title="")
    varCantidadN.set(cn)
    varTotalR.set(tr)
    
def determinarValorBoleta(i,f):
    vb=0
    if f=="2D":
        if i=="GENERAL":
            vb=8000
        else:
            vb=10000
    
    elif i=="GENERAL":
        vb=14000
    else:
        vb=12000
    
    return vb
    
def calcularPago(a,n,vb):
    vp=float(a)*vb+float(n)*(vb*0.90)
    return vp
    
    
    

#Interfaz Gráfica de usuario
raiz = Tk()
raiz.resizable(0,0)
raiz.title("CINE PAR")

#contenedor Botones
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10, padx = 10)

iniciarB = Button(marco1, text="Iniciar",width=12, command=principal)
iniciarB.grid(row=1,column=0,padx=3, pady=3)
salirB = Button(marco1, text="Salir",width=12, command=salir)
salirB.grid(row=1,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Borrar",width=12, command=borrar)
borrarB.grid(row=1,column=2,padx=3, pady=3)


#contenedor Reporte
marco2 = LabelFrame(raiz, text="Reporte de Ventas - CINE")
marco2.config(bd=3, relief="sunken", padx=15,pady=15)
marco2.pack(pady= 10, padx = 10)

reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0, columnspan=2)

cantidadNLabel = Label(marco2, text="Cantidad de niños:").grid(row = 1, column = 0, sticky = "w", padx = 10, pady=5)
varCantidadN = StringVar()
cantidadNTb = Entry(marco2, width=15, state="disable",textvariable= varCantidadN)
cantidadNTb.grid(row=1, column = 1, padx = 10, pady=5,sticky = "w")

totalRLabel = Label(marco2, text="Total recaudado:").grid(row = 2, column = 0, sticky = "w", padx = 10, pady=5)
varTotalR = StringVar()
totalRTb = Entry(marco2, width=15, state="disable",textvariable= varTotalR)
totalRTb.grid(row=2, column = 1, padx = 10, pady=5,sticky = "w")

raiz.mainloop()
