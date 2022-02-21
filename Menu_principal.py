#lADY GAUIN GUSÑAY
#INGENIERIA DE SOFTWARE

from listas import Lista
from Main import Menu
from pilas import Stack
from colas import Tails
import os
os.system("cls")
men = Menu()
lis = ["1)Listas","2)Pilas","3)Colas","4)Salir"]
alternativa = ""
while alternativa != "4":
    os.system("cls")
    alternativa = men.menu(lis)
    if alternativa == "1":
        alt1 = ""
        lista = Lista()
        while alt1 != "8":
            os.system("cls")
            alt1 = men.menu (["1.push", "2.pop", "3.show", "4.posicion a eliminar" , "5.insertar", "6.buscar", "7.vaciar ", "8. salir"])
            if alt1 == "1":
                for x in range(4):
                    val =input("Ingrese elementos a la lista :")
                    lista.Agregar(val)
            elif alt1 == "2":
                    lista.Eliminar()
            elif alt1 == "3":
                    lista.Mostrar()
            elif alt1 == "4":
                    while True:
                            indice= int(input("Posicion a Eliminar: "))
                            os.system("cls")        
                            a = lista.EleminarEle(indice)
                            if a == True:
                                break
                            else:
                                print("La posicion no se encuentra")
                                os.system("cls")      
            elif alt1 == "5":
                    pos=int(input("ingrese una posición: "))
                    dato = input("ingrese un elemento nuevo: ")
                    lista.InsertarEle(pos,dato)
            elif alt1 == "6":
                    while True:
                            dato=input("ingrese el valor que desee saber en que posicion se encuentra: ")
                            os.system("cls")        
                            li = lista.Buscar(dato)
                            if li == True:
                                break
                            else:
                                print("La posicion no se encuentra")
                                os.system("cls")         
            elif alt1 == "7":
                    lista.Vaciar()
            elif alt1 == "8":
                    print("saliendo al menu principal")
                    os.system("cls")
    if alternativa == "2":
        alt1 = ""
        tama = int(input("ingrese el tamaño de la pila: "))        
        pila = Stack(tama)
        while alt1 != "6":
            os.system("cls")
            alt1 = men.menu (["1)Push", "2)Pop", "3)Show", "4)Buscar" , "5)Longitud", "6)Salir"])
            if alt1 == "1":
                valor=input("Ingrese contenid a la pila: ")
                pila.push(valor)
            elif alt1 == "2":
                print(pila.pop())
            elif alt1 == "3":
                pila.show()
            elif alt1 == "4":
                while True:
                    buscado=input("ingrese el contenido que desee saber en que posicion esta: ")
                    os.system("cls")        
                    li = pila.buscar(buscado)
                    if li == True:
                        break
                    else:
                        print("La posicion no se ha encontrado")
                        os.system("cls") 
            elif alt1 == "5":
                pila.longitud()
            elif alt1 == "6":
                    print("saliendo al menu principal")
                    os.system("cls")
    if alternativa == "3":
        alt1 = ""
        tama = int(input("ingrese el tamaño de la cola: "))        
        cola = Tails(tama)
        while alt1 != "6":
            os.system("cls")
            alt1 = men.menu (["1)Push", "2)Pop", "3)Show", "4)Buscar" , "5)Longitud", "6)Salir"])
            if alt1 == "1":
                valor=input("Ingrese elementos a la cola: ")
                cola.push(valor)
            elif alt1 == "2":
                print(cola.pop())
            elif alt1 == "3":
                cola.show()
            elif alt1 == "4":
                while True:
                    buscado=input("ingrese el valor que desee encontrar: ")
                    os.system("cls")        
                    li = cola.buscar(buscado)
                    if li == True:
                        break
                    else:
                        print("La posicion no se encuentra")
                        os.system("cls") 
            elif alt1 == "5":
                cola.longitud()
            elif alt1 == "6":
                    print("saliendo al menu principal")
                    os.system("cls")
    if alternativa == "4":
           os.system("cls")
print("gracias por su ingreso...")