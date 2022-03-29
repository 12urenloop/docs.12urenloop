# Applications

## Currently in use

### Telraam

- Function: New and hopefully improved application to count laps of the 12urenloop event.
- Note: Shiny new software. The backbone and main database of our system.
- URL: No, this runs locally.
- Repo: <https://github.com/12urenloop/telraam>
- Hosted on: Probably a poor mortal's PC during the event, preferably a dedicated server.
- Stack: Java

### TelraamSim

- Function: Simulation of the event to test Telraam without the actual hardware
- Note: Very usefull to test the software in a development setup
- URL: Runs as desktop application on your PC
- Repo: <https://github.com/12urenloop/telraamsim>
- Stack: Godot with CSharp

### Telraam UI

- Function: CRUD-dashboard for Telraam
- Repo: <https://github.com/12urenloop/telraam-ui>
- Hosted on: locally, on your computer
- Stack: Node.js - React

### Manual Count v2

- Function: Backup system for manual counting in the first hours of the event (hopefully)
- Note: Very important this works.
- URL: Some local ip during the event.
- Repo: <https://github.com/12urenloop/manual-count-2>
- Hosted on: Some client in box office.
- Stack: Node.js - Typescript - Vue

### Ronny the station chef

- Function: interpret BTLE information and host easy to access HTTP server.
- Repo: <https://github.com/12urenloop/Ronny-the-station-chef>
- URL: <ip per station>
- Stack: Python
- usage: `GET <ip>/detection/<last_id>`
- returns
```typescript
{
    'detections':
        {'id': number, 'mac': string, 'rssi': number, 'battery': number, 'uptime_ms': number, 'detection_timestamp': number}[],
    'station_id': string
}
```
Consists of two parts: 
1. ronny.py: this handles BTLE detections and inserts them in a database
2. station.py: this exposes a web interface where the detections can be requested


### Loxsi
- Function: A simple server to offload the load of the public livesite to the cloud. Polls data from telraam and makes it available to livesite via websockets.
- Repo: <https://github.com/12urenloop/loxsi>
- Hosted on: the 12urenloop server hosted by the UGent
- Stack: Python, FASTApi

### Monitoring
- Function: Get instant feedback of anomalies and easily observe the status of our running services and hardware.
- Repo: <https://github.com/12urenloop/monitoring>
- Hosted on: Some client in box office.
- Stack: docker-compose, Grafana, Prometheus


### Saruman

- Function: Platform to book materials and drinks for participating clubs
- Note: Standallone app. Still on the Zeus repo for some reason.
- URL: <https://materiaal.12urenloop.be>
- Repo: <https://github.com/ZeusWPI/Saruman>
- Hosted on: materiaal@12urenloop.be:2222
- Stack: Ruby on Rails

### Site

- Function: It's a website
- Note: You need to update this before the event.
- URL: <https://12urenloop.be>
- Repo: <https://github.com/12urenloop/site>
- Hosted on: urenloop@zeus.ugent.be:2222 (see public/)
- Stack: nanoc

### Factuur

- Function: Platform to generate/make invoice PDF
- Note: Standalone app
- Note: Check /var/www/factuur.12urenloop.be/ (instead of ~)
- URL <https://12urenloop.be/factuur>
- Repo: <https://github.com/12urenloop/Factuur>
- Hosted on: factuur@12urenloop.be:2222
- Stack: Ruby on Rails

## Archive

These are applications (in no specific order) that were used in or made for previous editions but are now deprecated or out of use.

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
