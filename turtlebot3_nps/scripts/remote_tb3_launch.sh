ROS_MASTER_URI=http://192.168.11.110:11311 ROS_HOSTNAME=192.168.11.118 ROS_NAMESPACE=tb3_1 roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:="tb3_1" set_lidar_frame_id:="tb3_1/base_scan"

ROS_MASTER_URI=http://192.168.11.110:11311 ROS_HOSTNAME=192.168.11.113 ROS_NAMESPACE=tb3_0 roslaunch turtlebot3_bringup turtlebot3_robot.launch multi_robot_name:="tb3_0" set_lidar_frame_id:="tb3_0/base_scan"


ROS_MASTER_URI=http://192.168.11.110:11311 ROS_HOSTNAME=192.168.11.118 roslaunch turtlebot3_bringup turtlebot3_robot.launch


export ROS_MASTER_URI=http://192.168.11.110:11311 && roslaunch thingmagic_rfid reader.launch port:=/dev/ttyACM1
