---
parent: 21-22
title: debriefing 6urenloop
---

# Debriefing 6urenloop

## Changes we want for following events


### Preparation

- Print the inventory list before leaving
- Print a map with the setup on the terrain
- Print inventory list sorted by box for disassembly after event


### Manual count

- bigger manual count UI, "last detected" should be very visible
- the manual count server should be easily exportable
- the manual count server should be restartable (sync with telraam)

## Monitoring

- only show active batons by default (have another dashboard for detailed baton status)

### Hardware

- Use clamps for boxes instead of tape -> 3D-print 'em
- Ensure no boxes are transparent to avoid theft
- Monitor voltage remotely via voltage sensor
- Better weatherproof container for sockets

## Live screen

- For Raspberry Pi clients, check that adapter supplies enough voltage
    - WARNING: the warning is disabled for now (by uninstalling the package), this might lead to really hard to debug issues

## External partners

- Ask for an NS record on a subdomain instead of an A-record, that way we can set our own DNS records (this year, a AAAA-record was set pointing to a UGent server that has no IPv6 support)


### Extra material to bring

- drill
- more blankets
- more female to female ethernet bricks, in case a switch breaks
