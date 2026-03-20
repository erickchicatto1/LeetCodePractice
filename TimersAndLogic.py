import time

'''
ALERT_COOLDOWN = 5  # esperar al menos 5 segundos entre alertas

last_alert_time = 1000.0   # la última alerta fue en el segundo 1000
now             = 1003.5   # ahora estamos en el segundo 1003.5

now - last_alert_time = 3.5   # solo pasaron 3.5s → bloqueado ✗

# más tarde...
now = 1006.0
now - last_alert_time = 6.0   # pasaron 6s > 5 → ¡se envía! ✓
last_alert_time = now          # se actualiza para el próximo ciclo

'''

ALERT = 5

last_alert_time = 0

#now - last_alert_time , cuantos segundos han pasado desde la ultima alerta
while True:
    now = time.time() #dentro del loop para que este calculando el tiempo 
    diff = now - last_alert_time
    print(f"this is the diff  of time {diff} \n")
    
    if (diff) > ALERT:
        print("Alert")
        last_alert_time = now
    
    
