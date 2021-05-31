import os
from classHelado import Helado
from classSabor import Sabor
from classManejaHelados import ManejaHelados
from classManejaSabores import ManejaSabores
class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.salir
                         }
    def getSwitcher(self,MH,MS):
        return self.__switcher
    def opcion(self,op,MH,MS):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(MH,MS)

    def salir(self,MH,MS):
        print('Salida del programa')

    def opcion1(self,MH,MS):
        cont=0
        band=False
        os.system('cls')
        print('~~~VENTA HELADO~~~')
        gramos=input('-Ingrese tipo de helado (100/150/250/500/1000) gramos:')
        while not band:
            if gramos in('100','150','250','500','1000'):
                unHelado=Helado(int(gramos))
                band=True
            else:
                os.system('cls')
                print('~~~VENTA HELADO~~~')
                print('GRAMOS INCORRECTOS')
                gramos=input('-Ingrese tipo de helado (100/150/250/500/1000) gramos:')
        os.system('cls')
        print('~~~VENTA HELADO~~~')
        sabor=input('INGRESE SABOR DE HELADO: ')
        while sabor !='fin':
            unSabor=MS.comprobarSabor(sabor)   #COMPRUEBA SI EXISTE EL SABOR CARGADO
            if unSabor!=None:                  #SI RETORNA NONE, NO EXISTE, SINO RETORNA EL OBJETO SABOR
                unHelado.cargaSabor(unSabor)
                MS.contador(unSabor)
                cont+=1                         #CUANDO AGREGA EL SABOR AUMENTA EL CONTADOR
            else:
                print('SABOR NO ENCONTRADO')
            if cont==4:                         #SI EL CONTADOR LLEGA A 4, PARA DE AGREGAR
                break
            sabor=input('INGRESE SABOR DE HELADO (FIN):')
        if cont!=0:
            MH.agregarHelado(unHelado)
    
    def opcion2(self,MH,MS):
        os.system('cls')
        print('-----SABORES MAS VENDIDOS-----\n')
        MS.listar5()
        input()
        os.system('cls')

    def opcion3(self,MH,MS):
        os.system('cls')
        band=True
        num=int(input('INGRESE EL NUMERO DE UN SABOR:'))
        while band:
            #COMPRUEBA SI EXISTE EL SABOR CARGADO
            if MS.comprobarSabor(num) !=None:                  #SI RETORNA NONE, NO EXISTE, SINO RETORNA EL OBJETO SABOR
                print('LA CANTIDAD DE GRAMOS VENDIDOS DEL SABOR ES DE {}'.format(MH.gramosSabor(num)))
                band=False
            else:
                print('SABOR NO ENCONTRADO')
                num=int(input('INGRESE EL NUMERO DE UN SABOR:'))
        input()
        os.system('cls')

    def opcion4(self,MH,MS):
        os.system('cls')
        band=False
        tipo=input('-Ingrese tipo de helado (100/150/250/500/1000) gramos:')
        while not band:
            if tipo in('100','150','250','500','1000'):
                print('TIPO DE HELADO --{} GRAMOS--'.format(tipo))
                MH.saborPorTipo(int(tipo))
                band=True
            else:
                os.system('cls')
                print('GRAMOS INCORRECTOS')
                tipo=input('-Ingrese tipo de helado (100/150/250/500/1000) gramos:')
        input()
        os.system('cls')