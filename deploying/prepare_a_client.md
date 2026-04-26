---
parent: Deploying
title: Preparing a client for the ansible-config
---

# Preparing a client for the ansible-config

1. Download the Debian netinst image `debian-x.y.z-amd64-netinst.iso` from: <https://ftp.belnet.be/debian-cd/current/amd64/iso-cd/>

2. Flash it to a (Zeus) usb stick with e.g.: `dd if=debian-x.y.z-amd64-netinst.iso of=/dev/sdX bs=1M oflag=sync status=progress` , substitute `/dev/sdX` for the usb stick as reported by `lsblk -f` and triple check this.

3. Boot from the installer usb by mashing `F12` on boot.

4. Proceed through the installer:

- Connect it to the kelder network during installation.
- Set the language to `English`.
- Set the location to `Belgium` or `Brussels`.
- Set the locale to `en_GB.UTF-8`.
- Set the keymap to `Belgian`.
- Use **ethernet** for networking.
- Set the **hostname to `client1` or `client2`**.
- Leave the domain empty.
- **Use `zeus` as the default username**.
- Overwrite the **entire disk** with `Guided - use entire disk`.
- Use the recommended mirror, without proxy.
- Select any desktop environment, and **enable ssh**.

5. Wait for the installer to finish, **unplug the ethernet cable**, then configure the following:

- Disable shutdown on power button press.
- **Disable auto-suspend**.
- Disable screensaver / display auto power off.

Repeat steps 3 through 5 for the other client as well.
