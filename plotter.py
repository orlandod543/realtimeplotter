#This is a simple python script that reads a CSV file and plots the variables in real time. 
#Usage: The simplest usage is introducing the file name and the variables to plot. 
#author: Orlando Diaz

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import sys

from parser import argparser

#function that verifies that the input file and variables exist 
def Argschecker(args):
    result = []
    try:
        df = pd.read_csv(args.file)

        #If x axis is defined Check if the x axis column exist. 
        if args.xaxis and (not args.xaxis in df):
            print("Horizontal variable " + args.xaxis + " does not exist")
            sys.exit(0)

        #Check if all the input variables exist in the file 
        #Note: Python does not allow to remove the element of an item within a for loop, so your option is to create a new list with the existing elements
        for var in args.vars: 
            if  var in df:
                result.append(var)
            else:
                print("Variable " + var + " does not exist in the data file.") 
        args.vars= result
        #if no variable is correct   
        if not args.vars:
            if args.verbose:
                print("No valid variables introduced")
            sys.exit(0)

    except FileNotFoundError: 
        print("The file does not exist")
        sys.exit(1)

    #Change refresh rate from seconds to miliseconds
    args.refreshrate = args.refreshrate*1000
    return args

def animate(i):
    #Open the file
    try:
        df = pd.read_csv(args.file)
    except:
        print("The file could not be read.")
        return None
    #if data is bigger than the time window, drop the extra data.
    if(len(df)>args.window):
        df=df.drop(df.index[0:len(df)-args.window])

    #Extract the horizontal axis if exist
    if(args.xaxis):
        x = df[args.xaxis]
    ax1.clear()
    
    #Plot and overlap the variables.
    for column in args.vars:
        y = df[column]
        if (args.print):
            print(y)
        #If there is no x defined only plot the y data
        if(not args.xaxis):
            ax1.plot(y[len(y)-args.window:len(y)])
        else:
            ax1.plot(x[len(x)-args.window:len(x)], y[len(y)-args.window:len(y)])

    plt.xlabel(str(args.xaxis))
    plt.ylabel(args.ylabel)
    plt.legend(args.vars, loc='upper left')

#function that generates the namespace from the input arguments
args = argparser()

#Does the file and variables exist?
args = Argschecker(args)
if args.verbose:
    print("Verbosity turned on")
    print(args)

style.use('fivethirtyeight')

fig = plt.figure(figsize = (12,7))
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate, interval=(args.refreshrate))
plt.show()