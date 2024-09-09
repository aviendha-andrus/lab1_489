from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration, PythonExpression
from ament_index_python.packages import get_package_share_directory
import os
import yaml

def generate_launch_description():
    ld = LaunchDescription()

    # allows for command line input
    v_parameter = LaunchConfiguration('v', default=0.0)
    d_parameter = LaunchConfiguration('d', default=0.0)

    talker_node = Node(
        package='lab1_pkg',
        executable='talker',
        name='talker',
        parameters=[
            {'v': v_parameter},
            {'d': d_parameter}
        ],
        output='screen',
    )

    relay_node = Node(
        package='lab1_pkg',
        executable='relay',
        name='relay',
        output='screen',
    )

    ld.add_action(talker_node)
    ld.add_action(relay_node)

    return ld