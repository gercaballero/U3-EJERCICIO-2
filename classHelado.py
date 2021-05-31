from classSabor import Sabor
from classManejaSabores import ManejaSabores

class Helado:
    __gramos=0
    __sabores=[]

    def __init__(self,gramos):
        self.__gramos=gramos
        self.__sabores=[]

    def cargaSabor(self,unSabor):
        self.__sabores.append(unSabor)
    
    def __str__(self):
        sabores=''
        helado='\n GRAMOS:{}'.format(self.__gramos)
        for sabor in self.__sabores:
            sabores=sabores+('\n\t{}'.format(sabor))
        return helado+sabores
    def getGramos(self):
        return int(self.__gramos)

    def vecesSabor(self,numero):
        cont=0
        for sabor in self.__sabores:
            if sabor.getNumero()==numero:
                cont+=1
        return cont

    def gramosPorSabor(self):
        return float(self.getGramos()/int(len(self.__sabores)))
    
    def getSabores(self):
        return self.__sabores

