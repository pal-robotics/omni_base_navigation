^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_laser_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.7 (2024-04-10)
------------------
* Merge branch 'feat/ros2-params' into 'humble-devel'
  Feat/ros2 params
  See merge request robots/omni_base_navigation!20
* launch indipendent nav loc and slam public sim
* added dlo dep
* pipelines for navigation
* fix and change params names
* fix laser pipeline
* renamed lifecycle manager
* corrected dep
* Contributors: andreacapodacqua

2.0.6 (2024-03-06)
------------------
* Merge branch 'feat/dlo-integration' into 'humble-devel'
  integrate dlo_ros
  See merge request robots/omni_base_navigation!19
* cosmetic
* integrate dlo_ros
* Contributors: andreacapodacqua

2.0.5 (2024-03-05)
------------------
* Merge branch 'fix/laser-pipeline' into 'humble-devel'
  renamed apps and removed unuseful args
  See merge request robots/omni_base_navigation!18
* renamed apps and removed unuseful args
* Contributors: andreacapodacqua

2.0.4 (2024-02-28)
------------------
* Merge branch 'aca/experiments-module' into 'humble-devel'
  Aca/experiments module
  See merge request robots/omni_base_navigation!17
* removed unused launch and config files
* cosmetic
* new load of params in module
* added laser filters to pipeline
* remappings laser pipeline
* add lifecycle manager
* laser pipeline
* added laser pipeline
* Contributors: andreacapodacqua

2.0.3 (2024-02-02)
------------------

2.0.2 (2023-12-14)
------------------
* Merge branch 'fix/ros2-laser-sensors' into 'humble-devel'
  Fix/ros2 laser sensors
  See merge request robots/omni_base_navigation!15
* revert last 4 commits
* cosmetic
* cosmetic
* cosmetic
* refactor launch of the sick
* cosmetic
* fix lasers in real robot
* removed old sick and added 571 launch file
* Contributors: andreacapodacqua

2.0.1 (2023-12-11)
------------------
* Merge branch 'fix/modules-ros2' into 'humble-devel'
  moved omni modules from 00 to 10
  See merge request robots/omni_base_navigation!14
* moved omni modules from 00 to 10
* Contributors: Noel Jimenez, andreacapodacqua

2.0.0 (2023-11-23)
------------------
* Merge branch 'feat/use-module' into 'humble-devel'
  Feat/use module
  See merge request robots/omni_base_navigation!12
* cosmetic
* cosmetic
* using correct prefix
* use module
* omni_base ROS 2
* added laser cfg files
* added ira_laser_tool new rviz config
* fix: Typo and time_offset in sick 561
* add missing laser sensor launch.py files
* omnibase laser sensors to ROS 2:
  + colcon
  + yaml
  + launch.py
  - discontinued hokuyo URG-04LX-UG01
* Contributors: Noel Jimenez, YueErro, andreacapodacqua

0.0.11 (2023-03-06)
-------------------

0.0.10 (2023-01-27)
-------------------

0.0.9 (2022-08-16)
------------------
* Merge branch 'fix/lasers-fov' into 'ferrum-devel'
  fix lasers fov
  See merge request robots/omni_base_navigation!5
* adjusted fov for sick laser scanner
* fix hokuyo_urg_04lx_ug01_laser fov
* Contributors: antoniobrandi, josegarcia

0.0.8 (2022-08-08)
------------------

0.0.7 (2022-08-04)
------------------

0.0.6 (2022-07-13)
------------------
* Merge branch 'hokuyo-support' into 'ferrum-devel'
  Hokuyo support
  See merge request robots/omni_base_navigation!1
* Update hokuyo_urg_04lx_ug01_laser.yaml
* Assign laser ports
* Update hokuyo_laser.launch
* Update hokuyo_laser.launch
* Update yaml file in launch file
* Update package.xml
* Adding specificatios for hokuyo
* Contributors: David ter Kuile, antoniobrandi, davidterkuile

0.0.5 (2021-10-26)
------------------
* changed laser sensor configuration for the final base
* Contributors: antoniobrandi

0.0.4 (2021-10-06)
------------------

0.0.3 (2021-10-04)
------------------

0.0.2 (2021-09-30)
------------------
* removed unused dempendencies and adding dependency from ira_laser_tools
* Contributors: antoniobrandi

0.0.1 (2021-09-30)
------------------
* preparing release
* adapting to the new urdf convention using virtual_base_laser_link
* Omni base navigation initial commit
* Contributors: antoniobrandi
