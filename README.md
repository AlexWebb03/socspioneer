# The SOCSPIONEER Package

`socspioneer` is a package of launch files, configuration and helper nodes.

## Installation

**NOTE**: *This part assumes basic understanding of Linux terminal and
commandline usage. Basic understanding of ROS workflow and package
organisation is also important (eg. [Creating a colcon workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)).*

### Install Package Dependencies

Clone the following repositories in the `src` directory of your colcon workspace.

- stage_ros2: https://github.com/tuw-robotics/stage_ros2
- Stage: https://github.com/tuw-robotics/Stage

### Build package

- Clone this repo to the `src` directory of your colcon workspace.
- Build the colcon workspace (`colcon build` ).

**NOTE: The colcon workspace should be sourced each time a new
terminal session is loaded (run `source install/setup.sh`). Alternatively,
add the line `source <colcon_ws>/install/setup.sh` to your `.bashrc`
file to avoid repeating it every time.**

## Testing Simulation and Installation

If everything installed correctly, the following steps should provide
a very simplistic simulation of a robot in a provided world map.

1. In one terminal, run `ros2 run stage_ros2 stage_ros2 --ros-args -p world_file:=./src/socspioneer/data/meeting.world`.
This should start a simple simulated world with a robot and a map.
2. In another terminal, run `ros2 launch socspioneer keyboard_teleop.launch.py`.

This would allow you to move the robot using keyboard commands. Note that
when controlling using the keyboard control, the terminal where the
keyboard control node is running should be in focus (click on the terminal
before using the keys to control the robot).

## Simulator Usage

**NOTE**: *This part assumes basic understanding of ROS, ROS topics,
messages, nodes, etc.*

Running `ros2 run stage_ros2 stage_ros2 --ros-args -p world_file:=<.world file>` will start the
simulator with a robot and an obstacle the provided world. The
robot and object can be interacted with using the mouse or using
ROS topics, nodes, etc. The world view can also be changed using
the mouse.

- Pressing `R` on keyboard toggles between 2D and 3D views. 
- `D` key toggles laser field of view visualisation.

The simulator publishes the following (important) topics. By
subscribing to these topics, you can access different sensor
information from the robot.

| ROS Topic | Data | ROS Message Type |
| ------ | ------ | ------ |
| `/odom` | The odometry information from the robot wheel encoders. | [`nav_msgs/Odometry`](http://docs.ros.org/kinetic/api/nav_msgs/html/msg/Odometry.html) |
| `/base_scan` | Laser scan data from the laser scanner at the front of the robot. | [`sensor_msgs/LaserScan`](http://docs.ros.org/kinetic/api/sensor_msgs/html/msg/LaserScan.html) |

The simulator subscribes to the following topics. You can control
the robot using this.

| ROS Topic | Data | ROS Message Type |
| ------ | ------ | ------ |
| `/cmd_vel` | Velocity commands to the robot's wheel motors. | [`geometry_msgs/Twist`](http://docs.ros.org/melodic/api/geometry_msgs/html/msg/Twist.html) |
