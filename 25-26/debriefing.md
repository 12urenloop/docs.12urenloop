---
parent: 25-26
title: Debriefing 12urenloop 2026
---

# Debriefing 12urenloop 2026

## Preparations

### Software

- We should test the whole setup beforehand (at the S9)
    - Putting everything together should be much faster now with the new ansible playbooks

- ansible-config repo improvements:
    - Manual flashing guide for clients/stations (now on docs.12urenloop.be "deploying").
    - More playbooks: (some were only made during buildup)
        - clients/stations init
        - stations:
            - ronny (was already there, fixed go download 403)
            - uwb
        - client1:
            - telraam
            - loxsi tunnel
            - telraam-push-db-dumps.sh script/service
            - manual-count-2
            - dedenker
        - client2:
            - telraam replica
            - monitoring
    - What's missing?
        - Telraam credentials need to be manually set in src
        - Telraam needs to be started manually in tmux for now
        - Manual count needs multiple source code edits to get it out of localhost development mode
        - ssh keys generation & pub key copying for client1 <-> client2 sync
        - Loxsi (asimov)
        - TARGET (asimov)

- docs.12urenloop.be improvements:
    - Update APPLICATIONS page, was last touched 4 years ago
        - Add Baton firmware
        - Add Banshee
        - Add DeDenker
        - Add SIMSALABIM
        - Remove ronny python instructions, mention it's go now
        - Add ansible-config
        - Add TARGET
        - Add Loxsi
        - Add REPLAY
        - Add Lapocalypse3000
    - Add DEPLOYING pages

- Network
    - [ ] TODO: Make sure router documentation is up to date

- Monitoring
    - Flynn has nice software called NSV (Network State Visualiser) that shows the status of hosts and plays a sound when a host is down
    - battery monitoring for stations (on a stations overview dashboard) could be nice perhaps
    - sort grafana dashboards in folders
    - audible alert for grafana alert rules
        - banshee is only for prometheus alerts apparently

- manual-count-2
    - Took a long time to get working
        - very poorly documented
        - Build instructions talk about yarn/npm but only pnpm files exist
        - Suggested scripts don't exist, build fails
        - Only local development mode worked
            - Needed patches so the frontend doesn't try to send to localhost
    - css is broken (it should have nice colours to indicate time since last lap but it doesn't)
        - Heard after the event that there was a refactor and update last year, and that introduced this issue. This wasn't documented anywhere (debriefing/docs/readme). That would also explain the weird build issues.
    - could use a new frontend
    - or maybe make a whole new manualcount
- Telraam
    - maybe set the default for the time column in the batonswitchover table to current time

- Telraam-UI
    - finalise, test and setup and use telraam-ui (apparently it works properly now) (tnx @flynn)
    - overview for which batons are linked to which teams, with name and ids for batons and teams
        - we have to cross-reference a bunch of db tables now which is Annoying
        - could use grafana for this as well

- Loxsi
    - Docs could use some love:
        - [ ] TODO: document how to use
        - [ ] TODO: document what the podium buttons do
        - [ ] TODO: mention that --build is needed on every config change
    - E.g.:
        - enable:
            ```
            ssh to root@asimov.zeus.ugent.be:2222
            machinectl shell loxsi@
            cd ~/loxsi
            docker compose up -d --build
            ```
        - login: go to `https://loxsi.12urenloop.be/admin`, username/password is in `~/loxsi/config.yml`

- TARGET
    - Missing some documentation:
        - how to configure team images
        - how to configure track image
        - how to configure station coordinates
        - [ ] TODO: make issues
    - had to be configured through editing `App.vue`
        - [ ] TODO: make issue

- Other stuff
    - reverse proxy for the web interfaces (with hostnames) (so we don't have to remember and enter ips and ports)
    - don't use Xfce!!! KDE was pretty nice imo _(i == saturn)_
        - would download twice over mobile data again _- jnms_

### Hardware

- Nieuw materiaal
    - RPi heatsinks!
    - Baton organizer (tnx @hcney)

## Buildup 27/04

- Abdij was gesloten
    - starlink
        - Werkte, maar had een hard limit van 36GiB totale download.
        - Enkel op showday als backup uplink gebruiken.
    - 4G
        - @jnms z'n gsm op 4G met warnings/limiet vanaf 30-50GiB
        - usb-c ethernet dongle ethernet, uit het raam gehangen
        - 10 GiB gebruikt tot dinsdagmiddag, incl. 2x ubiquiti "selfhosted" en 2x KDE want Xfce bleef het scherm automatisch locken

## Buildup 28/04

- Abdij
    - Tijd met de hoogtewerker was kostbaar voor crew.
        - Slechte kopjes
    - Verkeerde PoE injector(s?) gekregen van SKO, waren 48V.
    - Stralers werken enkel op 24 PoE met 0.5A.
        - Mysterie waarom
        - Initieel 100Mbit/s PoE.
        - Net voor de abdij sloot nog kunnen vervangen naar 1 Gbit/s (thanks @nutty).
            - We konden via bewaking ook al binnen woensdag vanaf 7u in de ochtend.

- uwb tests zijn gelukt
    - Software side was een ansible playbook, deployed op 3 ronnys in een bocht

## Showday 29/04

### Changes

- Manual count
    - Uit debriefing 12ul 2025 geleerd:
        - 2 mensen met touch laptops (tnx @caturn @robinp) assigned
        - de nieuwste iPad (met Robbe&Rien als achtergrond) toch opgezet als fallback, werkt nog
        - 1 persoon die nummers afroept
        - op stoelen op het dak van de container
        - 1u lang onafhankelijk, geen enkele fout :O

- telraam_push_db_dumps script stopped making dumps halfway through the day, we didn't notice
    - this was after moving systemd `StartLimitIntervalSec=0` to the `[Unit]` section
    - need monitoring of systemd services
        - [ ] TODO: make issue

- Ontdekt dat SLapper praktisch even goed werkt als RobustLapper
    - Stond aan by default
    - Is een 2de licht verschillende RobustLapper implementatie
    - Moest enkel in Grafana toegevoegd worden
    - Handig als een extra referentie, naast DeDenker

- Baton organizer by @hcney ging geweldig goed

### Other remarks

- Baton switchovers:
    - Geen echt nodig gehad
    - Enkel gedaan zo dat de nieuwkomers het onder de knie krijgen

- Alles in ansible maakte het makkelijk om patches te doen

### Wat is er gefaald?

- Netwerk:
    - kabel tussen ronny 3 en 4.
        - slechte kabel. In het vervolg deftige CAT6 gebruiken.
    - slechte patch kabel in ronny 5 tussen pi en switch
    - Ethernet kopjes zijn slecht.
        - best nieuwe aankopen
    - Kijk in het vervolg bij het opzetten van de ronnys dat elke connectie aan 1Gbit gaat (groen lampje en NIET oranje)

- SD slot van Ronny04 (waarschijnlijk door iemand die niet weet dat de SD kaart eruit moet voor je de Pi uit de case krijgt)

- RobustLapper heeft een 8-tal rondjes niet geteld (sommige tijdens een gedeeltelijke outage), is binnen de 5 minuten gedetecteerd en gecorrigeerd geweest

- CSS van Manualcount was broken

- Loxsi podium was weg de dag na
    - TODO: test op voorhand en documenteer

## Teardown 30/04

- Merci aan @tyboro @arnoutdp @alexbot
- Whiteboard buiten vergeten... oops... (tnx @alexbot om die naar de kelder te dragen)
