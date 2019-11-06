import RPi.GPIO as gp
import time
gp.setwarnings(False)
gp.setmode(gp.BOARD)
ldr_thrhold=100
LIGHT_PIN = 7
LDR_PIN = 13

gp.setup(LIGHT_PIN, gp.OUT)
gp.output(LIGHT_PIN, False)
    

def read_LDR(LDR_PIN):
    gp.setup(LDR_PIN, gp.OUT)
    gp.output(LDR_PIN, False)
    reading =0
    time.sleep(0.1)
    gp.setup(LDR_PIN, gp.IN)
    while(gp.input(LDR_PIN) == False):
        reading +=1
        if reading > ldr_thrhold:
            break
    return reading

try:
    while True:
        r = read_LDR(LDR_PIN)
        print(r)
        time.sleep(0.1)
    
        
        if r > ldr_thrhold:
            gp.setup(LIGHT_PIN, gp.OUT)
            gp.output(LIGHT_PIN, True)
            
        else:
            gp.setup(LIGHT_PIN, gp.OUT)
            gp.output(LIGHT_PIN, False)
           
    time.sleep(0.5)
            
        
except KeyboardInterrupt:
    gp.cleanup()
