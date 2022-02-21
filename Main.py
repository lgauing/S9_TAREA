#lADY GAUIN GUSÑAY
#INGENIERIA DE SOFTWARE

class Menu:
    def _init_(self):
        pass
    def menu(self,alternativa):
        print("-"*10,"MENU","-"*10)
        for opcion in alternativa: 
            print(opcion)
        opc = input("Elija opcion[1...{}] : " .format(len(alternativa)))
        return opc


