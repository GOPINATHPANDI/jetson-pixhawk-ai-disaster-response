"""
Preprocessing for AI inference
"""

import cv2

def preprocess(frame, input_size=(640, 640)):
    frame_resized = cv2.resize(frame, input_size)
    frame_normalized = frame_resized / 255.0
    return frame_normalized
