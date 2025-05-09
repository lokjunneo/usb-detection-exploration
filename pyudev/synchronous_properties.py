# Requires udev (linux only)
# Needs additional setup on alpine (udev).

import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('usb')

for device in iter(monitor.poll, None):
    if (device.action == "add"):
        print("+"* 50)
        print("Action:", device.action)
        for i in device.properties.keys():
            print(f"{i}: {device.properties[i]}")
        print("+"* 50)
    elif (device.action == "remove"):
        print("-"* 50)
        print("Action:", device.action)
        for i in device.properties.keys():
            print(f"{i}: {device.properties[i]}")
        print("-"* 50)
    
    # print(f"{device.action} - {device.device_node}")
    