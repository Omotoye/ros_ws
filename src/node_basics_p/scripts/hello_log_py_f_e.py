#!/usr/bin/python3
import rospy

# Initializing the node and giving it a name
rospy.init_node("hello_log_py_n")

# Creating an instance of the Rate() class as an object loop_hz
loop_hz = rospy.Rate(10)

# Infinite loop using the ros style
# This loop takes in a SIGTSTP signal to set the while loop to False
while not rospy.is_shutdown():
    rospy.loginfo('Hello from Python')
    loop_hz.sleep()

