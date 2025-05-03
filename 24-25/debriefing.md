---
parent: 24-25
title: Debriefing
---

# 12urenloop 2025 - debriefing

## Start
- Hesjes op voorhand controleren zodat we zeker weten dat we alles hebben
- 1 hesje per team rond de baton wikkelen zodat deze gemakkelijker verdeeld kunnen worden aan de start
    - Dit samen met het materiaal van saruman meegeven aan de logistieke zone
    - Als bovenstaande niet gaat, een bak met gaten in waar in 1 gat = 1 team zodat er geen lijst meer nodig is en gewoon per team kan afgeroepen worden
- Voor de start al rond gaan met de hesjes per tent zodat deze daar al klaar liggen

## Telraam
- De websocket client in telraam werd iedere x opnieuw geopend, door thread locking toe te voegen is dit opgelost. We hebben wel de eerste versie moeten aanpassen omdat deze een gesharde lock gebruikte voor alle clients
- De detections waren perongeluk getruncate. Hierdoor moesten we de detections opnieuw clearen en binnentrekken zodat robustlapper verder kon

## Manual-count
- Een gsm die record om achteraf te controleren kan nice zijn in de chaos die er soms heerst
- 2 mensen tikken is echt nodig
- 1 van de 2 ipads kan niet aan manual count (outdated ios)
- Verschillende kleuren hesjes zou nice zijn voor 1-2-3
- Duidelijker communiceren da nr vanachter -> geen lap
- Ipad verliest soms connectie naar backend
- Als backend ofline is kun je niet tikken op een team (enkel getest op ipad, dubbelchecken dat dit kan)
- Nadat de batons zijn gegeven terugkeren want je hebt minstens 4 man nodig in/rond de container voor opstart
- Persoon die drukt herhaalt het nr maakt het makkelijk om te confirmeren dat de gezegde nrs effectief doorkoemen

## Ronny
- Fans/heatsink toevoegen voor warme edities
- Polling sleep verhogen
- Spreader vraagt heel veel van db als er 2 sockets openstaan. Vervangen van gorm door sqlc zodat we terug de macht krijgen tot onze DB queries

## Monitoring
- SNMP monitoring stralers
- team baton ids view neemt switchovers van in de toekomst over waardoor bepaalde monitoring breekt

## Baton
- Meer spanbandjes gelost (R, N)
- Bij sommige batons is de batterij uit de moes geschoven
- 1 baton geherstart maar nog 1u blijven werken
