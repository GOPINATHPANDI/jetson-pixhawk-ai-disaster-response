from pymavlink import mavutil

mav = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)
mav.wait_heartbeat()

def send_object_count(name, value):
    mav.mav.named_value_int_send(0, name.encode(), value)
