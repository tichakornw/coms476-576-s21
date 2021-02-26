#!/usr/bin/env python2

import rospy
import numpy as np
from std_msgs.msg import Float64

joint_controller_map = {
    'shoulder_pan_joint':  '/shoulder_pan_joint_position_controller/command',
    'shoulder_lift_joint': '/shoulder_lift_joint_position_controller/command',
    'elbow_joint':         '/elbow_joint_position_controller/command',
    'wrist_1_joint':       '/wrist_1_joint_position_controller/command',
    'wrist_2_joint':       '/wrist_2_joint_position_controller/command',
    'wrist_3_joint':       '/wrist_3_joint_position_controller/command',
}

def planner():
    pubs = {}
    for joint, controller in joint_controller_map.items():
        pubs[joint] = rospy.Publisher(controller, Float64, queue_size=1)

    config = {}
    for joint in joint_controller_map.keys():
        config[joint] = 0.0

    rospy.init_node('planner', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    t = 0
    while not rospy.is_shutdown():
        t = (t + 1) % 50
        # shoulder_lift_joint's angle goes from -pi/2 to 0
        config['shoulder_lift_joint'] = np.pi / 4.0 * (-1.0 + np.cos(t / 50.0 * 2.0 * np.pi))
        config['elbow_joint']         = -config['shoulder_lift_joint']
        config['wrist_1_joint']       = -np.pi / 2.0

        rospy.loginfo('{}'.format(config['shoulder_lift_joint']))
        for joint, pos in config.items():
            pubs[joint].publish(pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        planner()
    except rospy.ROSInterruptException:
        pass