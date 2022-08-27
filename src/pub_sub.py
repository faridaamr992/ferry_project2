#!/bin/env python3
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import rospy
rospy.init_node("gotoctrl")
vel=Twist()
cord=Pose()
x2=int(input("enter X goal"))
y2=int(input("enter y goal"))
beta=1.5
phi=6

cont1=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)  

def cal(x1,y1,theta,x2,y2):
    vel.linear.x=math.sqrt(((x2-x1)**2)+((y2-y1)**2))*beta
    vel.angular.z=phi*(-theta+math.atan2(y2-y1,x2-x1))
    cont1.publish(vel) 

#subscriber 
def callback(pose):
    cal(pose.x,pose.y,pose.theta,x2,y2)

rospy.Subscriber("/turtle1/pose",Pose,callback)

while not rospy.is_shutdown():
    1
    
    




