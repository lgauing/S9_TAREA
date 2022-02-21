#lADY GAUIN GUSÑAY
#INGENIERIA DE SOFTWARE

class Lista:
    def __init__(self, dat = []):
       self.dat = []

    def Agregar(self,dato):
        self.dat.append(dato)
        print(f'Se han agregado nuevos elementos a la lista : {self.dat}\n')
        
    def Eliminar(self):
        dato = self.dat.pop()
        print(f'Se elimino un numero de la lista: {self.dat}\n')
    
    def Vaciar(self):
        dato = self.dat.clear()
       


    def Mostrar(self):
         print(f'Aqui se muestra como esta actualmente la lista: {self.dat}\n')


    def InsertarEle(self,pos,dato):
        self.dat.insert(pos,dato)
        print(f'Se agrego un nuevo elemento a la lista : {self.dat}\n')
 
     
    def EleminarEle(self,indice):
        try:
            if indice <= len(self.dat):
                print("El elemento eliminado: {}".format(self.dat.pop(indice)))
                return True
        except ValueError:
            return False

    def Buscar(self,dato):
        try:
            if dato in self.dat:
                print("el elemento ingresado se encuentra en : {}".format(self.dat.index(dato)))
                return True
        except ValueError:
            return False       
    
    
    

    




