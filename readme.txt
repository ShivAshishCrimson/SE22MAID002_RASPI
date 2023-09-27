PARAM SHIV ASHISH
SE22MAID002
MTECH AI AND DS
INDIVIDUAL ASSSIGNMENT
(ALL IMAGES, CODE FILES AND DOCUMENTATION IN THE GIT REPO)

Here are some key steps that I have done for implementing IoT on a Raspberry Pi

Step 1 Selecting Hardware:
Raspberry Pi Model 3 (I have used the appropriate Raspberry Pi model for my project)
DHT11 (additional sensor to interface with the physical world)
DHT11 is a single wire digital humidity and temperature sensor. 
which provides humidity and temperature values serially with one-wire protocol.

Step 2 Connected the circuit as per circuit diagram (Attached in the repo)
DHT11 Vcc => Raspberry Pi Vcc
DHT11 Gnd => Raspberry Pi Gnd
DHT11 Digital Out => Raspberry Pi GPIO 23 

Step 3 Installing an Operating System.
Install Raspberry Pi OS using Raspberry Pi Imager,  
with the supported OS which is available directly on the official Pi OS website

Step 4 Programming
Install adafruit library using the following command in the terminal.
>> pip install Adafruit-DHT
This library is used to interface with the sensor, which is DHT11 in our case
Install pyrebase library using the following command in the terminal
>> pip install pyrebase
This library is used to connect with the firebase realtime database
I import the required libraries
Initialize our firebase config
(Firebase config is obtained by first creating an firebase application and instantiating a storage bucket)
Connect to firebase real time database using pyrebase library as shown in the code
Instantiate a  while loop which reads the sensor data continuously in a loop
Lastly update this sensor data in firebase using the defined client connection in above section

Step 5 Sensors and Data Collection:
Run the python code on the Raspberry pi
Firebase Real Time Database is updated in the following way, here's a screenshot of the real time database which has updated with the latest values which where measured using the raspberry pi setup

ALL IMAGES AND CODE FILES IN THE GIT REPO