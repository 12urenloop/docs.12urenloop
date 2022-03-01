---
title: Gyrid
---

Deprecated
{: .label .label-red }

# Gyrid Setup

- Try accessing gyrids via ssh
  - Access gyrid through a [serial connection](https://wiki.archlinux.org/index.php/Working_with_the_serial_console)
  - Successful connections used a baud rate of 38400 or 24000, with 8 data bits, no parity bit and 1 stopbit.
- Run [setup.sh](https://github.com/ZeusWPI/12urenloop/blob/master/config/setup.sh)
- Add ssh keys for future easy access
- Replace /etc/gyrid.conf with [this one](https://github.com/ZeusWPI/12urenloop/blob/master/config/gyrid.conf)
- Replace /etc/network/interfaces with [this one](https://github.com/ZeusWPI/12urenloop/blob/master/config/interfaces)
- When NTP has run (and so the time is correctly set), run `hwclock -w`
- If the old gyrid code is used, apply [this patch](https://github.com/ZeusWPI/12urenloop/issues/114#issuecomment-206234613)
- Add `popen(["/etc/init.d/bluetooth", "restart"])` na dbus restart
- Verwijder wifi lijn in scanmanager
