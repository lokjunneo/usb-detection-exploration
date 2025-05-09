# Requires udev (linux only)
# Needs additional setup on alpine (udev).

import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('usb')

for device in iter(monitor.poll, None):
    for attr in device.attributes.available_attributes:
        print("="*50)
        print("Action:", device.action)
        try:
            print(f"{attr}: {device.attributes.asstring(attr)}")
        except:
            print(f"{attr}:") # No values
        print("="*50)
    
    # print(f"{device.action} - {device.device_node}")
    