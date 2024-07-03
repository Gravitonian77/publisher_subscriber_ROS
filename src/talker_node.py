#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher_ = self.create_publisher(String, 'Buffer', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, my name is Roko! {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    
    #Initialize rclpy
    rclpy.init(args=args)
    
    #Create a node
    node = TalkerNode()
    
    #Use node
    rclpy.spin(node)
    
    #Destroy node
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
