import matplotlib.pyplot as plt
import numpy as np

# Funções que geram as curvas para os 3 tipos de geradores, Fonte: Solucionário Fundamentos de Maquinas Eletricas, Chapman

class Casamento:
    def __init__(self, zo=50,zl=10,freq=100,l_linha=10,amplitude=15):
        # if r_a <0 or r_adj<0 or r_adjlim<0 : raise ValueError('invalido')
        self.zo= zo
        self.zl=zl
        self.freq= freq
        self.l_linha= l_linha
        self.amplitude= amplitude
        


class Serie(Casamento):
    
  
    def simular(self):
        
        x = np.sqrt(np.abs((np.square(self.zo)-self.zl)*((1/self.zl)-1)))
        dist = np.abs(np.arctan((x*self.zo)/(np.square(self.zo)-self.zl)))/((2*np.pi*self.freq)/300)
        

        return x, dist

class Curto(Casamento):
    
    

    def simular(self):
        
        yl = 1/self.zl
        yo=1/self.zo
        
        yl_ = np.sqrt(np.abs((np.square(yo)-yl)*((1/yl)-1)))
        dist = np.abs(np.arctan((yl_*yo)/(np.square(yo)-yl)))/((2*np.pi*self.freq)/300)
        l = np.abs(np.arctan(yo/yl_)/((2*np.pi*self.freq)/300))

        

        return  dist, l

class Aberto(Casamento):
    
    

    def simular(self):
        
        yl = 1/self.zl
        yo=1/self.zo
        
        yl_ = np.sqrt(np.abs((np.square(yo)-yl)*((1/yl)-1)))
        dist = np.abs(np.arctan((yl_*yo)/(np.square(yo)-yl)))/((2*np.pi*self.freq)/300)
        l = np.abs(np.arctan(yl_/yo)/((2*np.pi*self.freq)/300))
        

        return  dist, l
 

def main():
    
    # teste excind
    casamento = Serie(zo=5,zl=200, freq=40, l_linha= 10, amplitude =15)
    x, dist = casamento.simular()
    
    print(x)
    print(dist)
    



