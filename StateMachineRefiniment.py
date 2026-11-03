class StateMachineVendor:
    
    def __init__(self):
        self.state = "IDLE"
        self.balance = 0.0
        self.product_prices = {
            "soda": 1.25,
            "chips": 0.75,
            "candy": 1.00
        }
        self.selected_product = None
          
    def get_state(self) -> str:
        return self.state
    
    def get_balance(self) -> float:
        return round(self.balance, 2)
    
    def insert_coin(self, coin_value: float):
        if coin_value not in [0.25, 0.10, 0.05]:
            return  # Moneda no aceptada
        
        # Transición de estado inicial
        if self.state == "IDLE":
            self.state = "ACCEPTING_COINS"
            
        # Acumular balance si estamos aceptando monedas
        if self.state == "ACCEPTING_COINS":
            self.balance = round(self.balance + coin_value, 2)
    
    def select_product(self, product: str) -> bool:
        if self.state not in ["ACCEPTING_COINS", "IDLE"]:
            return False
        
        if product not in self.product_prices:
            return False
        
        price = self.product_prices[product]
        
        if self.balance >= price:
            self.balance = round(self.balance - price, 2)
            self.selected_product = product
            self.state = "DISPENSING"
            return True
        return False

    def collect_product(self) -> str:
        if self.state != "DISPENSING":
            return ""
        
        # Corregido: usamos selected_product (con 'd') en lugar de la función
        product = self.selected_product
        self.selected_product = None  # Reseteamos la selección de forma segura
        
        # Si quedó dinero sobrante, pasamos a dar cambio, si no, volvemos a IDLE
        if self.balance > 0:
            self.state = "GIVING_CHANGE"
        else:
            self.state = "IDLE"
        
        return product if product else ""
    
    def collect_change(self) -> float:
        if self.state != "GIVING_CHANGE":
            return 0.0
        
        change = self.balance
        self.balance = 0.0
        self.state = "IDLE"
        return round(change, 2)
    
    def request_refund(self) -> float:
        if self.state != "ACCEPTING_COINS":
            return 0.0
        
        refund = self.balance
        self.balance = 0.0
        self.state = "IDLE"
        return round(refund, 2)
