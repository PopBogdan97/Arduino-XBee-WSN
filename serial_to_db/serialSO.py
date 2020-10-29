#!/usr/bin/env python

import serial
from datetime import datetime
import time

#enter your device file
arddev = '/dev/ttyACM0'
baud = 9600

#setup - if a Serial object can't be created, a SerialException will be raised.
while True:
    try:
        ser = serial.Serial(arddev, baud)

        #break out of while loop when connection is made
        break
    except serial.SerialException:
        print ('waiting for device ' + arddev + ' to be available')
        time.sleep(3)

#read lines from serial device
count = 0
while count < 5:

    element = ser.readline().decode("utf-8")
    count = count + 1
    datestamp = time.time()
    print ('received the element: ' + element) 
    print (datestamp)

    #cursor.execute('insert into elements(Name) values("%s")'%(element))


#allentries = []
#cursor.execute('SELECT * FROM elements')

#allentries=cursor.fetchall()

#print allentries
