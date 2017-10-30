import sys
from tkinter import *

# irrelevate para tk, sólo para probar el boton
def mi_comando():
    print('HELLO')

mi_gui= Tk()
# mi_gui.geometry('450x405+30+30') # Opcional para definir tamano-x y posicion+ de la ventan
mi_gui.title('Nombre de Ventana')

mi_label=Label(mi_gui,text='etiqueta').pack() # without mi_gui it is go on too but its better with

mi_boton=Button(mi_gui,text='OK',command=mi_comando).pack()

mi_entrada=Entry(mi_gui,text='esto va adentro')
mi_entrada.insert(END, 'default text')
mi_entrada.pack()

# pack is a easy version, another posibilities are grid and place
# place use coordenates and grid positions




# ---------------------------------------------------
mi_gui.mainloop() # this is only a contruction if sometimes dont fuction