#!/usr/bin/env python
import copy
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Point32
from sensor_msgs.msg import PointCloud


def rfid_callback(data):
    global pub
    global last_point
    rospy.loginfo(rospy.get_caller_id() + " rfid <%s>", data.data)
    pc.points.append(copy.deepcopy(last_point))
    pub.publish(pc)
    
def amcl_callback(data):
    global last_point
    rospy.loginfo(rospy.get_caller_id() + " amcl_pose: %f %f",
                  data.pose.pose.position.x,data.pose.pose.position.y)

    pc.header.seq += 1
    pc.header.stamp = data.header.stamp
    pc.header.frame_id = data.header.frame_id
    '''
    last_point.point.x = data.pose.pose.position.x
    last_point.point.y = data.pose.pose.position.y
    '''
    last_point.x = data.pose.pose.position.x
    last_point.y = data.pose.pose.position.y
    
def listener():
    global pub
    global last_point
    global pc
    last_point = Point32()
    pc = PointCloud()
    #pub = rospy.Publisher('rfid_pose',PointStamped,queue_size=10)
    pub = rospy.Publisher('rfid_pointcloud',PointCloud,queue_size=10)
    
    rospy.init_node('rfid_rviz', anonymous=True)

    rospy.Subscriber("rfid",String, rfid_callback)
    rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped, amcl_callback)
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
