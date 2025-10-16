#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist    #came from terminal by checking ros2 topic list then ros2 topic info
class Drawcircle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ =  self.create_publisher(Twist,"/turtle1/cmd_vel",10)    #cmd_vel  etc are inbuild command and the value in parentesis is also from terminal 
        self.timer_ = self.create_timer(0.5,self.send_velocity_command)   # to call back
        self.get_logger().info("hello I am Prem. Nice to meet you.")    #just print this line

    def send_velocity_command(self): #this is callback funtion in which we instruct what to publish
        msg=Twist()
        msg.linear.x = 0.5                    #this are math illustrate in terminal in ros2 interface show geometry.msgs.msg
        msg.angular.z=0.5
        self.cmd_vel_pub_.publish(msg)   # message that to publish

def main(args=None):
    rclpy.init(args=args)
    node=Drawcircle()
    rclpy.spin(node)    # this command kept  alive the code then  rerun the above timer after 0.5 sec send velocity publish again  
    rclpy.shutdown()