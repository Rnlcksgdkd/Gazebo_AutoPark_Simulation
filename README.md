# Gazebo_AutoPark_Simulation


download catkin_ws/src
cm

cd ..../parkingdemo_gazebo/launch
roslaunch parkingdemo_world.launch
- launch gazebo world

python parking_tracking.py
- show robot's velocity and Trajectory

cd ..../parkingdemo_teleop/launch
roslaunch parking_demo_teleop_key.launch
- launch keyboard control
- w/s -> increase or decrease acceleration
- a/d -> increase or decrease Steer


