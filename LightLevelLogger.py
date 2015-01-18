from utils.ReadResistance import *
import time

#Constants
FILE_TO_LOG = "output/lightReadings.txt"
LOG_TIMEOUT = 60 * 5
NUMBER_OF_TESTS = 20
TEST_TIMEOUT = 1
PIN = 18

#Run if not being loaded as a module
if __name == "__main__":
	GPIO.setmode(GPIO.BCM)
	
	logFile = open(FILE_TO_LOG, 'a')
	
	print "Starting to log"
	
	try:
		
		while True:
			resultTotal = 0
			
			for i in range(NUMBER_OF_TESTS):
				resultTotal += readResistance(PIN)
				time.sleep(TEST_TIMEOUT)
				
			averageResult = resultTotal / NUMBER_OF_TESTS
			
			timeStr = time.strftime("%D %H:%M", time.time())
			logStr = timeStr + "\t" + str(averageResult) + "\n"
			
			print logStr
			
			logFile.write(logStr)
			
			time.sleep(LOG_TIMEOUT)
		
	catch KeyboardInterrupt:
		
		print "Cleaning up...'\n"
		GPIO.cleanup()
	
	
	