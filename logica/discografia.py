from disco import Disco
import csv

class Discografia:
    def __init__(self):
        self._lista_discos=[]
        self.cargar_discos()

    @property
    def lista_discos(self):
        return self._lista_discos
    
    def agregar_disco(self, disco):
        if self.buscar_codigo(disco.codigo): #Busca si ya hay un disco con el mismo codigo
            print('YA EXISTE UN DISCO CON ESTE CODIGO')
        else:
            self._lista_discos.append(disco) # Se añade el disco a la lista
            self.guardar_discos()
            #print('DISCO AGREGADO EXITOSAMENTE')
            return
    
    def buscar_codigo(self, codigo_a_buscar):
        for disco in self._lista_discos:
            if codigo_a_buscar== disco.codigo:
                return True
        return False
    
    def retornar_indice(self, codigo_a_buscar):
        index=0
        for disco in self._lista_discos:
            if codigo_a_buscar== disco.codigo:
                return index
            index+=1
        return -1 # Si no encuentra el codigo retorna -1



    def modificar_disco(self, disco):
        index=self.retornar_indice(disco.codigo)
        if index!=-1:
            self._lista_discos[index]=disco
            self.guardar_discos()
        else:
            print('No se ha encontrado este disco')


    # Escribe los elementos de la lista de discos en el archivo csv
    def guardar_discos(self,archivo="discos.csv"):
        with open(archivo,'w', newline='') as file:
            writer=csv.writer(file)
            for disco in self._lista_discos:
                writer.writerow([disco.codigo, disco.nombre, disco.artista, 
                                 disco.num_canciones, disco.precio])
    
    # Carga los registros del archivo a la lista de discos
    def cargar_discos(self,archivo="discos.csv"):
        with open(archivo,'r') as file:
            reader=csv.reader(file)
            for fila in reader:
                disco=Disco(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregar_disco(disco)


discografia=Discografia()
disco1=Disco("DIS002","Nuevo Nombre","Amy Winehouse",12,15)
#disco2=Disco("DIS007","25","Adele",12,15)
#discografia.agregar_disco(disco1)
#discografia.agregar_disco(disco2)
discografia.modificar_disco(disco1)
for disco in discografia.lista_discos:
    print(disco.nombre)

