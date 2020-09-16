# Turtlebot3_shm
For multiple Turtlebot3 Navigation + ORCA algorithm for local pathing

**Requirement**


- Ubuntu 16.04
- ROS Kinetic Kame
- Pre-installed catkin_Ws

`note: please install the following item before proceding`

**About this project**


This repository is dedicated for the developement of Robotic Navigation, via turtlebot as the model.
For the navigation stack, Global pathing used A* algorithm and the Local pathing used ORCA.

**Installation**


Just do the "catkin_make" in your catkin_ws/src file.

`cd catkin_ws/src`

`git clone https://github.com/syahmi001/turtlebot3_shm.git`

`cd ..`

`catkin_make`

**Running the code**


Follow these commands.

- new terminal

`roscore`

- new terminal

`export TURTLEBOT3_MODEL=burger`


`roslaunch turtlebot3_gazebo turtlebot3_world_multi.launch`

- new terminal

`export TURTLEBOT3_MODEL=burger`


`roslaunch turtlebot3_navigation turtlebot3_navigation_multi.launch`

**Outcome**


![Optional Text](../master/figures/s1.gif)




**Disclaimer**

- Some of the codes in here are not owned by me. They belongs to the respected people.
- This project is still under improvement and debugging. The release version will be released soon.
