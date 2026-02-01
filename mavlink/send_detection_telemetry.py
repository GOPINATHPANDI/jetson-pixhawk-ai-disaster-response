"""
Sends AI detection results to Pixhawk via MAVLink
"""

from pymavlink import mavutil
import time

class MavlinkTelemetry:
    def __init__(self, port="/dev/ttyACM0", baud=115200):
        self.mav = mavutil.mavlink_connection(port, baud=baud)
        self.mav.wait_heartbeat()
        print("[INFO] MAVLink connected")

    def send_object_count(self, label, count):
        """
        Uses NAMED_VALUE_INT for telemetry
        Label must be <= 10 chars
        """
        label_short = label[:10]
        timestamp = int(time.time() * 1000) & 0xFFFFFFFF

        self.mav.mav.named_value_int_send(
            timestamp,
            label_short.encode("utf-8"),
            int(count)
        )
