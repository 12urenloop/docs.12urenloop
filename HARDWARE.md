# Hardware

Software is needed to save the data, calculate laps, monitor hiccups, ...

But the counting will never be automated without a good portion of hardware. So here goes...

The hardware consists of batons, containing a Bluetooth LE microcontroller and several stations around the parcours, listening to beacon packets sent by the batons.

## Batons

The batons contain "Adafruit Feather nRF52 Bluefruit LE - nRF52832" development boards. These boards broadcast BLE beacon packets with a configurable power and MAC address.

## Stations

The stations are Raspberry Pi 4 single-board computers that listen for the packets sent by the batons using their built-in Bluetooth chipset.
