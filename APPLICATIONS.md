---
title: Applications
nav_order: 90
---

# Applications

## Currently in use

### Baton firmware

- Function: Code that runs on the baton electronics and shouts BLE beacons with its identifier wherever it goes.
- Repo: <https://github.com/12urenloop/baton_firmware>
- Stack: nRF52832, Arduino platform

### Ronny the station chef

- Function: interpret BLE information and host easy to access HTTP server.
- Repo: <https://github.com/12urenloop/Ronny-the-station-chef>
- Hosted on: The Raspberry Pi's in the stations along the track.
- Stack: ~~Python~~ Go

Consists of two parts:

1. collector: this handles BLE detections and inserts them in a local PostgreSQL database
2. spreader: this exposes a REST and websocket interface where the detections can be requested

### Telraam

- Function: New and hopefully improved application to count laps of the 12urenloop event.
- Note: ~~Shiny new software.~~ The backbone and main database of our system.
- Repo: <https://github.com/12urenloop/telraam>
- Hosted on: client1 @ ZeusContainer
- Stack: Java

### Manual Count v2

- Function: An external lapper for Telraam. Works by manually counting teams through it's web UI. Backup system in case the ronny's fail.
- Note: Very important this works. Also make sure devices (e.g. iPads) work properly. Assign 1 person per 6 teams. Stop when the ronny's have proven themselves for an hour at least.
- Repo: <https://github.com/12urenloop/manual-count-2>
- Hosted on: client1 @ ZeusContainer
- Stack: Node.js - Typescript - Vue

### DeDenker

- Function: External lapper for Telraam which employs HMM machine learning.
- Note: Never the reference lapper, but more lappers can highlight oddities when they give different counts.
- Repo: <https://github.com/12urenloop/DeDenker>
- Hosted on: client1 @ ZeusContainer
- Stack: Python (SKLearn)

### Monitoring

- Function: Get instant feedback of anomalies and easily observe the status of our running services and hardware.
- Repo: <https://github.com/12urenloop/monitoring>
- Hosted on: client2 @ Zeus container
- Stack: docker-compose, Grafana, Prometheus

### Banshee

- Function: Screams at you when monitoring alerts are being ignored.
- Repo: <https://github.com/12urenloop/banshee>
- Hosted on: client2 @ Zeus container
- Stack: Go

### ansible-config

- Function: What deploys all of the above. Provided some initial setup and networking, turns 2 clients and 8 pi's into the “telsysteem”.
- Note: See [Deploying](./DEPLOYING). Anything not deployed (or not todo) should be below.
- Repo: <https://github.com/12urenloop/ansible-config>
- Hosted on: Your laptop @ ZeusContainer
- Stack: Ansible (`(gu|l|n)ix` one day)

### Loxsi

- Function: The Telraam proxy. Runs next to the livesite on an external server. Polls data from telraam via `ssh -R` and makes it available to livesite via websockets.
- URL: <https://loxsi.12urenloop.be/>
- Repo: <https://github.com/12urenloop/loxsi>
- Hosted on: loxsi@12urenloop.be:2222 (Zeus asimov)
- Stack: Python (FASTApi)

### TARGET

- Function: The new livesite, with prediction of runner locations best-effort prediction
- Note: Always stress that these predictions are not what determines lap count. Updating the count happens later and is always reviewed manually and adjusted if the system made a mistake.
- Repo: <https://github.com/12urenloop/TARGET>
- URL: <https://live.12urenloop.be/>
- Hosted on: live@12urenloop.be:2222 (Zeus asimov)
- Stack: Vue.js

### Saruman

- Function: Platform to book materials and drinks for participating clubs
- Note: Standalone app, not part of the telsysteem.
- URL: <https://materiaal.12urenloop.be>
- Repo: <https://github.com/ZeusWPI/Saruman>
- Hosted on: materiaal@12urenloop.be:2222 (Zeus asimov)
- Stack: Ruby on Rails

### Factuur

- Function: Platform to generate/make invoice PDF
- Note: Standalone app, not part of the telsysteem.
- Note: Check /var/www/factuur.12urenloop.be/ (instead of ~)
- URL <https://12urenloop.be/factuur>
- Repo: <https://github.com/12urenloop/Factuur>
- Hosted on: factuur@12urenloop.be:2222 (Zeus asimov)
- Stack: Ruby on Rails

## Prototypes

### Lapocalypse3000

- Function: Next gen runner-tracking system employing UWB technology. In prototyping stage. Could eventually replace the BLE system and provide accurate real-time positions.
- Repo: <https://github.com/12urenloop/Lapocalypse3000>

## Development tools

### REPLAY

- Function: Replays station data from previous events for development purposes.
- Repo: <https://github.com/12urenloop/REPLAY>
- Stack: Python

### SIMSALABIM

- Function: Simulates runner behaviour as fake station data for development purposes.
- Repo: <https://github.com/12urenloop/SIMSALABIM>
- Stack: Godot

## Archive

These are applications (in no specific order) that were used in or made for previous editions but are now deprecated or out of use.

### Site

- Function: It's a website
- Note: You need to update this before the event.
- URL: <https://12urenloop.be>
- Repo: <https://github.com/12urenloop/site>
- Hosted on: urenloop@zeus.ugent.be:2222 (see public/)
- Stack: nanoc

### Telraam UI

- Function: CRUD-dashboard for Telraam
- Repo: <https://github.com/12urenloop/telraam-ui>
- Hosted on: locally, on your computer
- Stack: Node.js - React

### TelraamSim

- Function: Simulation of the event to test Telraam without the actual hardware
- Note: Very usefull to test the software in a development setup
- URL: Runs as desktop application on your PC
- Repo: <https://github.com/12urenloop/telraamsim>
- Stack: Godot with CSharp

### Boxxy

- Function: Displays the live score to the public
- Note: Connects to Count Von Count with WebSockets
- URL <https://live.12urenloop.be/>
- Repo: <https://github.com/12urenloop/boxxy>
- Hosted on: urenloop@zeus.ugent.be:2222 (see app/)
- Stack: Node.js - HTML

### Count von Count

- Function: System for aggregating runner-detect events from detectors around the track, detecting errors, and propagating this data to Boxxy. Has been replaced by Telraam
- Note: The beast of burden
- URL: No, this runs locally.
- Repo: <https://github.com/12urenloop/cvc>
- Hosted on: A poor mortal's PC during the event.
- Stack: Haskell

### STROLL

- Function: A collection of shell scripts ment to run on the espressobins during the event. They send data to CVC.
- Note: Test this.
- URL: No.
- Repo: <https://github.com/12urenloop/STROLL>
- Hosted on: All the espressobins
- Stack: Bash

### Logger Proxy

- Function: Log all events coming into CVC and going out of CVC
- Note: This way we don't have to touch CVC code.
- URL: No.
- Repo: <https://github.com/12urenloop/loggerproxy>
- Hosted on: Same machine as CVC (probably)
- Stack: Python

### Misc

- Old Manual Count
- Join Site
- Twitter wall
- Old Gyrid code
