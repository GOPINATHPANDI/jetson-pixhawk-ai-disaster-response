"""
AI Inference Module
Runs object detection on camera frames and returns detections.
Model weights are loaded externally.
"""

import cv2

CLASS_NAMES = ["person", "debris", "vehicle", "equipment"]

def load_model(model_path):
    """
    Load ONNX / TensorRT model here.
    """
    print(f"[INFO] Loading model from {model_path}")
    model = None  # placeholder
    return model

def run_inference(frame, model):
    """
    Runs inference on a frame.
    Returns list of detections.
    Each detection: {label, confidence, bbox}
    """
    height, width, _ = frame.shape

    # ---- PLACEHOLDER OUTPUT ----
    detections = [
        {
            "label": "person",
            "confidence": 0.87,
            "bbox": [int(0.3*width), int(0.2*height), int(0.6*width), int(0.7*height)]
        }
    ]

    return detections
