'''
Created on 26 nov. 2019

@author: martha
'''

class Tarjeta:
    def Accept(self,v):
        pass
   
class TarjetaBanorte(Tarjeta):
    def Accept(self,v):
        print("Tarjeta banorte aceptada")
        v.VisitTarjetaBanorte(self)

class TarjetaBanamex(Tarjeta):
    def Accept(self,v):
        print("Tarjeta banamex aceptada")
        v.VisitTarjetaBanamex(self)
class Visitor:
    def VisitTarjetaBanorte(self, elem):
        pass
    def VisitTarjetaBanamex(self, elem):
        pass
class ConcreteVisitor1(Visitor):
    
    def VisitTarjetaBanamex(self, elem):
        print("Tarjeta Banamex")
        
    def VisitTarjetaBanorte(self, elem):
        print("Tarjeta Banorte")
    
    
class ConcreteVisitor2(Visitor):
    
    def VisitTarjetaBanamex(self, elem):
        print("Tarjeta Banamex")
        
    def VisitTarjetaBanorte(self, elem):
        print("Tarjeta Banorte")
        
class Cliente():        
    elements=[]
    banorte=TarjetaBanorte()
    banamex=TarjetaBanamex()

    elements.append(banorte)
    elements.append(banamex)

    v1=ConcreteVisitor1()
    v2=ConcreteVisitor2()

    for elem in elements:
        elem.Accept(v1)
        elem.Accept(v2)
    

       
    
        
        
        
    
    

