from utils.ReadResistance import *
from time import sleep, time
from pprint import pprint
import matplotlib.pyplot as pyplot

#Constants
PIN = 15

#Run if not being loaded as a module
if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	
	raw_input("Put finger on and press enter when ready")
	print "Gathering data..."
	
	
	
	try:
		times = []
		data = []
		start = time()
		
		for i in range(100):
			data.append(readResistance(PIN))
			times.append(time() - start)
		
		print "Plotting data..."
		pyplot.plot(times, data)
		pyplot.savefig("testFinger.png")
		
		print "All done!!"
		
	except KeyboardInterrupt:
		pass
		
	finally:
		print "\nCleaning up...'\n"
		GPIO.cleanup()
	
	
	