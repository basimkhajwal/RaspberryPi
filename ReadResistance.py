import RPi.GPIO as GPIO, time, os

#Constants
NUM_TESTS = 3

def readResistance(RCpin):
    ''' 
        Read the resistance with the pin stated in the input, returns an array with the number
        of clock cycles passed and the number of seconds passed
    '''
    
    #Discharge the pins and capacitor
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
    
    #Get the time from before
    before = time.time()
    reading = 0 #Set the initial reading to 0
    
    #Start the count down
    GPIO.setup(RCpin, GPIO.IN)
    
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    
    #Return the results
    return [reading, (time.time() - before)]

#Test code if the file is actually being run
if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        
        #Get the user input
        pin = input("Which GPIO pin are you using? ")
        capValue = input("How many microFarads is the capacitor? ")
        
        print "\nWe will first run some resistor tests to have a more accurate reading. Connect a resistor with a known resistance to the circuit and follow the instructions\n"
        
        for test in range(NUM_TESTS):
            resValue = input("Test " + str(i + 1) + "How many ohms is the resistor that you are using? ")
            value = readResistance(pin)
            
            print "Time taken: %ds\nClock cycles: %d" % (value[1], value[0])
            
            
        while True:
            print RCtime()   # Read RC timing using pin #18
            time.sleep(0.5)
    except KeyboardInterupt:
        GPIO.cleanup()