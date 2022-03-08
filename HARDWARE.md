# Hardware

Software is needed to save the data, calculate laps, monitor hiccups, ...

But the counting will never be automated without a good portion of hardware. So here goes...

The hardware consists of batons, containing a Bluetooth LE microcontroller and several stations around the parcours, listening to beacon packets sent by the batons.

## Batons

The batons contain "Adafruit Feather nRF52 Bluefruit LE - nRF52832" development boards. These boards broadcast BLE beacon packets with a configurable power and MAC address.

See (the repo)[https://github.com/12urenloop/baton_firmware/] for instructions on how to flash the microcontrollers.

### Batteries

Lithium ion, 3.7v. About the size of a AA battery. Need to be charged to **?? v** after the event before storage. This is necessary to retain the full capacity of the batteries for further editions.

## Stations

The stations are Raspberry Pi 4 single-board computers that listen for the packets sent by the batons using their built-in Bluetooth chipset.

### Batteries

We use lead acid car batteries. Need to be fully charged after the event before storage. This is necessary to retain the full capacity of the batteries for further editions.
