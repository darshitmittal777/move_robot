#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.curr = None
        self.countt = 0
        self.pose_subscriber = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.create_timer(0.2,self.print_pose)

    def pose_callback(self, msg: Pose):
        self.curr = msg

    def print_pose(self):
        self.get_logger().info(str(self.curr.x)+","+str(self.curr.y)+" Iteration: "+str(self.countt))
        self.countt += 1

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
    