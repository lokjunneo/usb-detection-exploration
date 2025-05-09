# Pull image
# curl -O https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.5.0-amd64-netinst.iso
# curl -O https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-standard-3.19.1-x86_64.iso
curl -O https://nl.alpinelinux.org/alpine/v3.8/releases/x86_64/alpine-standard-3.8.0-x86_64.iso

# Create image
qemu-img create -f qcow2 alpine.qcow2 16G

# Install & Boot

qemu-system-x86_64 \
    -m 2048 \
    -nic user,model=virtio \
    -boot d \
    -hda alpine.qcow2 \
    -cdrom alpine-standard-3.8.0-x86_64.iso

# setup-alpine, use "sda" disk with "sys" installation
# https://wiki.alpinelinux.org/wiki/QEMU#Install_Alpine_Linux_in_QEMU

# Boot existing
qemu-system-x86_64 \
    -m 2048 \
    -nic user,model=virtio \
    -usb -device usb-ehci \
    -boot d \
    -hda alpine.qcow2

# ctrl + option + 1 to switch between Qemu Monitor and Linux