import sys
import os
absolute_path = os.path.dirname(__file__)
print(absolute_path)
relative_path = "../logica"
full_path = os.path.join(absolute_path, relative_path)
print(full_path)

sys.path.insert(0, full_path)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from discografia import Discografia
from disco import Disco


class Formulario:
    def __init__(self, root):
        self.discografia=Discografia()

        self.root=root
        self.root.title("Gestion de discos de Audio")
        self.root.geometry("400x400")

        #self.form=ttk.Frame(root)

        # Labels y las cajas de texto
        tk.Label(self.root, text="Código: ").grid(row=0, column=0, padx=10, pady=10)
        self.input_codigo=tk.Entry(self.root)
        self.input_codigo.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root,text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
        self.input_nombre=tk.Entry(self.root)
        self.input_nombre.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root,text="Artista:").grid(row=2, column=0, padx=10, pady=10)
        self.input_artista=tk.Entry(self.root)
        self.input_artista.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root,text="Numero canciones:").grid(row=3, column=0, padx=10, pady=10)
        self.input_num_canciones=tk.Entry(self.root)
        self.input_num_canciones.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root,text="Precio:").grid(row=4, column=0, padx=10, pady=10)
        self.input_precio=tk.Entry(self.root)
        self.input_precio.grid(row=4, column=1, padx=10, pady=10)

        self.btn_guardar= tk.Button(self.root, text="Guardar", command=self.guardar_disco)
        self.btn_guardar.grid(row=5, column=0,pady=10)

        self.btn_limpiar= tk.Button(self.root, text="Limpiar", command=self.limpiar_controles)
        self.btn_limpiar.grid(row=5, column=1,pady=10)

        self.tabla= ttk.Treeview(self.root, show="headings",
                                 columns=("Codigo", "Nombre", "Artista", "Canciones", "Precio") )
        
        self.tabla.grid(row=6, columnspan=2, padx=10, pady=10)
        self.tabla.bind('<ButtonRelease-1>', lambda event:self.seleccionar_disco())
        self.tabla.heading("Codigo", text="Codigo")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Artista",text="Artista")
        self.tabla.heading("Canciones",text="Canciones")
        self.tabla.heading("Precio", text="Precio ($)")

        self.mostrar_discos()

  
    def seleccionar_disco(self):
        print('SE HA EJECUTADO EL METODO')
        selected_row=self.tabla.selection()[0]
        self.limpiar_controles()
        codigo= self.tabla.item(selected_row,"values")[0]
        self.input_codigo.insert(tk.END,codigo)
        nombre= self.tabla.item(selected_row,"values")[1]
        self.input_nombre.insert(tk.END,nombre)
        artista= self.tabla.item(selected_row,"values")[2]
        self.input_artista.insert(tk.END,artista) 
        canciones= self.tabla.item(selected_row,"values")[3]
        precio= self.tabla.item(selected_row,"values")[4]
        self.input_num_canciones.insert(tk.END,canciones)
        self.input_precio.insert(tk.END,precio)
    def guardar_disco(self):
        try:
            codigo=self.input_codigo.get()
            nombre=self.input_nombre.get()
            artista=self.input_artista.get()
            num_canciones=int(self.input_num_canciones.get())
            precio= float(self.input_precio.get())
            disco=Disco(codigo,nombre,artista,num_canciones,precio)
            if self.discografia.buscar_codigo(codigo):
                # Si ya esta, se modifica
                self.discografia.modificar_disco(disco)
                messagebox.showinfo("Modificacion","Disco modificado exitosamente")
            else:
                # Si no, se registra
                self.discografia.agregar_disco(disco)
                messagebox.showinfo("Insercion", "Disco insertado exitosamente")
            self.mostrar_discos()
        except:
            messagebox.showerror("Error", "Ingrese números válidos.")
            

    def limpiar_controles(self):
        print('Entro a la funcion')
        self.input_codigo.delete(0, tk.END)
        self.input_nombre.delete(0, tk.END)
        self.input_artista.delete(0, tk.END)
        self.input_precio.delete(0, tk.END)
        self.input_num_canciones.delete(0, tk.END)   

    def mostrar_discos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for disco in self.discografia.lista_discos:
            self.tabla.insert('','end',
                              values=[disco.codigo, disco.nombre, disco.artista,disco.num_canciones, disco.precio])
            



root=tk.Tk()
formulario=Formulario(root)
root.mainloop()
