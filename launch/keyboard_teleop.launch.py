from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    teleop_node = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        name="teleop_twist_keyboard",
        remappings=[("twist", "cmd_vel")],
        prefix = "xterm -e",
        output="screen"
    )

    ld = LaunchDescription()
    ld.add_action(teleop_node)

    return ld
