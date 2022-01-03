import random
import math
import time
from os import system, name

# define our clear function 
def clear(): 
   
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    
    # for mac and linux
    else: 
        _ = system('clear') 

def run(loops,s,x,y,high,low,p):

  def PerlinNoise():

    #import random number
    n = random.randint(0,100000000)

    #gets the seed
    random.seed(n)

    #set the sizes
    def WhiteNoise(w,h):
        perlin = [[r for r in range(w)] for i in range(h)]

        for i in range(0,h):
            for j in range(0,w):
                perlin[i][j] = random.randint(0,1)

        return perlin

    #set perlin noise
    perlin = WhiteNoise(x,y)

    #print the perlin noise
    for i in perlin:
        print()
        time.sleep(p)
        for o in i:
            if(o == 0):
                print(low,end='')
            else:
                print(high,end='')


  for i in range(loops):
    PerlinNoise()
    time.sleep(s)
    clear()