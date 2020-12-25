#!/usr/bin/python3
import rospy 
from std_msgs.msg import String

# Initializing the node with a name 
rospy.init_node("pub_py_n")

# Creating a publisher object 
pub_handle_py = rospy.Publisher("my_first_t", String, queue_size=10)

# Creating a String message object
hello_v = String()
hello_v.data = "Hello from Python"

# Object to set the frequency
loop_hz = rospy.Rate(5)

while not rospy.is_shutdown():
    pub_handle_py.publish(hello_v)
    rospy.loginfo(hello_v.data)
    loop_hz.sleep()

