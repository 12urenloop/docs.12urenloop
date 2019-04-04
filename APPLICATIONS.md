# Applications

## Boxxy

- Function: Displays the live score to the public
- Note: Connects to Count Von Count with WebSockets
- URL <https://live.12urenloop.be/>
- Repo: <https://github.com/12urenloop/boxxy>
- Hosted on: urenloop@zeus.ugent.be:2222 (see app/)
- Stack: Node.js - HTML

## Factuur

- Function: Platform to generate/make invoice PDF
- Note: Standallone app
- Note: Check /var/www/factuur.12urenloop.be/ (instead of ~)
- URL <https://12urenloop.be/factuur>
- Repo: <https://github.com/12urenloop/Factuur>
- Hosted on: factuur@12urenloop.be:2222
- Stack: Ruby on Rails

## Saruman

- Function: Platform to book materials and drinks for participating clubs
- Note: Standallone app. Still on the Zeus repo for some reason.
- URL: <https://materiaal.12urenloop.be>
- Repo: <https://github.com/ZeusWPI/Saruman>
- Hosted on: materiaal@12urenloop.be:2222
- Stack: Ruby on Rails

## Count von Count

- Function: System for aggregating runner-detect events from detectors around the track, detecting errors, and propagating this data to Boxxy.
- Note: The beast of burden
- URL: No, this runs locally.
- Repo: <https://github.com/12urenloop/cvc>
- Hosted on: A poor mortal's PC during the event.
- Stack: Haskell

## Site

- Function: It's a website
- Note: You need to update this before the event.
- URL: <https://12urenloop.be>
- Repo: <https://github.com/12urenloop/site>
- Hosted on: urenloop@zeus.ugent.be:2222 (see public/)
- Stack: nanoc

## STROLL

- Function: A collection of shell scripts ment to run on the espressobins during the event. They send data to CVC.
- Note: Test this.
- URL: No.
- Repo: <https://github.com/12urenloop/STROLL>
- Hosted on: All the espressobins
- Stack: Bash

## Logger Proxy

- Function: Log all events coming into CVC and going out of CVC
- Note: This way we don't have to touch CVC code.
- URL: No.
- Repo: <https://github.com/12urenloop/loggerproxy>
- Hosted on: Same machine as CVC (probably)
- Stack: Python

## Manual Count v2

- Function: Backup system for manual counting in the first hours of the event (hopefully)
- Note: Very important this works.
- URL: Some local ip during the event.
- Repo: <https://github.com/12urenloop/manual-count-2>
- Hosted on: Some client in box office.
- Stack: Node.js - Typescript - Vue

## Misc

- Old Manual Count
- Join Site
- Twitter wall
- Old Gyrid code