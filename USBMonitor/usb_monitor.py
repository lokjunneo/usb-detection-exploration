from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL, ID_MODEL_ID, ID_VENDOR_ID
import time
device_info_str = lambda device_info: f"\tModel: {device_info[ID_MODEL]}\n\tID:{device_info[ID_MODEL_ID]}\n\tVendor ID:{device_info[ID_VENDOR_ID]}"
# Define the `on_connect` and `on_disconnect` callbacks
on_connect = lambda device_id, device_info: print(f"Connected: +++\n{device_info_str(device_info=device_info)}\n+++")
on_disconnect = lambda device_id, device_info: print(f"Disconnected: ---\n{device_info_str(device_info=device_info)}\n---")

# Create the USBMonitor instance
# https://github.com/Eric-Canas/USBMonitor?tab=readme-ov-file#api-reference
monitor = USBMonitor(filter_devices= None) # Insert filter here

# (Tested on Windows) cannot scan_monitor after start_monitor
scan_monitor = USBMonitor(filter_devices= None)

# Start the daemon
monitor.start_monitoring(on_connect=on_connect, on_disconnect=on_disconnect)

print("(1 -> scan, 2-> exit)")
while 1:
    r = input("")
    if r == "2":  break
    elif r == "1": 
        devices_dict = scan_monitor.get_available_devices() 
        # Print them
        for device_id, device_info in devices_dict.items():
            print(f"{device_id} -- {device_info[ID_MODEL]} ({device_info[ID_MODEL_ID]} - {device_info[ID_VENDOR_ID]})")

# If you don't need it anymore stop the daemon
monitor.stop_monitoring()