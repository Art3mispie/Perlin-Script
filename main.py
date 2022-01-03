from noise import *


#def run(loops,s,x,y,high,low,p):def run(loops,s,x,y):

input_loops = int(input("How many patterns to show?"))
input_s = int(input("How many seconds between each pattern?"))
input_x = int(input("How many units across?"))
input_y = int(input("How many units up?"))
input_high = input("What symbol to show high spaces?")
input_low = input("What symbol to show low spaces?")
input_p = int(input("How many seconds between each line?"))

clear()
run(input_loops,input_s,input_x,input_y,input_high,input_low,input_p)
clear()
print("Done")
