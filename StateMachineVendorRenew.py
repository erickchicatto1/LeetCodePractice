class StateMachineVendor:
    
    def __init__(self):
        #Convendra inicializar los estados?        
        self.state = "IDLE"
        self.balance = 0.0
        self.product_prices = {
            "soda":1.25,
            "chips":0.75,
            "candy":1.00
        }
        self.selected_product = None
        self.varOcg = "VendingMachineOCG"
        self.varFilterCg = ["quarter","val2","nickel"]
            
    def get_state(self)->str:
        return self.state
    
    def get_balance(self)->float:
        return round(self.balance,2) #que significa este 2?
    
    def insert_coin(self,coin_value:float):
        
        if coin_value not in [0.25,0.10,0.05]:
            return 
        #State idle
        if self.state == "IDLE":
            self.state = "ACCEPTING_COINS"
            
        #State accepting coins
        if self.state == "ACCEPTING_COINS":
            self.balance += coin_value
            self.balance = round(self.balance,2) #aqui se actualiza self.balance
    
    def select_product(self,product:str)->bool:
        
        if self.state not in ["ACCEPTING_COINS","IDLE"]:
            return False
        
        if product not in self.product_prices:
            return False
        
        price = self.product_prices[product] # con esto seleccionamos en el diccionario
        
        if self.balance >= price:
            self.balance -= price
            self.balance = round(self.balance,2)
            self.selected_product = product
            self.state = "DISPENSING"
            return True
        return False
    

    def collect_product(self)->str:
        
        if self.state != "DISPENSING":
            return ""
    
        product = self.select_product
        self.select_product = None #para resetear
        
        if self.balance > 0 :
            self.state = "GIVING_CHANGE"
        else:
            self.state = "IDLE"
        
        return product
    
    def collect_change(self)->float:
        
        if self.state != "GIVING_CHANGE":
            return 0.0
        
        change = self.balance
        self.balance = 0.0 #aqui se resetea y guarda el valor en otra variable?
        self.state = "IDLE"
        return round(change,2)
    
    def request_refund(self)->float:
        
        if self.state != "ACCEPTING_COINS":
            return 0.0
        
        refund = self.balance
        self.balance = 0.0
        self.state = "IDLE"
        return round(refund,2)
        
#uso de la clase 
