# 12urenloop documentation

This repo should help you give an overview of things that exist in relation to organizing the yearly 12urenloop and setting up the counting system.

## Resources

Things that exist that might help you.

- GitHub Organisation <https://github.com/12urenloop>.
- 12urenloop MM channel <https://mattermost.zeus.gent/zeus/channels/12urenloop>.
- Notion Wiki (2019) <https://www.notion.so/zeus12ul/12urenloop-b5f12f293bb34eb69f355d919a26a66d>.
- 12urenloop Slack channel (for when you need prehistoric stuff) <https://zeuswpi.slack.com/messages/C02SAQ136/>.
- Docs in CVC (old track schematics, mac addresses) <https://github.com/12urenloop/cvc/tree/master/doc>.
- **This repo**.

## Applications

### Boxxy

- Function: Displays the live score to the public
- Note: Connects to Count Von Count with WebSockets
- URL <https://live.12urenloop.be/>
- Repo: <https://github.com/12urenloop/boxxy>
- Hosted on: urenloop@zeus.ugent.be:2222 (see app/)
- Stack: Node.js - HTML

### Factuur

- Function: Platform to generate/make invoice PDF
- Note: Standallone app
- URL <https://12urenloop.be/factuur>
- Repo: <https://github.com/12urenloop/Factuur>
- Hosted on: factuur@12urenloop.be:2222
- Stack: Ruby on Rails

### Saruman

- Function: Platform to book materials and drinks for participating clubs
- Note: Standallone app. Still on the Zeus repo for some reason.
- URL: <https://materiaal.12urenloop.be>
- Repo: <https://github.com/ZeusWPI/Saruman>
- Hosted on: materiaal@12urenloop.be:2222
- Stack: Ruby on Rails

### Count von Count

- Function: System for aggregating runner-detect events from detectors around the track, detecting errors, and propagating this data to Boxxy.
- Note: The beast of burden
- URL: No, this runs locally.
- Repo: <https://github.com/12urenloop/cvc>
- Hosted on: A poor mortal's PC during the event.
- Stack: Haskell

### Site

- Function: It's a website
- Note: You need to update this before the event.
- URL: <12urenloop.be>
- Repo: <https://github.com/12urenloop/site>
- Hosted on: urenloop@zeus.ugent.be:2222 (see public/)
- Stack: nanoc

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

### Manual Count v2

- Function: Backup system for manual counting in the first hours of the event (hopefully)
- Note: Very important this works.
- URL: Some local ip during the event.
- Repo: <https://github.com/12urenloop/manual-count-2>
- Hosted on: Some client in box office.
- Stack: Node.js - Typescript - Vue

### Misc

- Old Manual Count
- Join Site
- Twitter wall
- Old Gyrid code

## Materials

Relevant things that Zeus has (or once had) (and you should probably bring):

- Clients / Desktops (for running CVC, Manual Count ...)
- Networking gear
  - Long cables (if note, buy some, you need at least 500m)
  - Short cables
  - Cable tester
  - 2 routers
  - Switches
  - Big switches
- AA Batteries (you'll want lot's)
- Screens
- Gyrids (5)
- Bluetooth sticks (6)
- Espressobins (5)
- RF transmitters (10)
- RF receivers (10)
- USB-C / Micro USB cables
- Battons (+- 16)
  - Tubes
  - Mousse
  - Battery holders
  - Bluetooth senders
- Car batteries (6)
- Big plastic containers (5) (with eyes (2 (* . *)))
- Ethernet to USB converters
- Access point
- Club Mate

If you need more stuff, ask these people:

- Student KickOff. These people can lend you:
  - Switches
  - Routers
  - Netwerk Beamer
  - Camera's
- 12urenloop org (of course)
  - Funding
  - Spanbandjes
  - Gaffa tape
  - Network cables