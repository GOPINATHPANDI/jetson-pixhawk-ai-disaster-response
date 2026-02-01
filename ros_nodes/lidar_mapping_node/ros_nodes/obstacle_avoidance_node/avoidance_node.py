#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidanceNode:
    def __init__(self):
        rospy.init_node("obstacle_avoidance_node")

        self.cmd_pub = rospy.Publisher(
            "/mavros/setpoint_velocity/cmd_vel_unstamped",
            Twist,
            queue_size=1
        )

        rospy.Subscriber("/scan", LaserScan, self.scan_callback)
        rospy.loginfo("Obstacle Avoidance Node Started")

    def scan_callback(self, scan):
        cmd = Twist()
        front_dist = min(scan.ranges[0:10] + scan.ranges[-10:])

        if front_dist < 1.5:
            cmd.linear.y = 0.5   # move sideways
            cmd.linear.x = 0.0
        else:
            cmd.linear.x = 1.0   # move forward

        self.cmd_pub.publish(cmd)

if __name__ == "__main__":
    ObstacleAvoidanceNode()
    rospy.spin()
