How to use:

Copy and Paste all the files in this folder into your catkin_ws
Do a "catkin_make"
To launch,

<open new terminal>
roscore
<open new terminal>
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_world.launch
<open new terminal>
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch

(manual bringup)
sol 2:
rosrun map_server map_server ~/user/map.yaml
roslaunch mrc_hw8 amcl_tb0.launch
roslaunch mrc_hw8 amcl_tb1.launch
roslaunch turtlebot3_nps move_base_two.launch

Note:
There is some problems for Tf-Prefix of the robots. I developed
a proper solution for this in the link github below:
https://github.com/nejiko001/turtlebot3_nejiko