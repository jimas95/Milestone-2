import math
import numpy as np
import functions
"""
This file contains a list of states for our trajectory.
states = [state1,state2,...,stateN]
example of state : state = [start,end,Tf,N,gripper]
    starting position of eef 4x4 matrix
    end      position of eef 4x4 matrix
    Tf       total time of trajectory
    N        total number of points for the trajectory
    gripper  on/off 0/1
"""


Tf = 5
N = 100
gripper = 0
angle = 3*math.pi/4

# go near the object
start = functions.trasl(0,0,0.5)
end = functions.rot_y(angle,0.85,0,0.15)
state1 = [start,end,Tf,N,gripper]


# go at grasping position
start = end
end = functions.rot_y(angle,1,0,0)
state2 = [start,end,Tf,N,gripper]


#pick the object
start=end
end = functions.rot_y(angle,1,0,0)
gripper = 1
state3 = [start,end,Tf,N,gripper]


#go up
start=end
end = functions.rot_y(angle,1,0,0.2)               
Tf = 1
gripper = 1
state4 = [start,end,Tf,N,gripper]


#go to dropping location
start=end
angle = -math.pi/2
rotation = functions.rot_z(angle,0,0,0)
end = np.matmul(rotation,start)
Tf = 5
gripper = 1
state5 = [start,end,Tf,N,gripper]


#go down
angle = 3*math.pi/4
start= end
angle = -math.pi/2
rotation    = functions.trasl(0,0,-0.2)
Tf = 1
gripper = 1
end = np.matmul(rotation,start)
state6 = [start,end,Tf,N,gripper]

#open gripper
start= end
Tf = 1
gripper = 0
state7 = [start,end,Tf,N,gripper]

#go up
start = end
rotation    = functions.trasl(0,0,0.2)
end = np.matmul(rotation,start)
state8 = [start,end,Tf,N,gripper]

# go to home position
tf = 5
start = end
end = functions.trasl(0,0,0.5)
state9 = [start,end,Tf,N,gripper]

# add all states to one list
states = [state1,state2,state3,state4,state5,state6,state7,state8,state9]
