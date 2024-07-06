#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import time

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        self.publisher_ = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        time.sleep(2)  # Wait for publisher to be ready

    def move_turtle(self, linear_speed, angular_speed, duration):
        twist = Twist()
        twist.linear.x = linear_speed
        twist.angular.z = angular_speed
        self.publisher_.publish(twist)
        rospy.loginfo(f"Moving: linear_speed={linear_speed}, angular_speed={angular_speed}, duration={duration}")
        time.sleep(duration)
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher_.publish(twist)
        rospy.loginfo("Stopping")
        time.sleep(1)

    def draw_letter_T(self):
        rospy.loginfo("Drawing letter T")
        self.move_turtle(2.0, 0.0, 1.0)
        self move_turtle(0.0, math.pi/2, 1.0)
        self move_turtle(2.0, 0.0, 0.5)
        self move_turtle(0.0, -math.pi/2, 1.0)
        self move_turtle(2.0, 0.0, 1.0)

if __name__ == '__main__':
    turtle_controller = TurtleController()
    turtle_controller.draw_letter_T()
    rospy.spin()