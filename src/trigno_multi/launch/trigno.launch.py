from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

from launch_ros.actions import Node


def generate_launch_description():
    trigno_node = Node(
            package="trigno_multi",
            namespace="",
            executable="trigno",
            name="trigno",
        )
        
    return LaunchDescription([
        trigno_node,
    ])

