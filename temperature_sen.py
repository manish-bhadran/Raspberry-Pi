import sys
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin =4
humidity, temperature= Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print("Temperature: ", temperature, "*C")
    print("Humidity: ", humidity, "%")
   
else:
    print("Failed to get reading.")
    sys.exit(1)
