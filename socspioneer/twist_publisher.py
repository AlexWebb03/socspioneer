import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class TwistPublisher(Node):
    def __init__(self):
        super().__init__('twist_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.msg = Twist()
        self.msg.linear.x = 0.1

    def timer_callback(self):
        self.publisher_.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)

    twist_publisher = TwistPublisher()

    rclpy.spin(twist_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
