#lADY GAUIN GUSÑAY
#INGENIERIA DE SOFTWARE

class Stack:                
    def __init__(self,tamaño):
        self.lista = []
        self.tope = 0
        self.size = tamaño
     
    def empty(self):
        return self.tope == 0
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Pila está Llena")
   
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top
            
    def longitud(self):
        print(self.tope)
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,busca):
        try:
            if busca in self.lista:
                print("el elemento se encontrara en : {}".format(self.lista.index(busca)))
                return True
        except ValueError:
            return False