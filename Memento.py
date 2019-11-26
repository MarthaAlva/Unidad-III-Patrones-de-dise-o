class Memento:
    def __init__(self, value):
        self.state=value
        
    def SetState(self, value):
        self.state=value
            
    def GetState(self):
        return self.state
            
class Originator:
    def SetState(self, value):
        self.state=value
        
    def GetState(self):
        return self.state
    
    def CreateMemento(self):
        return (Memento(self.state))
    
    def SetMemento(self, memento):
        print("Precio anterior del producto")
        self.state=memento.GetState()

class Producto:
    def __init__(self,originatorObj):
        self.memento=None
        self.origin=originatorObj
     
   
    def Execute(self):
        self.memento=self.origin.CreateMemento() 
        self.origin.SetState(110)
        
    def Unexecute(self):
        self.origin.SetMemento(self.memento)
class Cliente:       
    originator=Originator()

    originator.SetState(130)
    print("Nuevo precio", originator.GetState())

    Producto=Producto(originator)
    Producto.Execute()
    print("El valor inicial:", originator.GetState())

    Producto.Unexecute()
    print("El precio actual es :", originator.GetState())
