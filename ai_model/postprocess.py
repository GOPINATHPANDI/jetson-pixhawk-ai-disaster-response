"""
Postprocessing AI outputs
"""

def count_objects(detections):
    counts = {}
    for det in detections:
        label = det["label"]
        counts[label] = counts.get(label, 0) + 1
    return counts
