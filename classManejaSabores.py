import csv
from classSabor import Sabor
class ManejaSabores:
    __Sabores=[]

    def __init__(self):
        self.__Sabores=[]
    
    def carga(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            numero=fila[0]
            nombre=fila[1]
            desc=fila[2]
            unSabor=Sabor(numero, nombre, desc)
            self.agregarSabor(unSabor)
        archivo.close()
    
    def ordenar(self):
        self.__Sabores.sort(reverse=True)
    def agregarSabor(self,unSabor):
        if isinstance(unSabor, Sabor):
            self.__Sabores.append(unSabor)
    def contador(self,sabor):
        if self.indice(sabor)!=-1:
            self.__Sabores[self.indice(sabor)].contar()
    def indice(self,sabor):
        band=True
        i=0
        while band and i<len(self.__Sabores):
            if self.__Sabores[i]==sabor:
                band=False
            else:
                i+=1
        if not band:
            retorna=i
        else:
            retorna=-1
        return retorna
    def comprobarSabor(self,sabor):
        retorna=None
        i=0
        while retorna==None and i<len(self.__Sabores):
            if self.__Sabores[i]==sabor:
                retorna=self.__Sabores[i]
            else:
                i+=1
        return retorna
    
    def listar5(self):
        self.ordenar()
        for i in range(5):
            print(self.__Sabores[i])
        