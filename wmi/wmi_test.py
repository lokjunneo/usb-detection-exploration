#https://stackoverflow.com/questions/61158399/detecting-insertion-removal-of-usb-input-devices-on-windows-10

import wmi
import pythoncom
import threading

# Function to scan existing USB devices
def list_usb_devices():
    c = wmi.WMI()
    for usb in c.Win32_USBHub():
        # List of attributes at https://learn.microsoft.com/en-us/previous-versions/windows/desktop/cimwin32a/win32-usbhub
        print(f"Device: {usb.Name} | PNPDeviceID: {usb.PNPDeviceID}")

# Function to monitor USB plug/unplug events
def monitor_usb():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    watcher_insert = c.Win32_USBHub.watch_for(notification_type="Creation")
    watcher_remove = c.Win32_USBHub.watch_for(notification_type="Deletion")

    while True:
        try:
            inserted = watcher_insert(timeout_ms=50)
            print(f"[+] Inserted: {inserted.Name} | PNPDeviceID: {inserted.PNPDeviceID}")

        except wmi.x_wmi_timed_out:
            pass

        try:
            removed = watcher_remove(timeout_ms=50)
            print(f"[-] Removed: {removed.Name} | PNPDeviceID: {removed.PNPDeviceID}")
        except wmi.x_wmi_timed_out:
            pass

# Run monitor in background thread
if __name__ == "__main__":
    print("Listing current USB devices:")
    list_usb_devices()

    print("\nMonitoring USB changes (Ctrl+C to stop)...")
    monitor_thread = threading.Thread(target=monitor_usb, daemon=True)
    monitor_thread.start()

    # Keep the main thread alive
    try:
        while True:
            input("Press Enter to scan usb devices:")
            list_usb_devices()
    except KeyboardInterrupt:
        print("\nStopped monitoring.")
