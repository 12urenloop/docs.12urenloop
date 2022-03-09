# Configuring a pi to run Ronny for 12urenloop

1. Download and copy the raspbian lite .img [file](https://downloads.raspberrypi.org/raspios_lite_arm64/images/raspios_lite_arm64-2022-01-28/2022-01-28-raspios-bullseye-arm64-lite.zip) to an sd card
2. Mount the root partition and edit `/etc/hostname` to the desired hostname
3. Mount the boot partition and create a file named `ssh` (`touch ssh`) to enable ssh for one time
4. Insert the sd card and boot the pi
5. Ssh into the pi and run `sudo raspi-config`
	- Change the password to `zeusisdemax`
	- Enable ssh
	- Enable wait for network at boot
	- Set timezone to `Europe/Brussels`
	- Expand the filesystem
	- Quit (don't reboot)
6. Edit `/etc/systemd/timesyncd.conf`
	- Change `#NTP=` to `NTP=ntp.ugent.be`
7. Run `sudo systemctl enable systemd-time-wait-sync.service` to allow waiting for the NTP server
8. Reboot the pi
9. Install git and pip on the pi
10. Run `sudo -i && cd / && git clone https://github.com/12urenloop/Ronny-the-station-chef.git && cd Ronny-the-station-chef && pip install -r requirements.txt` download Ronny and install the requirements
11. Create `/etc/systemd/system/ronny.service`,
	`/etc/systemd/system/station.service`,
	`/usr/local/bin/ronny`,
	and `/usr/local/bin/station`
12. In `/etc/systemd/system/ronny.service` paste
```service
[Unit]
Description=Ronny, collects detections into a database
Requires=network.target
Requires=time-sync.target
After=network.target
After=time-sync.target

[Service]
Type=simple
Restart=always
User=root
ExecStart=ronny

[Install]
WantedBy=multi-user.target
```

In `/usr/local/bin/ronny` paste
```sh
#!/bin/bash

cd /Ronny-the-station-chef
/usr/bin/env python ronny.py
```

In `/etc/systemd/system/station.service` paste
```service
[Unit]
Description=Station, serves detections from the database
Requires=network.target
Requires=time-sync.target
After=network.target
After=time-sync.target

[Service]
Type=simple
Restart=always
User=root
ExecStart=station

[Install]
WantedBy=multi-user.target
```

In `/usr/local/bin/station` paste
```sh
#!/bin/bash

cd /Ronny-the-station-chef
uvicorn station:app --host 0.0.0.0 --reload
```

Then enable the executables with `sudo chmod +x /usr/local/bin/ronny && sudo chmod +x /usr/local/bin/station`
and enable the services with `sudo systemctl enable ronny.service && sudo systemctl enable station.service`

13. Restart the pi or run `sudo systemctl start ronny && sudo systemctl start station` to start the services
