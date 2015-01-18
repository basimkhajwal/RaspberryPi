import RPi.GPIO as g

SEND_PIN = 4
TIME_OUT = 10000

def setupCapacitorSense(pin):
	global SEND_PIN
	
	SEND_PIN = pin
	
	g.setmode(g.BCM)

def discharge(pinNum):
    g.setup(pinNum, g.OUT)
    g.output(pinNum, g.LOW)


def capacitorSense(pinNum):
    discharge(SEND_PIN)
    discharge(pinNum)
    
    g.setup(pinNum, g.IN)
    
    g.output(SEND_PIN, g.HIGH)
    
    total = 0
    
    while g.input(pinNum) == g.LOW and total < TIME_OUT:
        total += 1
        
    return total
    