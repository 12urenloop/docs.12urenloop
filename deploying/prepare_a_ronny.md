---
parent: Deploying
title: Preparing a ronny for the ansible-config
---

# Preparing a ronny for the ansible-config

1. Download the latest Armbian (Debian 13 minimal) image from <https://armbian.com/boards/rpi4b>

2. Uncompress it: `unxz Armbian_x.y.z_Rpi4b_trixie_current_x.y.z_minimal.img.xz`

3. Flash it to the µSD card with e.g.: `dd if=Armbian_x.y.z_Rpi4b_trixie_current_x.y.z_minimal.img of=/dev/sdX bs=1M oflag=sync status=progress` , substitute `/dev/sdX` for the µSD card as reported by `lsblk -f` and triple check this.

4. Attach the ronny to the Telnet switch.

5. Power up the ronny.

6. Ssh to `root@172.12.50.10X`, where `X` is the ronny's number:
    - Set the root password.
    - Create the `zeus` user, with the same password as root.
    - **Now close your terminal**
    - That's it!
