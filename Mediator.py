'''
Created on 25 nov. 2019

@author: martha
'''
class Mediator:
    def EnviarPeticion(self, peticion, personaObj):
        pass
    
class ConcreteMediator(Mediator):
    def SetPersonas(self,persona1Obj, persona2Obj):
        self.persona1=persona1Obj
        self.persona2=persona2Obj
            
    def EnviarPeticion(self, peticion, personaObj):
        if personaObj==self.persona1:
            self.persona2.RecibirPeticion(peticion)
        elif personaObj==self.persona2:
            self.persona1.RecibirPeticion(peticion)

class Persona:
    def __init__(self,mediatorObj):
        self.mediator=mediatorObj
        
    def EnviarPeticion(self, peticion):
        pass
    def RecibirPeticion(self,peticion):
        pass
    
class ConcretePersona1(Persona):
    def __init__(self,mediatorObj):
        self.mediator=mediatorObj
        
    def EnviarPeticion(self,peticion):
        self.mediator.EnviarPeticion(peticion, self)
        
    def RecibirPeticion(self, peticion):
        print('Persona1 recibe la peticion ',peticion)
        
        
class ConcretePersona2(Persona):
    def __init__(self,mediatorObj):
        self.mediator=mediatorObj
        
    def EnviarPeticion(self,peticion):
        self.mediator.EnviarPeticion(peticion, self)
        
    def RecibirPeticion(self, peticion):
        print('Persona2 recibe la peticion ,',peticion)
        
        
Administrador=ConcreteMediator()

trabajador1=ConcretePersona1(Administrador)

trabajador2=ConcretePersona2(Administrador)

Administrador.SetPersonas(trabajador1,trabajador2)

trabajador1.EnviarPeticion("Solicitud de nuevo equipo de computo")
trabajador2.EnviarPeticion("Vacaciones")
        
        
        

        
        
    
        
                