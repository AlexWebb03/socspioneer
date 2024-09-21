from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    tf_publisher = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="odom_to_map",
        arguments=["--frame-id", "map", "--child-frame-id", "odom"]
    )

    ld = LaunchDescription()
    ld.add_action(tf_publisher)

    return ld
