# Milestone-2
write software that plans a trajectory for the end-effector of the youBot mobile manipulator.
This repository is part of the Robotic Manipulation course from Northwestern.
It is the part 1(Milestone 2: Reference Trajectory Generation) from the final project [link](http://hades.mech.northwestern.edu/index.php/Mobile_Manipulation_Capstone).


# Goal
1. From home configuration find a trajectory path that will place the end effector to grab a box.
2. Pick the box and place it somewhere else.
3. save the trajectory path as csv file.

# Run code
To execute the code run `<python main.py>`

# Implementation
1. main.py starts everything we need.
2. states.py has each state(configuration) that the end effector has to go in order to complete the path.
3. functions.py contains all the necessary functions we implement such as creating rotation matrix, save csv files.




# Extra packages
1. we are using the library modern robotics for the trajectory.
2. Coppelia Simulator to play the csv file.


# Coppelia Simulator Output
![](https://github.com/jimas95/Milestone-2/blob/main/gif/coppelisSim_trajectory.gif)