import RPi.GPIO as gp
import time
gp.setwarnings(False)
gp.setmode(gp.BOARD)
ldr_thrhold=100
LIGHT_PIN = 7
PIR_PIN = 11
LDR_PIN = 13

gp.setup(LIGHT_PIN, gp.OUT)
gp.output(LIGHT_PIN, False)

def read_PIR(PIR_PIN):
    gp.setup(PIR_PIN, gp.OUT)
    gp.output(PIR_PIN, False)
    time.sleep(0.1)
    gp.setup(PIR_PIN, gp.IN)
    i = gp.input(PIR_PIN)
    if i == 1:
        gp.setup(LIGHT_PIN, gp.OUT)
        gp.output(LIGHT_PIN, True)
        print("Object detected")
    else:
        gp.setup(LIGHT_PIN, gp.OUT)
        gp.output(LIGHT_PIN, False)
        print("Object not detected")
    
    

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
        
        time.sleep(0.1)
    
        
        if r > ldr_thrhold:
            read_PIR(PIR_PIN)
            
        else:
            gp.setup(LIGHT_PIN, gp.OUT)
            gp.output(LIGHT_PIN, False)
            print("Night")
    time.sleep(0.5)
            
        
except KeyboardInterrupt:
    gp.cleanup()
