import RPi.GPIO as gp
import time
gp.setwarnings(False)
gp.setmode(gp.BOARD)
PIR_pin= 22
LIGHT_pin= 11
gp.setup(LIGHT_pin,gp.OUT)
gp.output(LIGHT_pin, False)
 
def read_PIR(PIR_pin):
    gp.setup(PIR_pin,gp.OUT)
    gp.output(PIR_pin, False)
    time.sleep(0.1)
    gp.setup(PIR_pin, gp.IN)
    var1=gp.input(PIR_pin)
    
    if var1 == 1:
        gp.output(LIGHT_pin, True)
        print(var1)
    else:
        
        gp.output(LIGHT_pin, False)
        print(var1)
        
try:
    while True:
        read_PIR(PIR_pin)
        time.sleep(0.2)
        
except KeyboardInterrupt:
    gp.cleanup()
        

