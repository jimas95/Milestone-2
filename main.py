import functions
import math
import numpy as np
import states

"""
this is the main file for executing the trajectory for a series of states
we get the series of states from file states.py
find path from file functions.py --> generateTraj(states.states)
save the trajectory as csv file  from file functions.py --> csv(path)
"""

def main():

    print("Hello world!")
    #create trajectory
    path = functions.generateTraj(states.states)
    #save trajectory as cvs file
    functions.csv(path)



if __name__ == "__main__":
    main()