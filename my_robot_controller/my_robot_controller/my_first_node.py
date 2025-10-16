#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Mynode(Node):       #now our class have all the funtionatries of ros2
    def __init__(self):
        self.counter=0
        super().__init__("first_node")
        self.create_timer(1,self.timer_callback)
    def timer_callback(self):
        self.counter+=1
        self.get_logger().info(f"from ross {self.counter}" )


def main(args=None):
    rclpy.init(args=args)     #initialize ros2 communication

    node=Mynode()  
    rclpy.spin(node)                         #input the program 
    rclpy.shutdown()           #stop the communication

                            #whenever the spin command works interpreter goes to init fun that again runin which timer callback also runs again 


if __name__=="__main__":     # used to directly execute the file in the terminal
    main()
