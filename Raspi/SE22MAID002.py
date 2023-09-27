
import Adafruit_DHT
import time
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAvcYdKnQ51KOgtOrJkadaXhWRR8HfSVGs",
    "authDomain": "shiv-raspi.firebaseapp.com",
    "databaseURL": "https://shiv-raspi-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "shiv-raspi.appspot.com"}
fireClient = pyrebase.initialize_app(firebaseConfig)
rltd = fireClient.database()
dht = Adafruit_DHT.DHT11
gpio = 23
while True:
    humi, temp = Adafruit_DHT.read_retry(dht, gpio)
    if humi is not None and temp is not None:
        print(f'Temperature : {temp} C  Humidity :{humi} %')
        sensorData = {"Temperature" : temp, "Humidity" : humi}
        rltd.child("Sensor_Data").push(sensorData)
        rltd.update(sensorData)
        print("Updated Firebase Real-Time Database")
    else:
        print('Failed, Trying Again')
    time.sleep(1)
