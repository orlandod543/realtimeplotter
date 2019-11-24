import sys
import argparse #parse arguments to the function

#function that reads the parsed arguments to the functions
def argparser(): 
    try:
        #define all the arguments to parse
        parser = argparse.ArgumentParser()
        parser.add_argument("file", type = str, help="input file to read data")
        parser.add_argument("vars", type = str, nargs='+', help="variables to plot")
        parser.add_argument('-r', dest = 'refreshrate', type = float, default = 1, help="Refresh rate (secs)")
        parser.add_argument("-w", dest = 'window', type = int, default = 1000, help="Size of figure window in data points")
        parser.add_argument("-p", dest = 'print',action='store_true', default = False, help="Print data on command line")
        parser.add_argument("-x", dest = 'xaxis', type = str, default = "time", help = "Variable to plot in the x-axis. Default 'time'")
        parser.add_argument('-v', '--verbose', action = 'store_true', help = "Increase output verbosity")
        parser.add_argument('-y', dest = 'ylabel', type = str, default = None, help = "Label the Y axis" )
        #parse the variables to the function
        args = parser.parse_args()
        return args
    except AttributeError:
        e = sys.exc_info()[0]
        print (e)
        return None
