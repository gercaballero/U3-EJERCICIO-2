from classMenu import Menu
from classManejaHelados import ManejaHelados
from classManejaSabores import ManejaSabores

if __name__=='__main__':
    MH=ManejaHelados()
    MS=ManejaSabores()
    MS.carga()
    menu=Menu()
    salir= False           
    while not salir:
            print("\n-------------------Menu-------------------")
            print(' 1- REGISTRAR HELADO VENDIDO')
            print(' 2- LISTAR 5 SABORES MAS VENDIDOS')
            print(' 3- GRAMOS VENDIDOS')
            print(' 4- SABOR POR TIPO')
            print(' 5- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5'):
                menu.opcion(int(op),MH,MS)
                if op=='5':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")