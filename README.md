# Formula1 Inspired CAD Modeling and Simulation using Gazebo

![Formula1 Car](link-to-image)

## Project Overview

**Student:** Rishikesh Jadhav  
**Email:** rjadhav1@umd.edu  
**Project:** CAD Modelling of a Formula 1 Car followed by Simulation and Visualization in Gazebo

## Project Goals

1. Build a car in Solidworks and export it as a URDF file.
2. Add Lidar sensor modules to the car model and visualize in Rviz and Gazebo.
3. Create an empty Gazebo world and transform it into a competition arena.
4. Perform TeleOP using a coded publisher and subscriber node to navigate the competition arena.

## Project Steps and Flow

1. Create part models for building the car in Solidworks.
2. Assemble the car in Solidworks.
3. Export the car model as a URDF file.
4. Create a catkin_ws for sourcing, building, and developing the project.
5. Create a dummy link and joint to visualize the model in the environment.
6. Add transmission blocks to include controllers in the URDF of the car.
7. Integrate Lidar sensor and Car Model URDF using the Xacro file.
8. Configure controllers assigned to joints in the .yaml file.
9. Add Lidar sensor module to the workspace.
10. Perform TeleOP to manually move the model in the simulation environment.
11. Code a simple publisher and a subscriber to make the car move in a perfect circle.
12. Visualize the model in Rviz.
13. Simulate the model in Gazebo.

## Simulation Videos

- [![TeleOP Video](https://img.youtube.com/vi/04WyU0NI-ak/0.jpg)](https://www.youtube.com/watch?v=04WyU0NI-ak)
- [![Publisher-Subscriber Video](https://img.youtube.com/vi/1rl0F7T2MxY/0.jpg)](https://www.youtube.com/watch?v=1rl0F7T2MxY)

## Challenges Faced

- Mating parts in assembly.
- Assigning frames and axes to each joint correctly.
- Car model not spawning as expected in Gazebo (parts were dislocated).
- Understanding and integrating all files (Xacro, .yaml, URDF, .launch).
- Lidar sensor visualization in Rviz.
- Wobbling while moving in simulation (fixed by adjusting PID values).

## Contribution

- Designing and modeling Formula 1 inspired car parts in Solidworks.
- Assembling parts and defining axes and frames where necessary.
- Creating URDF, setting appropriate limits, and successfully exporting/importing in Gazebo.
- Creating a dummy link and joint for visualization.
- Integrating Lidar Sensor to the model.
- Integration of the model into the competition arena for visualization.
- Working on resolving errors during TeleOP.
- Coding the Publisher and Subscriber nodes for motion control.

## Project Structure

- **Assembly:** Contains part models and assembly files.
- **Package:** Includes subfolders for configuration, launch, meshes, source code, textures, URDF, and world files.
- **Report:** PDF document detailing the project.
- **Results:** Simulation videos.

## Instructions to Run the Package

1. Unzip the package (updated\_assembly).
2. Move the folder into the `src` folder of the catkin workspace.
3. Build the package using `catkin_make clean && catkin_make` (don't forget to source before building).
4. Launch the car in Gazebo: `roslaunch updated\_assembly updated\_assembly.launch`.
5. Open Rviz to visualize the robot in a parallel terminal (start simulation in Gazebo first).
6. Open the teleop file in another terminal: `python3 teleop\_template.py`.
7. To run the publisher\_subscriber, open four terminals (roscore, launch robot in Gazebo, publisher, subscriber).
8. Comment out the competition arena line in the launch file for the robot to move in a circle.
9. After completing the steps, the car should move in circles in the empty world in Gazebo.
