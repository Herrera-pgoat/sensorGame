import time
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from threading import Thread

class sensorThread(Thread):
    def __init__(self,trigPin,echoPin):
        Thread.__init__(self)
        self.distance = 0
        self.echoPin = echoPin
        self.trigPin = trigPin
        self.running = True
    def returnDistance (self):
        return self.distance
    
    def stopRunning (self):
        self.running = False
    
    def run(self):
        GPIO.setmode(GPIO.BOARD)                     #Set GPIO pin numbering 

        TRIG = self.trigPin                               #Associate pin 23 to TRIG
        ECHO = self.echoPin                                  #Associate pin 24 to ECHO

        print ("Distance measurement in progress" + str(TRIG))

        GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
        GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
        while self.running:
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
          print ("Waitng For Sensor To Settle")
          time.sleep(.04)                            #Delay of 2 seconds
            #.033333 is about 30fps
          GPIO.output(TRIG, True)                  #Set TRIG as HIGH
          time.sleep(0.00001)                      #Delay of 0.00001 seconds
          GPIO.output(TRIG, False)                 #Set TRIG as LOW

          oldTime = time.time()
          #I should restart if I meet some certain condition like a certain amount of time has passed 
          while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse
            #If the sensor flips out we will enter this if statement and basically restart it
            if pulse_start - oldTime > .2:
                print ("ERROR OCCURED")
                print("********************************************")
                print("ERROR OCCURED RESTARTING SENSOR ERROR ERROR ERROR")
                GPIO.output(TRIG, True)                  #Set TRIG as HIGH
                time.sleep(0.0001)                      #Delay of 0.00001 seconds
                GPIO.output(TRIG, False)  
                oldTime = time.time()

          while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 

          pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

          distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
          distance = round(distance, 3)            #Round to three decimal points
          self.distance = distance
          if distance > 2 and distance < 400:      #Check whether the distance is within range
            print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
