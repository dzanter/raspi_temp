#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
import time
from itertools import count
import Adafruit_DHT
import datetime
from time import sleep
sys.path.append(r'/home/pi/pysrc')
#import pydevd
import smtplib
#import dht11
import sendemail

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
PIR_PIN=22
GPIO.setup(PIR_PIN, GPIO.IN);
motion = False

def MOTION(PIR_PIN):
    print "Motion Detected!";
    global motion;
    motion = True;

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)
tempf = (temperature * 9) / 5 + 32;
lastf = tempf;
if humidity is not None:
    print("Temperature: %d C" % tempf)
    print("Humidity: %d %%" % humidity)
else:
    print("Error Can't read DHT22: %d" % result.error_code)
    sm.send('hi there')
    sys.exit(1)
    
day = 0    
risingt = 0;
    
while True :    
    with open("tvroomtemp.txt", "a") as myfile:
        secs = time.time()    
        day2 = secs % (60*60*12)    
        if day2 > day :
            newday = True
            day=day2;
            sentEmail = False
            print 'new day'
            #do stuff here for every new day
            
        
        
        i = datetime.datetime.now()
           
        sleep(30);
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)
        tempf = (temperature * 9) / 5 + 32;

        #check if increasing or decreasing
        if (tempf > lastf) :
            risingt = risingt + 1;
        if (tempf < lastf) :
            risingt = risingt - 1;
        if (risingt > 1) :
            risingt = 1;
        if (risingt < -1) :
            risingt = -1;
        lastf = tempf;                        
           
        # example of turning on LEDS if the temp is
        #  going up or going down.
        #if (risingt == 1) :
        #   GPIO.output(16, True);
        #   GPIO.output(26, False);        
        #if (risingt == -1) :
        #   GPIO.output(26, True);
        #   GPIO.output(16, False);           
        
        
        if (humidity is not None) :
            myfile.write(i.strftime('%Y/%m/%d %H:%M:%S,'))            
            myfile.write(str(tempf));
            myfile.write(',')
            myfile.write(str(humidity));            
            if (motion == True) :
                myfile.write(',1')
            else :
                myfile.write(',0')
            myfile.write('\n');
            myfile.flush()
        #else :
            #send email     
            #if (sentEmail == False) :  # only send one a day 
             #   sm.send('Unable to read DHT11, ')
            #sentEmail = True        
            #sleep(60*20) # sleep + 20
        
        motion = False
        sleep(60 * 10) # sleep 10 minutes
    
