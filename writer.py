
#Simple test script that simulates the datalogger, it creates a file called data with three columns: 
# time, cos(x), sin(x), cos(x)+sin(x).
# To test the plotter. run this script and then run the plotter.
import numpy as np
import math
import time
import os
import sys

#if there is no file, create header
if not os.path.isfile('data'): 
    try: 
        fp=open("data",'a')
        fp.write("time,sin(x),cos(x),sin+cos\n")
        fp.close()
    except:
        sys.exit(1)

fp=open("data",'a')
    
i=0
samplerate = 0.1 #sample reate in sec
t = 0

while (True):
    i=i+math.pi/100
    if(i>2*math.pi):
        i+0

    temp=math.cos(i)
    temp2=math.sin(i)
    temp3=temp+temp2
    t = t + samplerate
    try:
        fp=open("data",'a')
        fp.write(str(t))
        fp.write(',')
        fp.write(str(temp))
        fp.write(',')
        fp.write(str(temp2))       
        fp.write(',')
        fp.write(str(temp3))       
        fp.write('\n')
        fp.close()
    except:
        print("File can't be opened")
        print(str(temp))
    time.sleep(samplerate)