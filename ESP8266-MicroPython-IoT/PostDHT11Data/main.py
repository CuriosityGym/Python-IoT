# Import libraries and settings


import urequests
import machine
import time
import dht
import network


DHT11Pin=2

APIKEY="JZMYMXQKJ7JLEASK"
delayTime=16

# Functions

def measure():
    d = dht.DHT11(machine.Pin(DHT11Pin))
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print('Temp: ', temp)  # eg. 23.6 (°C)
    print('Humidity: ', hum)  # eg. 41.3 (% RH)
    return temp, hum





def goToSleep():
    # put the device to sleep for 60 seconds
    time.sleep(delayTime)

	
def sendData(temp,hum):
    URL="https://api.thingspeak.com/update?"
    URL=URL+"api_key="+APIKEY
    URL=URL+"&field1="+str(temp)
    URL=URL+"&field2="+str(hum)
    response = urequests.get(URL)
    response.close()
    print('Posted to Thingspeak')
	

	
	
	
# Start of actual program

while True:    
    (temp, hum) = measure()
    sendData(temp,hum)
    goToSleep()
