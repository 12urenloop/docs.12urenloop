---
title: Technologiestudie
parent: 19-20
---

# Telhardware

## Batons met GPS
De batons zijn dan heel actief en nogal failure-prone.

Dit is wat de VUB doet volgens http://be-here.be/wp-content/uploads/2019/05/20190515_Het-Nieuwsblad-Regionaal-Brussel-Noordrand_p-5.pdf. Voordeel is dat het mogelijk is te weten waar elke baton is, ook als er niet gelopen wordt.

## Nieuwe batons met Bluetooth
https://www.openbeacon.org/ – https://github.com/meriac/openbeacon-ng
Detectiestations zien er beter uit dan de Bluetooth-stations die we nu hebben, maar dit heeft nog steeds last van gelijkaardige problemen.

## Twee of meer krachtige base stations
Schets van 12UL-parcours (● = base station):
```
      _______________________________
N    |                               \
▼    |                                \
     |                                 |
     |_________________________________|
y        ●                         ●
└╴x
```

Met twee krachtige stations is het theoretisch mogelijk om met triangulatie goed genoeg te bepalen waar elke baton is. Je kan veronderstellen dat y>0 omdat er hekkens staan rond het parcours, dan is er per baton op elk ogenblik telkens maar één unieke oplossing voor het triangulatieprobleem.

Na wat meer opzoekwerk blijkt dat dit **met RFID allicht niet mogelijk** is. Een radioamateur heeft zelf 65 meter gehaald en denkt dat er meer uit te halen valt, maar het is directioneel en line-of-sight: https://www.youtube.com/watch?v=BR-JXDdzCko. Voor onze usecase zou de range iets van 120m moeten zijn, met obstakels. Da's niet haalbaar.

Om dit mogelijk te maken moet dus gekeken worden naar andere technologieën met actieve beacons (RFID is passief). LoRa zit op dezelfde bandbreedte als RFID UHF en heeft een zeer grote range: meerdere kilometers. **Verder te onderzoeken.**

## RFID met twee of meer base stations
Dit is wat klassieke race-timing-systemen doen: passieve RFID-beacons, van elk beacon wordt het ID geassocieerd met een loper. Er is een guide voor exact dit: https://www.atlasrfidstore.com/building-your-own-rfid-race-timing-system/

Schets van 12UL-parcours (▃ = matje):
```
      ___________________________▃___
N    |                               \
▼    |                                \
     |                                 |
     |___▃_____________________________|
```

Schets van 12UL-parcours (● = base station met antenne):
```
      _______________________________ ●
N    |                               \
▼    |                                \
     |                                 |
     |_________________________________|
         ●
```

Als antenne worden op professionele loopwedstrijden matjes gebruikt, maar die zijn wel schijteduur (grootteorde €500 per stuk). Life hack: een koperkabel van dezelfde lengte kan misschien hetzelfde doen.

Twee antennes langs het parcours met een range van pakweg 5 meter zijn bijna equivalent aan de matjes. Meer base stations of matjes kunnen redundantie voorzien.

Met deze variant kunnen we dan wel niet fancy kijken waar iedereen op elk moment is.

### Frequentie
Er moet gekeken worden om in de UHF-bandbreedte (433/860MHz) te werken. De bandbreedte kan genoeg data versturen om veel lopers tegelijkertijd te tracken. HF bandbreedte werkt ook, maar heeft minder range: de ruimte waarin een loper gedetecteerd kan worden is dan kleiner; en kan ook minder data versturen: dus minder lopers tegelijk detecteren binnen die ruimte.

### Stations
Dit zal het duurste onderdeel zijn van gans de setup als er gekozen wordt voor de klassieke vorm van race tracking (passieve beacons + actieve stations).

#### Dedicated lezer per station
Elk station moet naast de RFID-lezer ook een computer hebben die de data doorstuurt naar het centrale telsysteem.

Enkele mogelijkheden:

* Arduino met ethernetpoort. Pluspunt: embedded, dus start direct op; de RFID-lezer die we vonden is bruikbaar als Arduino-shield, gemakkelijk in elkaar te steken dus
* Raspberry Pi. Pluspunt: euh
* ESPRESSObin. Pluspunt: hebben we al

De stations programmeren we misschien best in C? Het algoritme is waarschijnlijk sowieso bijna portable tussen Pi's, Arduino's en ESPRESSObins.

#### Eén lezer met meerdere antennes aan
Met een coax-kabel kan de antenne vrij ver van de RFID-lezer-hardware staan. Zo kan één RFID-lezer met meerdere antennepoorten volstaan. Da's dan wel een single point of failure. De RFID-lezers met meerdere antennepoorten die we vonden zijn wel duur. ($1300) Misschien doen die dingen meer, zoals al timings berekenen (maar we willen zelf ook wat programmeren hé).

### Concrete productjes

* Tags:         $1.95 voor 5 https://www.sparkfun.com/products/14147 https://www.sparkfun.com/products/14151
* RFID-lezer: $224.95 voor 1 https://www.sparkfun.com/products/14066 https://www.antratek.be/simultaneous-uhf-rfid-reader-m6e-nano
* Antenne:     $37.95 voor 1 https://www.sparkfun.com/products/14131
* Arduino:    ~€40

Totaal voor 30 batons en 2 stations met ESPRESSObins: $537.50 = €480
Totaal voor 30 batons en 2 stations met Arduino's: €480 + €80 = €560

Deze RFID-lezer kan 120 tags per seconde simultaan lezen, da's goed. Volgens de comments op de productpagina is de range in combinatie met de vermelde antenne 4 à 5 meter.

# Software

## Count von Count
Count von Count is het "brein" van het telsysteem: het aggregeert de readings van de stations en bepaalt aan de hand daarvan de scores.

To rewrite or not to rewrite? Om het met een quote te zeggen:

> Count von Count is geschreven in Haskell zoals je Haskell moet schrijven. Daarom begrijpt niemand het.
> –[Flynn](https://mattermore.zeus.gent/quotes.html#2019-08-08_22:07:43)

Java vindt misschien niet iedereen zo leuk, maar iedereen kan het wel en dat gaat nog jaren zo blijven.

## Filosofie
Niet te veel dingen doen "omdat het kan", maar focussen op de vereisten. Als het simpeler kan dan "alle mogelijkheden in overweging nemen" zoals Count von Count momenteel doet, is dat misschien beter. Zorg wel dat het systeem overweg kan met randgevallen.
