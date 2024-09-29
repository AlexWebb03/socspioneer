import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    share_dir = get_package_share_directory("socspioneer")

    use_sim_time_arg = DeclareLaunchArgument(
        name="use_sim_time",
        default_value="true",
        description="Use simulated time instead of real time.",
        choices=["true", "True", "false", "False"],
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", [os.path.join(share_dir, "config", "demo.rviz")]]
    )

    stage_ros2 = Node(
        package="stage_ros2",
        executable="stage_ros2",
        parameters=[{"world_file": os.path.join(share_dir, "data", "meeting.world")}]
    )

    slam_toolbox = Node(
        package="slam_toolbox",
        executable="sync_slam_toolbox_node",
        parameters=[{"base_frame": "base_link"}],
        remappings=[("scan", "base_scan")]
    )

    ld = LaunchDescription()
    ld.add_action(use_sim_time_arg)
    ld.add_action(rviz2)
    ld.add_action(stage_ros2)
    ld.add_action(slam_toolbox)

    return ld
