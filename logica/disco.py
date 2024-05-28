class Disco:
    def __init__(self, codigo, nombre, artista, num_canciones, precio):
        self._codigo=codigo
        self._nombre=nombre
        self._artista=artista
        self._num_canciones= num_canciones
        self._precio=precio
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,valor):
        self._codigo=valor

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,valor):
        self._nombre=valor
    
    @property
    def artista(self):
        return self._artista
    
    @artista.setter
    def artista(self,valor):
        self._artista=valor

    @property
    def num_canciones(self):
        return self._num_canciones
    
    @num_canciones.setter
    def num_canciones(self,valor):
        self._num_canciones=valor

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,valor):
        self._precio=valor


    
    


