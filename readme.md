## Pyudev

Requires libudev 151 and newer. (Linux only)

## PyWin32

Windows only

## Monitoring /dev or /media filesystem (Linux/macOS)



## Qemu commands

Simulate adding/disconnecting usb device

```sh
(qemu) device_add usb-audio,id=mic1,bus=usb-bus.0
(qemu) device_del mic1
```