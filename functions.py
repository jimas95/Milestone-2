import modern_robotics as mr
import math
import numpy as np



def test():
    print("Test")


def csv(data):
    """
    save data as csv file
    csv form r11,r12,r13,r21,r22,r23,r31,r32,r33,px,py,pz,gripper_state
    """

    # Open a file for output
    # Overwrite
    f = open("trajectory.csv", "w") 
    
    for row in data:
        output = ""
        for i in range(len(row)):
            output += str(row[i]) 
            if(i!=len(row)-1):
                output +=", "
        
        output += " \n"
        f.write(output)
        
    # close file
    f.close()

def convertToCsvForm(myList,data,gripper_state):
    for row in data:
        r11 = row[0][0]
        r12 = row[0][1]
        r13 = row[0][2]
        r21 = row[1][0]
        r22 = row[1][1]
        r23 = row[1][2]
        r31 = row[2][0]
        r32 = row[2][1]
        r33 = row[2][2]
        px  = row[0][3]
        py  = row[1][3]
        pz  = row[2][3]
        myList.append([r11,r12,r13,r21,r22,r23,r31,r32,r33,px,py,pz,gripper_state])


def generateTraj(states):
    method = 5
    path = []
    for state in states:
        Xstart  = state[0]
        Xend    = state[1]
        Tf      = state[2]
        N       = state[3]
        gripper = state[4]
        trajectory = mr.CartesianTrajectory(Xstart,Xend,Tf,N,method)    
        convertToCsvForm(path,trajectory,gripper)

    return path


def rot_y(angle,x,y,z):
    mat = np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , x  ],
                        [0                  , 1     , 0                 , y  ],
                        [-math.sin(angle)   , 0     , math.cos(angle)   , z  ],
                        [0                  , 0     , 0                 , 1  ]])

    return mat

def rot_z(angle,x,y,z):
    mat =np.array( [[math.cos(angle)    , -math.sin(angle)  , 0   , x  ],
                    [math.sin(angle)    , math.cos(angle)   , 0   , y  ],
                    [0                  , 0                 , 1   , z  ],
                    [0                  , 0                 , 0   , 1  ]])

    return mat



def trasl(x,y,z):

    mat = np.array( [[1, 0, 0,x ],
                    [0, 1, 0, y ],
                    [0, 0, 1, z ],
                    [0, 0, 0, 1  ]])

    return mat


