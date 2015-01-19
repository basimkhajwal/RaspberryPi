from utils.ReadResistance import *
import time

#Constants
FILE_TO_LOG = "output/lightReadings.txt"
LOG_TIMEOUT = 60 * 5
NUMBER_OF_TESTS = 10
TEST_TIMEOUT = 0.1
PIN = 18

#Run if not being loaded as a module
if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	
	logFile = open(FILE_TO_LOG, 'a')
	
	print "Starting to log..."
	
	try:
		
		while True:
			resultTotal = 0
			
			for i in range(NUMBER_OF_TESTS):
				resultTotal += readResistance(PIN)
				time.sleep(TEST_TIMEOUT)
				
			averageResult = resultTotal / NUMBER_OF_TESTS
			
			timeStr = time.strftime("%D %H:%M", time.localtime(int(time.time())))
			logStr = timeStr + "\t" + str(averageResult) + "\n"
			
			print logStr
			
			logFile.write(logStr)
			logFile.flush()
			
			time.sleep(LOG_TIMEOUT)
		
	except KeyboardInterrupt:
		
		print "\nCleaning up...'\n"
		
		GPIO.cleanup()
		logFile.close()
	
	
	