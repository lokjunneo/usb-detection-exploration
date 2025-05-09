# Requires udev (linux only)
# Needs additional setup on alpine (udev).

import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('usb')

for device in iter(monitor.poll, None):
    print(device)
    # print(f"{device.action} - {device.device_node}")
    