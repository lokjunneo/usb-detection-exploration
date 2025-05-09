# Requires udev (linux only)
# Needs additional setup on alpine (udev).

import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('usb')

possibly_useful_properties = ["DEV_TYPE",
                              "DRIVER",
                            "ID_BUS",
                            "ID_FOR_SEAT",
                            "ID_MODEL",
                            "ID_MODEL_ENC",
                            "ID_REVISION",
                            "ID_SERIAL",
                            "ID_SERIAL_SHORT",
                            "ID_USB_MODEL",
                            "ID_USB_MODEL_ENC",
                            "ID_USB_MODEL_ID",
                            "ID_USB_REVISION",
                            "ID_USB_SERIAL",
                            "ID_USB_SERIAL_SHORT",
                            "ID_USB_VENDOR",
                            "ID_USB_VENDOR_ENC",
                            "ID_USB_VENDOR_ID",
                            "ID_VENDOR",
                            "ID_VENDOR_ENC",
                            "ID_VENDOR_FROM_DATABASE",
                            "ID_VENDOR_ID",
                              ]
for device in iter(monitor.poll, None):
    if (device.action == "add"):
        print("+"* 50)
        print("Action:", device.action)
        print("...")
        # Loop below is not optimized
        for i in possibly_useful_properties: 
            if i in device.properties:
                print(f"{i}: {device.properties[i]}")
        print("+"* 50)
    elif (device.action == "remove"):
        print("-"* 50)
        print("Action:", device.action)
        if "ID_MODEL" in device.properties:
            print(f"ID_MODEL: {device.properties[i]}")
        print("+"* 50)
    
    # print(f"{device.action} - {device.device_node}")
    