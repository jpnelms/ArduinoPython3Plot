#Plotting Serial Feed from an Arduino

import serial #import Serial Library
import matplotlib.pyplot as plt
from drawnow import *
arduinoSerialData = serial.Serial('com3',9600)
plt.ion() #Tells matplotlive we want to plot live data
cnt=0
cntlim=50 #Number of points to be displayed on plot

time = [] #Time array for plot
reading = [] #Reading array for plot


def makeFig(): #Create function that makes desired plot
    plt.plot(time,reading,'ro-')

#Reading and Saving Data from Serial Port
with open("Output.txt","w") as out_file:
    while True:
        while (arduinoSerialData.inWaiting()==0):#Waiting on Data
            pass #Do nothing
        arduinodata = arduinoSerialData.readline().decode()
        splitdata_str=arduinodata.split(',') #Splits String
        reading.append(float(splitdata_str[0])) #Reading is 1st position
        time.append(float(splitdata_str[1])) #Time is 2nd position
        out_file.write(arduinodata) #Writes data to file
        out_file.flush() #Saves written data from buffer
        drawnow(makeFig) #Calls live graph
        cnt=cnt+1
        if (cnt > cntlim): #Removes first points of graph data for scrolling
            time.pop(0)
            reading.pop(0)
            
