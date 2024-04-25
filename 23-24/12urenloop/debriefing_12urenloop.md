---
grand_parent: 23-24
parent: 12urenloop
title: debriefing
---

# 12urenloop 2023-2024

(origineel ingevuld op https://codimd.zeus.gent/ssPUG5EkS_GtE53XRQABuQ?both; na 01/05/2024 eens kijken of dit nog geupdate is, hier syncen en dan deze note verwijderen)

Wat willen we anders doen op volgende edities?

- TV meenemen: die hing nu vast aan de muur met vijzen, maar er waren geen vijzen om die in een staander te steken: zoek deze dus op voorhand
- we hebben wat walkies te kort; het zou nice zijn om wat meer walkies te hebben; dat is ook niet zo superduur (2 voor 40 euro); we kunnen die ook lenen bij DSA
- whiteboard meenemen!
- extra scherm zou nuttig zijn
- clients kunnen allemaal op voorhand klaargemaakt worden
- er zijn spade-connectoren op de meeste batterijen; er is nog 1 batterij waarbij er gewoon bare wires in de moeren zitten -> dit moet nog gefixt worden, hiervoor hebben we kleine heatshink nodig
- er zijn te weinig doppen voor batons, waardoor we geen switchovers gaan kunnen doen met 'snelle' teams
- we zijn pas vrij laat (~20 min voor startschot) begonnen met manualcount op te zetten, waardoor er wat chaos was
- voor manualcount wil je ideaal met twee teams zijn (elk team bestaat uit iemand die luidop zegt welke nummers voorbijlopen, en iemand die dat ingeeft op een tablet)
- spanning-tree heeft ons weer gefucked, dat werkt niet zo goed, dus probeer dat naar volgende events toe te vermijden
- we waren nu wat te laat met stokken brengen naar de startlijn, die mogen zeker een half uur op voorhand al klaar liggen in een doos
- er zijn te weinig micro USB kabels (er zijn er een aantal verloren gegaan op het Arduino-event), dit moet nog bijgekocht worden
- aansteker is heel handig om mee te doen
- de livesite op de ledwall was niet helemaal bevroren nadat de positioner op frozen gezet was:
    - oorzaken:
        - de livesite deed 'optimistic updates' (dus als de position groter is dan 1, dan werd er 1 bij de laps geteld)
        - loxsi had een cache van position-data, die ook werd gestuurd als het scorebord frozen is
        - de livesite bleef oneindig lang extrapoleren aan de hand van de laatste positiedata
    - suggested fixes (meerdere):
        - timeout zetten op hoe lang er mag ge-extrapoleerd worden op bepaalde data
        - de cache leegmaken als het scoreboard frozen is, en niet meer vullen
        - zeker zijn dat er geen positioner data meer in de cache komt als frozen

## Kapot

- er is een 12V naar 9V converter (in witte case, dient voor het autobatterij-voltage om te zetten naar voltage voor de switch) kapot gegaan: die was heel warm en er kwam maar 1V uit. Geen oorzaak gevonden, de switch die eraan hangt is niet kapot. -> mss een fuse ofzo voorzien?
- doppen van de batons zijn kapot gegaan, we hebben er nu te weinig (maar 2x17, dus voor 17 batons)
- er is een kabeltje van een baton-batterij (I) losgekomen van de baton, waardoor we in het begin geen tellingen hadden. Voor we stokken uitdelen, zouden we in het vervolg best kijken dat het ledje knippert, en dat de batons blijven gedetecteerd worden
- er is een kabelconnector tussen autobatterij en converters kapot gegaan; deze zijn echt dun en moeten verstevigd worden -> kan met heatshrink, maar onze heatshrink is op (kan bijgekocht worden op aliexpress)
- er was een baton die als 'herstart' gemarkeerd was in de monitoring (die van HILOK). We hebben een 'trage' switchover gedaan (dus beide lopers in de switchover uitgelegd wat er gaat gebeuren). Uiteindelijk bleek dat het spanbandje op de batterij broos geworden was, waardoor het gebroken was en de batterij soms kort uit de batterijhouder wupte. Gefixt met een nieuw spanbandje.

## batterijvoltages na event

TO DO: kijken om power te saven op raspberry pi (we hebben in de kelder een USB-powermeter): https://blues.com/blog/tips-tricks-optimizing-raspberry-pi-power/

- J (ronny 7): 10.33V **!!!**
- D (ronny 1): 12.29V
- B (ronny 2): 12.34V
- nieuwe batterij Y (ronny 4): 12.37V
- nieuwe batterij Z (ronny 5): 12.43V
- I (ronny 6): 12.56V
- K (ronny 3): 12.71V

J, D, B en Y direct aan de lader gelegd; J aan de nieuwe, goede lader (STREX)

niet gebruikt op het event (gemeten minimum 1 uur na loskoppelen lader):

- C: laadt op tot 12.90V
- G: laadt op tot 10.91V **!!!**
- H: laadt op tot 13.29V