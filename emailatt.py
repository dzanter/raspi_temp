#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
import time
from itertools import count
import datetime
from time import sleep
from subprocess import call
sys.path.append(r'/home/pi/pysrc')
import sendemail

call("/home/pi/raspproj/pljfile.sh");
sm = sendemail.sendemail();
with open("/tmp/output.jpg", "r") as myfile:    
    sm.sendatt("Room Temp", myfile.read());
