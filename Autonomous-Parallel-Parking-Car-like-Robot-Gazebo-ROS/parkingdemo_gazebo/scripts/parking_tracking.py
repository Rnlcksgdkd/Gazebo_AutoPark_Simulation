#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$


import roslib
import rospy
import numpy as np
import math
import matplotlib.pyplot as plt

from nav_msgs.msg import Odometry
from std_msgs.msg import Float64


flag = 0
history_x = []
history_y = []
delta_dist = []

f = open('tracking_robot_x_y', 'w+t')

def main():
    
    print("start tracking robot point")
    print("main start")
    rospy.init_node('parallel_parking', anonymous=True) #make node 
    rospy.Subscriber('ground_truth/state',Odometry, save)

    rospy.spin()
    f.close()
    print("finish spin")
    #plt.plot(history_x, history_y)
    plt.plot(delta_dist)
    plt.show()

    plt.plot(history_x, history_y)
    plt.show()
def cal_dist(x,y, n_x , n_y):
    return math.sqrt( (x- n_x)**2 + (y - n_y)**2 )
    
def save(msg):

    print("callback")
    #while not rospy.is_shutdown():
    rate = rospy.Rate(100) # 100hz
    
    current_pos = [msg.pose.pose.position.x, msg.pose.pose.position.y]
    #f.write(current_pos)
    history_x.append(current_pos[0])
    history_y.append(current_pos[1])

    if len(history_x) > 1:
	delta_dist.append(cal_dist(history_x[-2], history_y[-2], history_x[-1], history_y[-1]) )
    print("now point : [ {} , {} ]".format(current_pos[0], current_pos[1]) )
    
    rate.sleep()

if __name__ == "__main__":
    
    main()    
    
    
