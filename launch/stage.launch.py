import os

from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    share_dir = get_package_share_directory("socspioneer")

    lifecycle_manager = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        parameters=[{"node_names": ["map_server"], "autostart": True}]
    )

    map_server = Node(
        package="nav2_map_server",
        executable="map_server",
        parameters=[{"yaml_filename": os.path.join(share_dir, "data", "lgfloor.yaml")}]
    )

    stage_ros2 = Node(
        package="stage_ros2",
        executable="stage_ros2",
        parameters=[{"world_file": os.path.join(share_dir, "data", "lgfloor.world")}]
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", [os.path.join(share_dir, "config", "map_view.rviz")]]
    )

    ld = LaunchDescription()
    ld.add_action(lifecycle_manager)
    ld.add_action(map_server)
    ld.add_action(stage_ros2)
    ld.add_action(rviz2)

    return ld
