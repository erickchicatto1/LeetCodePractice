class RequestLogger:
    
    def __init__(self,limit):
        self.map = {}
        self.limit = limit
        
    def message_request_decision(self,timestamp,request):
        if request in self.map:
            if timestamp - self.map[request] < self.limit:
                return False
        self.map[request] = timestamp
        return True
