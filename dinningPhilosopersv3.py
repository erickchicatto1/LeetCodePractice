import threading

class DiningPhilosophers:
    
    def __init__(self):
        
        self.forks = []
        for idx in range(5):
            self.forks.append(threading.Lock())
        self.output = threading.Lock()
        
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork,
                   pickRightFork,
                   eat,
                   putLeftFork,
                   putRightFork):

        #numbers of philosophers
        left = philosopher
        right = (philosopher + 1) % 5 #sentido de las manecillas del clk?
        
        if philosopher % 2:
            first,second = left , right
        else:
            first,second = right , left
        
    
    def pickLeftFork(self):
        #como indicar el numero o que un filoso esta utilizando este metodo?
        if self.PickflagLeft == None:
            self.PickflagLeft = True
            if self.PickflagLeft:
                return self.SecuenceOutput.append([0][1]) , self.SecuenceOutput.append([0][1][1]) # esto estara correcto?
                
            
    def pickRightFork(self):
        if self.PickflagRight == None:
            self.PickflagRight = True
            if self.PickflagRight:
                return self.SecuenceOutput.append([0][2]) , self.SecuenceOutput.append([0][2][1])
                
                
    def eat(self):
        if self.PickflagLeft == True and self.PickflagRight == True:
            print(f"The philosoper number is eating {self.philosopher}")
            self.PickflagLeft = None #cuando un filosofo termino de comer , libera los 2 tenedores
            self.PickflagRight = None
            return self.SecuenceOutput.append([0][3])
        
            
    def putLeftFork(self):
        pass
    
    
    def putRightFork(self):
        pass


if __name__ == "__main__":
    
    philosopher1 = threading.Thread(target=)
    philosopher2 = threading.Thread(target=)
    philosopher3 = threading.Thread(target=)
    philosopher4 = threading.Thread(target=)
    philosopher5 = threading.Thread(target=)
    
    GroupOfPhiloshopers = [philosopher1,philosopher2,philosopher3,philosopher4,philosopher5]
    
    #como hacer que un filosofo espere a que otro esten disponibles?
    #como hacer que los threads esten en horario clockwise
    #como hacer o empezar a hacer pruebas?
    for i in GroupOfPhiloshopers:
        print(f"filosofos recorridos {i}")
        
        
