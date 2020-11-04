#!/usr/bin/env python

import serial
from datetime import datetime
import time
import logging
import logging.handlers
import requests

# configure syslog logging
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Starting script..")

#Connect to the serial port

#enter your device file
arddev = '/dev/ttyACM0'
baud = 9600

#setup - if a Serial object can't be created, a SerialException will be raised.
while True:
    try:
        ser = serial.Serial(arddev, baud)
        logger.info('Serial port opened successfully')

        #break out of while loop when connection is made
        break
    except serial.SerialException:
        logger.warning("Serial port open FAILED")
        print ('waiting for device ' + arddev + ' to be available')
        time.sleep(3)

def serial_read():
    
    #read lines from serial device

    logger.debug("Flushing serial I/O")
    ser.flushInput() #clear input serial buffer
    ser.flushOutput() #clear output serial buffer
    while True: # keep reading serial port and write to file till the end of time
        logger.debug("Waiting for serial data ...")
        #print("\nWaiting for serial data ...")
        data = ser.readline()
        logger.debug(data)
        data = data.decode("utf-8")
        logger.info("Data received via serial")

        #post data
        if data[0]=='s': # check if data is not empty and entire string is being sent (first value is always "i", which is node ID)
            datestamp = time.time()
            final_data = parse(data)
            final_data["timestamp"] = datestamp
            print(final_data)
            post(final_data)
        else:
            logger.warning("Incomplete data packet received")

# Parse the data into a dictioary for later usage
def parse(data):
    logger.debug("parsing Data")
    data_parse = {}
    #for el in data.strip().split(';'): #for each element after split for a list, but actually a dictionary is better ;)
    #    data_parse.append(el.strip())
    for el in data.strip().split(';'):
        k,v = el.split(':')
        k = k.strip()
        v = v.strip()
        data_parse[k] = v if v else "missing"
    
    logger.debug("Data parsed into dictionary")
    return data_parse

# Post the data on the to the django server applicatio
def post(data_post):
    
    logger.debug('posting data on django server API')
    url = 'http://127.0.0.1:8000/serializer/api/sensors/'
    result = requests.post(url, data=data_post)
    if result.status_code == requests.codes.ok:
        logger.debug("POST request successful")
    else:
        logger.warning("POST error")

#RUN
serial_read()






