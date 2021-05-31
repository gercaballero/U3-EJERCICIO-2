from classHelado import Helado
class ManejaHelados:
    __Helados=[]

    def __init__(self):
        self.__Helados=[]
    
    def agregarHelado(self,unHelado):
        if isinstance(unHelado, Helado):
            self.__Helados.append(unHelado)

    def listar(self):
        for helado in self.__Helados:
            print(helado)

    def gramosSabor(self,numero):
        retorna=0.0
        for helado in self.__Helados:
            retorna=retorna+helado.gramosPorSabor()*helado.vecesSabor(int(numero))
        return retorna
    
    def saborPorTipo(self,tipo):
        lista=[]
        for helado in self.__Helados:
            if helado.getGramos()==tipo:
                for sabor in helado.getSabores():
                    if not sabor in lista:
                        lista.append(sabor)
        if len(lista)!=0:
            for sabor in lista:
                print(sabor)
        else:
            print('NO SE REGISTRAN SABORES PARA EL TIPO DE HELADO')

