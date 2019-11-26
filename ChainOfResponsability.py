'''
Created on 25 nov. 2019

@author: martha
'''


class Handler:
    def __init__(self):
        self.successor=None
    def HandleRequest(self, solicitud):
        pass
    def Sucesor(self, handlerObj):
        self.successor=handlerObj
class Administrador(Handler):
    def HandleRequest(self, solicitud):
        print("Administrador ", solicitud)
        if solicitud=="Vacaciones":
            print("Esta solicitud no puede ser atendida")
            
        elif self.successor!=None:
            self.successor.Handle(solicitud)

class Director(Handler):
    def HandleRequest(self, solicitud):
        print("Director ", solicitud)
        if solicitud=="Hora libre":
            print("Es atendida por el administrador")
            
        elif self.successor!=None:
            self.successor.Handle(solicitud)
    
        
        
class Cliente(Handler):       
    p1=Administrador()
    p2=Director()
    p1.Sucesor(p2)


    p1.HandleRequest("Vacaciones")
    p2.HandleRequest("Hora libre")