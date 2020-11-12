import functions
import math
import numpy as np
import states


def main():

    print("Hello")
    #create trajectory
    path = functions.generateTraj(states.states)
    #save trajectory as cvs file
    # trajectoryList = [] 
    # functions.convertToCsvForm(trajectoryList,trajectory,0)
    functions.csv(path)



if __name__ == "__main__":
    main()