#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

class LidarMappingNode:
    def __init__(self):
        rospy.init_node("lidar_mapping_node")
        rospy.Subscriber("/scan", LaserScan, self.scan_callback)
        rospy.loginfo("LiDAR Mapping Node Started")

    def scan_callback(self, msg):
        # SLAM handled by gmapping
        min_distance = min(msg.ranges)
        rospy.loginfo_throttle(2, f"Closest obstacle: {min_distance:.2f} m")

if __name__ == "__main__":
    LidarMappingNode()
    rospy.spin()
