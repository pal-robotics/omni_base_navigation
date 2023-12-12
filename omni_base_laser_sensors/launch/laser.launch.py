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
from launch.substitutions import (
    PathJoinSubstitution,
    LaunchConfiguration,
    PythonExpression,
)
from launch.actions import (
    IncludeLaunchDescription,
    DeclareLaunchArgument,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    omni_base_laser_sensors_dir = get_package_share_directory("omni_base_laser_sensors")
    laser_model = LaunchConfiguration("laser")

    declare_laser_cmd = DeclareLaunchArgument(
        "laser",
        default_value="sick-561",
        description="Specify the type of laser in the robot",
    )

    front_laser_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                substitutions=[
                    omni_base_laser_sensors_dir,
                    "launch",
                    PythonExpression(
                        [
                            '"',
                            laser_model,
                            '_laser.launch.py"',
                        ]
                    ),
                ]
            )
        ),
        launch_arguments={
            "side":"front",
            "device_number":"0",
        }.items()
    )

    rear_laser_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                substitutions=[
                    omni_base_laser_sensors_dir,
                    "launch",
                    PythonExpression(
                        [
                            '"',
                            laser_model,
                            '_laser.launch.py"',
                        ]
                    ),
                ]
            )
        ),
        launch_arguments={
            "side":"rear",
            "device_number":"1",
        }.items()
    )

    laser_filters_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            omni_base_laser_sensors_dir, 'launch', 'laser_filters.launch.py')]
        )
    )

    # Create the launch description
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_laser_cmd)

    # Add the actions to launch all of the laser nodes
    ld.add_action(front_laser_launch)
    ld.add_action(rear_laser_launch)
    ld.add_action(laser_filters_launch)

    return ld
