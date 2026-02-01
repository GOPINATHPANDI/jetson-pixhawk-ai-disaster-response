#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import json

from ai_model.inference import load_model, run_inference
from ai_model.postprocess import count_objects
from mavlink.send_detection_telemetry import MavlinkTelemetry

class ObjectDetectionNode:
    def __init__(self):
        rospy.init_node("object_detection_node")

        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher("/detection/image", Image, queue_size=1)
        self.count_pub = rospy.Publisher("/detection/counts", String, queue_size=1)

        self.cap = cv2.VideoCapture(0)
        self.model = load_model("ai_model/onnx/model.onnx")
        self.mavlink = MavlinkTelemetry()

        rospy.loginfo("Object Detection Node Started")

    def run(self):
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            if not ret:
                continue

            detections = run_inference(frame, self.model)
            counts = count_objects(detections)

            # Publish counts to ROS
            self.count_pub.publish(json.dumps(counts))

            # Send to Pixhawk via MAVLink
            for label, count in counts.items():
                self.mavlink.send_object_count(label, count)

            # Publish image
            img_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.image_pub.publish(img_msg)

            rate.sleep()

if __name__ == "__main__":
    node = ObjectDetectionNode()
    node.run()

