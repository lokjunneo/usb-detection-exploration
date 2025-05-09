# Pull image

# curl -O https://nl.alpinelinux.org/alpine/v3.8/releases/x86_64/alpine-standard-3.8.0-x86_64.iso

# wget https://cdimage.debian.org/cdimage/daily-builds/daily/arch-latest/amd64/iso-cd/debian-testing-amd64-netinst.iso
# wget https://cdimage.debian.org/debian-cd/current/arm64/iso-cd/debian-12.10.0-arm64-netinst.iso
wget https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso
# Create image
# qemu-img create -f qcow2 alpine.qcow2 16G
qemu-img create -f qcow2 debian.qcow2 16G

# Install & Boot
# (Software selection - Only need standard system utilities)

qemu-system-x86_64 \
  -m 2048 \
  -nic user,model=virtio \
  -hda debian.qcow2 \
  -k en-us \
  -cdrom debian-12.10.0-amd64-netinst.iso \
  -boot d \
  -usb -device usb-ehci

# Boot existing
qemu-system-x86_64 \
    -m 2048 \
    -nic user,model=virtio \
    -usb -device usb-ehci \
    -k en-us \
    -boot d \
    -hda debian.qcow2

# ctrl + option + 1 to switch between Qemu Monitor and Linux

# Boot existing in serial monitor

# If GRUB is installed:
#   In Guest OS (use above command to access, run)
#   sudo nano /etc/default/grub

# Then modify/add this lines
# GRUB_TERMINAL=serial
# GRUB_SERIAL_COMMAND="serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1"
# GRUB_CMDLINE_LINUX="console=tty0 console=ttyS0"

qemu-system-x86_64 \
    -m 2048 \
    -nic user,model=virtio \
    -nographic \
    -serial mon:stdio \
    -usb -device usb-ehci \
    -k en-us \
    -boot d \
    -hda debian.qcow2

# https://www.qemu.org/docs/master/system/mux-chardev.html
# ctrl-a c switches between qemu console and debian 
# (Press ctrl-a, release, then press c)

# setup-alpine, use "sda" disk with "sys" installation
# https://wiki.alpinelinux.org/wiki/QEMU#Install_Alpine_Linux_in_QEMU