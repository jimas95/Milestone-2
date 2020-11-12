import math
import numpy as np


# go near the object
start = np.array( [[1, 0, 0, 0  ],
                    [0, 1, 0, 0  ],
                    [0, 0, 1, 0.5],
                    [0, 0, 0, 1  ]])


angle = 3*math.pi/4
end = np.array( [  [math.cos(angle)     , 0     , math.sin(angle)   , 0.85  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.15  ],
                    [0                  , 0     , 0                 , 1     ]])

                    
Tf = 5
N = 100
gripper = 0
state1 = [start,end,Tf,N,gripper]


# go at grasping position
angle = 3*math.pi/4
start =np.array([  [math.cos(angle)     , 0     , math.sin(angle)   , 0.85  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.15  ],
                    [0                  , 0     , 0                 , 1     ]])


angle = 3*math.pi/4
end = np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.0   ],
                    [0                  , 0     , 0                 , 1     ]])

                    
Tf = 5
N = 100
gripper = 0
state2 = [start,end,Tf,N,gripper]



#pick the object
angle = 3*math.pi/4
start=np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.0   ],
                    [0                  , 0     , 0                 , 1     ]])


angle = 3*math.pi/4
end = np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.0   ],
                    [0                  , 0     , 0                 , 1     ]])

                    
Tf = 5
N = 100
gripper = 1
state3 = [start,end,Tf,N,gripper]


#go up
angle = 3*math.pi/4
start=np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.0   ],
                    [0                  , 0     , 0                 , 1     ]])


angle = 3*math.pi/4
end = np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.2   ],
                    [0                  , 0     , 0                 , 1     ]])

                    
Tf = 1
N = 100
gripper = 1
state4 = [start,end,Tf,N,gripper]


#go to dropping location
# angle = 3*math.pi/4
# start=np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
#                     [0                  , 1     , 0                 , 0     ],
#                     [-math.sin(angle)   , 0     , math.cos(angle)   , 0.2   ],
#                     [0                  , 0     , 0                 , 1     ]])


# angle = math.pi/2
# end  =np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
#                     [0                  , 1     , 0                 , 0     ],
#                     [-math.sin(angle)   , 0     , math.cos(angle)   , 0.2   ],
#                     [0                  , 0     , 0                 , 1     ]])
                    
# Tf = 1
# N = 100
# gripper = 1
# state5 = [start,end,Tf,N,gripper]




#go to dropping location
angle = 3*math.pi/4
start=np.array( [   [math.cos(angle)    , 0     , math.sin(angle)   , 1.00  ],
                    [0                  , 1     , 0                 , 0     ],
                    [-math.sin(angle)   , 0     , math.cos(angle)   , 0.2   ],
                    [0                  , 0     , 0                 , 1     ]])



angle = -math.pi/2
end2 =np.array( [   [math.cos(angle)    , -math.sin(angle)  , 0   , 0  ],
                    [math.sin(angle)    , math.cos(angle)   , 0   , 0  ],
                    [0                  , 0                 , 1   , 0  ],
                    [0                  , 0                 , 0   , 1  ]])


end = np.matmul(end2,start)
Tf = 1
N = 100
gripper = 1
state5 = [start,end,Tf,N,gripper]



#go down
angle = 3*math.pi/4
start= end


angle = -math.pi/2
end2    = np.array([[1, 0, 0, 0   ],
                    [0, 1, 0, 0   ],
                    [0, 0, 1, -0.2],
                    [0, 0, 0, 1]])


Tf = 1
N = 100
gripper = 1
end = np.matmul(end2,start)
state6 = [start,end,Tf,N,gripper]


states = [state1,state2,state3,state4,state5,state6]
# states = [state5,state6]