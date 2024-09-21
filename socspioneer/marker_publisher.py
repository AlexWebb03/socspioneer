import rclpy
import rclpy.duration
from rclpy.node import Node

# documentation: http://wiki.ros.org/rviz/DisplayTypes/Marker
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

class MarkerPublisher(Node):

    def __init__(self):
        super().__init__('marker_publisher')
        self.publisher_ = self.create_publisher(Marker, '/visualization_marker', 10)

    def publish_marker(self):
        id_counter = 0

        # place a point
        m = Marker()

        # specify reference frame (options in RViz Global Options > Fixed Frame)
        # markers relative to 0,0 in odometry
        m.header.frame_id = '/odom'
        m.header.stamp    = self.get_clock().now().to_msg()

        # marker with same namespace and id overrides existing
        m.ns = 'my_markers'
        m.id = id_counter
        id_counter += 1

        m.type = Marker.SPHERE
        m.action = Marker.ADD

        m.pose.position.x = 0.0
        m.pose.position.y = 0.0
        m.pose.position.z = 0.0
        m.pose.orientation.x = 0.0
        m.pose.orientation.y = 0.0
        m.pose.orientation.z = 0.0
        m.pose.orientation.w = 1.0
        m.scale.x = 1.0
        m.scale.y = 1.0
        m.scale.z = 1.0
        m.color.r = 1.0
        m.color.g = 0.0
        m.color.b = 0.0
        m.color.a = 1.0

        m.lifetime = rclpy.duration.Duration().to_msg() # forever
        #m.lifetime = rclpy.Duration(...)

        self.publisher_.publish(m)

def main(args=None):
    rclpy.init(args=args)

    marker_publisher = MarkerPublisher()
    marker_publisher.publish_marker()

    rclpy.spin(marker_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
