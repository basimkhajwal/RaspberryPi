import RPi.GPIO as GPIO, time, os

#Constants
NUM_TESTS = 3
NUM_TESTS_PER_VALUE = 5

def readResistance(RCpin):
    ''' 
        Read the resistance with the pin stated in the input, returns an integer with the number
        of clock cycles passed
    '''
    
    #Discharge the pins and capacitor
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
    
    #Get the time from before
    reading = 0 #Set the initial reading to 0
    
    #Start the count down
    GPIO.setup(RCpin, GPIO.IN)
    
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    
    #Return the results
    return reading

#Test code if the file is actually being run
if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        
        #Get the user input
        pin = input("Which GPIO pin are you using? ")
        capValue = input("How many microFarads is the capacitor? ")

        #Input was in microFarads so divide accordingly
        capValue /= 1000000.0
        
        print "\nWe will first run some resistor tests to have a more accurate reading. Connect a resistor with a known resistance to the circuit and follow the instructions"
        print "Test atleast one value but then just press enter to quit at any time"

        #Set the initial ratio, needs to be changed
        ratio = 0
        num = 0
        
        for test in range(NUM_TESTS):
            try:
                resValue = input("\nTest " + str(test + 1) + ": resistor size (ohms): ")
	    except Exception:
                if ratio == 0:
                    continue
    		break
            
	    values = []
            average = 0.0
            
            print "Calculating..."
            
            #Read some values
            for i in range(NUM_TESTS_PER_VALUE):
            	values.append(readResistance(pin))           
            
            	average += values[i]
            	
            	time.sleep(0.1)
            
            #Take the average
            average /= NUM_TESTS_PER_VALUE
            
            print "Average No. of Clock Cycles: %f" % (average)

            #This is the time it should take for the
            #capacitor to charge in an RC circuit
            exactTime = resValue * capValue

            #Add the ratio of the time found and the clock cycles
            ratio += (exactTime / average)
            num += 1

        #Take the average of the ratios
        ratio /= num
    
        print "\nTests completed\n"        

        #Get the sleep time limit
        timeLimit = min(max(0.2, input("How often to update resistance(seconds and 0.2 < s < 5): ")), 5)

        #Loop while user is running                           
        while True:
            #Get the number of cycles
            numCycles = readResistance(pin)

            #Predict the resistance in ohms
            resistance = (numCycles * ratio) / capValue

            #Print the results
            print "Number Of Clock Cycles: %d" % (numCycles)
            print "Predicted Resistance: %f Ohms\n" % (resistance)
            
            #Sleep for the desired time                                    
            time.sleep(timeLimit)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
