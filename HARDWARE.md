---
title: Hardware
---

# Hardware

Software is needed to save the data, calculate laps, monitor hiccups, ...

But the counting will never be automated without a good portion of hardware. So here goes...

The hardware consists of batons, containing a Bluetooth LE microcontroller and several stations around the parcours, listening to beacon packets sent by the batons.

## Batons

The batons contain "Adafruit Feather nRF52 Bluefruit LE - nRF52832" development boards. These boards broadcast BLE beacon packets with a configurable power and MAC address.

See [the repo](https://github.com/12urenloop/baton_firmware/) for instructions on how to flash the microcontrollers.

This is how not to attach the rope to the battery:
 ![How not to attach batons](/assets/images/baton_bad.jpg)

This is how you should attach the rope to the battery 
![How to attach batons](/assets/images/baton_good.jpg)


### Batteries

Lithium ion, 3.7v. About the size of a AA battery. Need to be charged to **?? v** after the event before storage. This is necessary to retain the full capacity of the batteries for further editions. The battery is connected via a JST connector to the microcontroller.

## Stations

The stations (also called "Ronny's" by some) are Raspberry Pi 4 single-board computers that listen for the packets sent by the batons using their built-in Bluetooth chipset. The code that runs on them and deploy instructions are in the [Ronny repo](https://github.com/12urenloop/Ronny-the-station-chef).

### Batteries

We use lead acid car batteries. Need to be fully charged after the event before storage. This is necessary to retain the full capacity of the batteries for further editions.

### Converting car battery voltage to useful voltage

There are two voltage converters per station: a buck converter, converting the battery voltage down to a 5V USB port (for the Pi) and a buck/boost converter, converting the battery voltage up or down to 9V for the switch inside the station.

The voltage converters are connected via JST XH connectors to the battery: one connector is connected to the battery, the other to a converter. That way, you can plug and unplug the connector without the risk of getting
the polarity wrong. The lead of the connector connected to the battery is glued to the battery, to prevent stain
on the wire connected to the terminal.

TODO - insert pictures