import time

class Logger:

    def __init__(self,stream):
        #receive the timestamps
        self.msg_stream = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #Each unique msg should only be printed every 10 seconds
        if self.timestamp >= 10   


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
