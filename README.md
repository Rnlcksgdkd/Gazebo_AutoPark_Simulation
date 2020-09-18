# Gazebo_AutoPark_Simulation
# 가즈보로 만든 자동주차 테스트를 위한 시뮬레이션입니다

![스크린샷, 2019-11-08 01-21-58](https://user-images.githubusercontent.com/55937069/93562277-af66ac00-f9c0-11ea-95b9-aa524df52fba.png)
![스크린샷, 2019-11-08 02-06-31](https://user-images.githubusercontent.com/55937069/93562280-b097d900-f9c0-11ea-9b51-8e7f7949d924.png)
![스크린샷, 2019-11-22 07-49-39](https://user-images.githubusercontent.com/55937069/93562282-b097d900-f9c0-11ea-8765-bcb8e3c664f4.png)


# How to Install and launch

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


