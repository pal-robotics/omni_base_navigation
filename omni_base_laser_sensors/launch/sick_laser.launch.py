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

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    LaunchConfiguration,
    PythonExpression,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    omni_base_laser_sensors_dir = get_package_share_directory(
        "omni_base_laser_sensors")
    laser_model = LaunchConfiguration("laser")
    side = LaunchConfiguration("side")
    device_number = LaunchConfiguration("device_number")

    declare_side_cmd = DeclareLaunchArgument(
        "side",
        default_value="front",
        description="Specify the side of the laser in the robot",
    )

    declare_device_number_cmd = DeclareLaunchArgument(
        "device_number",
        default_value="0",
        description="Specify the device number of the laser in the robot",
    )

    node = Node(
        package="sick_tim",
        name=PythonExpression(
            ['"', side, '_', laser_model, '_ros_driver".replace("-","_")']),
        executable="sick_tim551_2050001",
        output="screen",
        remappings=[("scan", PythonExpression(['"scan_', side, '_raw"']))],
        parameters=[PathJoinSubstitution(
            [omni_base_laser_sensors_dir, "config", PythonExpression(
                ['"', laser_model, '_laser.yaml"'])],

        ),
            {'frame_id': PythonExpression(['"base_', side, '_laser_link"']),
             'device_number': device_number
             },
        ]
    )

    # Create the launch description
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_side_cmd)
    ld.add_action(declare_device_number_cmd)

    # Add the node with the driver for the laser
    ld.add_action(node)

    return ld
