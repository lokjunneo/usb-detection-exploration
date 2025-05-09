# Pull image
# curl -O https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.5.0-amd64-netinst.iso
# curl -O https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-standard-3.19.1-x86_64.iso
curl -O https://nl.alpinelinux.org/alpine/v3.8/releases/x86_64/alpine-standard-3.8.0-x86_64.iso

# Create image
qemu-img create -f qcow2 alpine.qcow2 16G

# Boot up

qemu-system-x86_64 \
    -m 2048 \
    -nic user,model=virtio \
    -drive file=alpine.qcow2,media=disk,if=virtio \
    -cdrom alpine-standard-3.8.0-x86_64.iso 

# ctrl + option + 1 to switch between Qemu Monitor and Linux