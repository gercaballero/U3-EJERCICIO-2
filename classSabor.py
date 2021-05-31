

class Sabor:
    __numero=0
    __nombre=''
    __descripcion=''
    __contador=0

    def __init__(self,numero,nombre,desc):
        self.__numero=numero
        self.__nombre=nombre
        self.__descripcion=desc
        self.__contador=0
    
    def __str__(self):
        return ('NUMERO:{}\tNOMBRE:{:15}\tDESCRIPCION:{}'.format(self.__numero,self.__nombre.upper(),self.__descripcion))
    
    def getNombre(self):
        return self.__nombre
    def getNumero(self):
        return int(self.__numero)
    def contar(self):
        self.__contador+=1
    
    def __gt__(self,unSabor):
        if isinstance(unSabor, Sabor):
            return (self.__contador>unSabor.__contador)
        
    def __eq__(self,unSabor):
        retorna=None
        if isinstance(unSabor, Sabor):
            retorna= self.__nombre==unSabor.__nombre
        if type(unSabor)==int:
            retorna= self.getNumero()==unSabor
        if type(unSabor)==str:
            retorna= self.getNombre()==unSabor
        return retorna