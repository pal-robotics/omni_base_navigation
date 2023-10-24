# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import (
    PathJoinSubstitution,
    LaunchConfiguration,
    PythonExpression,
)
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():
    omni_base_laser_sensors_dir = get_package_share_directory("omni_base_laser_sensors")
    laser_model = LaunchConfiguration("laser")

    declare_laser_cmd = DeclareLaunchArgument(
        "laser",
        default_value="sick-561",
        description="Specify the type of laser in the robot",
    )

    laser_config_path = PathJoinSubstitution(
        substitutions=[
            omni_base_laser_sensors_dir,
            "config",
            PythonExpression(
                ['"', laser_model, '_filter.yaml"']
            ),
        ]
    )

    multi_laser_node = Node(
        package="ira_laser_tools",
        executable="laserscan_multi_merger",
        output="screen",
        parameters=[{'destination_frame': 'virtual_base_laser_link',
                     'cloud_destination_topic': '/merged_cloud',
                     'scan_destination_topic': '/scan_raw',
                     'laserscan_topics': '/scan_front_raw /scan_rear_raw',
                     'time_increment': '0.0',
                     'scan_time': 0.0,
                     'range_min': 0.05,
                     'range_max': 25.0,
                     'angle_min': -3.1459,
                     'angle_max': 3.1459,
                     'angle_increment': 0.005769,
                    }],
    )

    laser_filter_node = Node(
        package="laser_filters",
        # name = 'laser_filter',        # Name changed produces multiple nodes with the same name.
        # https://answers.ros.org/question/344141/ros2-launch-creates-two-nodes-of-same-type/
        executable="scan_to_scan_filter_chain",
        output="screen",
        remappings=[("scan", "scan_raw"), ("scan_filtered", "scan")],
        parameters=[laser_config_path],
    )

    # Create the launch description
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_laser_cmd)

    # Add the actions to launch all of the laser nodes
    ld.add_action(laser_filter_node)
    ld.add_action(multi_laser_node)

    return ld