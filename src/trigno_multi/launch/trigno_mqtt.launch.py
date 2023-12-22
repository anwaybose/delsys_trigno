from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

from launch_ros.actions import Node


def generate_launch_description():
    trigno_node = Node(
            package="trigno_multi",
            namespace="",
            executable="trigno",
            name="trigno",
        )
        
     # include xml launch file
    launch_include = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("mqtt_client"),
                "launch/standalone.launch.ros2.xml",
            )
        )
    )
        
    return LaunchDescription([
        launch_include, trigno_node,
    ])

