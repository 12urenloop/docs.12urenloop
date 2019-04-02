# Espressobins

## Setup

Download ubuntu 16.04 [hier zo](http://espressobin.net/tech-spec/) en installeer hem volgens de instructies [hier zo](http://wiki.espressobin.net/tiki-index.php?page=Boot+from+removable+storage+-+Ubuntu#Preparing_removable_media_2).

- smijt een ethernetkabel in de middelste poort en verbind het ander eind met een netwerk waar `dhcp` op draait
- voeg een wachtwoord toe met `passwd` (default "tettentetten")

### Networking setup [outdated voor armbian]

Eerst en vooral moet er bij boot een bridge aangemaakt worden. Voeg de volgende commandos toe aan `/etc/rc.local`/.

```shell
# add a bridge called br0 to the interfaces
brctl addbr br0
```

Copy & paste de volgende config naar `/etc/network/interfaces` en pas de config toe met `/etc/init.d/networking restart` (of een reboot).

```shell
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

# loopback
auto lo
iface lo inet loopback

# configure lan0 so it correctly sets up on boot
auto lan0
allow-hotplug lan0
iface lan0 inet manual
        pre-up ip link set eth0 up

# configure lan1 so it correctly sets up on boot
auto lan1
allow-hotplug lan1
iface lan1 inet manual
        pre-up ip link set eth0 up

# configure the bridge
auto br0
iface br0 inet static
        address xxx.xxx.xxx.xxx
        netmask 255.255.255.0
        gateway xxx.xxx.xxx.xxx

        bridge_ports lan0 lan1
```

### SSH setup

- Na het succesvol installeren van `openssh`, pas de lijn `PermitRootLogin without-password` aan naar `PermitRootLogin yes` in `/etc/ssh/sshd_config`.
- Herstart de ssh service met `sudo service ssh restart`.
- Kopieer uw lokale key naar de espresso bin met `ssh-copy-id root@<IP>`.