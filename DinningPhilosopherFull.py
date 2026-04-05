import threading
import time
import random


class DiningPhilosophers:
    
    def __init__(self):
        
        self.forks = []
        for idx in range(5):
            self.forks.append(threading.Lock())
        self.output = [] #registro de aciones    
        self.lock_output = threading.Lock() #proteger escritura , crea un objeto bloqueado
        
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
        
        #Estrategia para evitar el deadlock
        #sentido de liberar recursos?
        #forma de ordenar que nunca se traslapen los recursos?
        if philosopher % 2: # 0%2=1 ,1%2=1 , 2%2=0 
            first,second = left , right
        else: #3%2 = 1 , 4%2=1
            first,second = right , left
        
        with self.forks[first]:
            pickLeftFork(philosopher)
            self._log(philosopher , "pick_left")

            with self.forks[second]:
                pickRightFork(philosopher)
                self._log(philosopher,"pick_right")

                eat(philosopher)
                self._log(philosopher,"eat")
                
                putRightFork(philosopher)
                self._log(philosopher,"put_right")

            putLeftFork(philosopher)
            self._log(philosopher,"put_left")
        
    def _log(self,philosopher,action):
        with self.lock_output:
            self.output.append((philosopher,action))
           
#funciones simuladas
def pickLeftFork(p):
    print(f"Philosopher {p} picked LEFT fork")


def pickRightFork(p):
    print(f"Philosopher {p} picked RIGHT fork")
    
def eat(p):
    print(f"Philosopher {p} is EATING")
    time.sleep(random.uniform(0.5, 1.5))


def putLeftFork(p):
    print(f"Philosopher {p} put LEFT fork")


def putRightFork(p):
    print(f"Philosopher {p} put RIGHT fork")


def think(p):
    print(f" Philosopher {p} is thinking")
    time.sleep(random.uniform(0.5, 1.5))    

# ─────────────────────────────
# Ejecución con threads
# ─────────────────────────────

def philosopher_task(dp, i):
    while True:
        think(i)
        dp.wantsToEat(
            i,
            pickLeftFork,
            pickRightFork,
            eat,
            putLeftFork,
            putRightFork
        )


if __name__ == "__main__":
    dp= DiningPhilosophers()
    
    threads = []
    
    for i in range(5):
        t = threading.Thread(target=philosopher_task, args=(dp, i))
        t.daemon = True  # termina cuando el programa principal termina
        threads.append(t)
        t.start()
    
    time.sleep(10)
    
    print("Registro de acciones")
    for entry in dp.output:
        print(entry)
