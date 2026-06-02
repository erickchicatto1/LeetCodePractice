
class Logger:

    def __init__(self):
        #receive the timestamps
        self.msg_stream = {} #cuanto tiempo tiene permitido volver a entrar

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #paso A: revisar si el mensaje no esta en el dicc o si el timestamp actual es mayor o igual al tiempo que tenias guardado para ese msg
        if message not in self.msg_stream or timestamp >= self.msg_stream[message]:
            #actualizamos el dict
            self.msg_stream[message] = timestamp + 10 #con esto actualizamos el tiempo 
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
