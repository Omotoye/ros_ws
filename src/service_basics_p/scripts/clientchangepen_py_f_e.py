#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
import random 
from turtlesim.msg import Pose
from turtlesim.srv import SetPen 

is_turtle_outside = None 
is_turtle_outside_prev = None 
def pose_clbk(pose_message):
	"""
	A function that takes the real-time position of 
	the turtlesim robot and set boundaries with that data
 	for the robot so it doesn't hit the wall
	"""
	global is_turtle_outside
	is_turtle_outside = (pose_message.x<2) or (pose_message.x>8) or \
	(pose_message.y<2) or (pose_message.y>8)

# Initializing the node
rospy.init_node("clientchangepen_py_n")
rospy.wait_for_service("turtle1/set_pen")

# Creating a publisher object
vel_pub_py = rospy.Publisher("turtle1/cmd_vel", Twist,queue_size = 10)

# Creating a subscriber the get the real time location of the robot
pose_sub_py = rospy.Subscriber("turtle1/pose", Pose, pose_clbk, queue_size = 10)

changepen_handle_py =rospy.ServiceProxy("turtle1/set_pen", SetPen)


# Creating an object to set the frequency
loop_rate = rospy.Rate(20)

# Creating an object for the turtle motion
velocity_v = Twist()
velocity_v.linear.x = 1.0
#velocity_v.angular.z = 1.0

while not rospy.is_shutdown():
	#velocity_v.angular.z = random.random()
	if(is_turtle_outside):
		velocity_v.angular.z = 1
	else:
		velocity_v.angular.z = 0
	if(is_turtle_outside_prev == 0 and is_turtle_outside == 1):
		changepen_handle_py(0,0,0,5,False)
	elif(is_turtle_outside_prev == 1 and is_turtle_outside == 0):
		changepen_handle_py(255, 255, 255, 5, False)
	is_turtle_outside_prev = is_turtle_outside
	vel_pub_py.publish(velocity_v)
	loop_rate.sleep()



 