---
parent: 22-23 6urenloop
---

# 6urenloop 2022-2023

## Verloop

- Dag voordien: al het materiaal ingeladen in gelabelde dozen (zie ook inventaris_6urenloop.md), en dan in 5 winkelkarren zodat die makkelijk in te laden zijn
- 08:30: afgesproken in de kelder, dan al het materiaal ingeladen in de camionet
- 09:06: vertrokken vanaf de Zeuskelder met de 2 auto's naar Brugge
- 09:58: eerste auto toegekomen op t'Zand, tweede auto met materiaal kwam 10 minuten later ook toe
- 10:54: we waren bezig met het netwerk in de Zeus-tent op te zetten, er was nog geen stroom voorzien door de organisatie
- 11:13: we waren bezig Loxsi en livesite op te zetten, er was toen netwerk (in de tent) en stroom
- 11:43: auto is opgesteld langs de binnenkant van het parcours, met goed uitzicht op de lopers
- 11:55: we hadden beslist om de stations langs de binnenkant van het circuit te zetten: er was geen truss en we wilden liever geen kabel over het terrein spannen(later komen we daar nog op terug omdat de detectieradius van stations dan te veel overlappen)
- 15:11: alle stations zijn online, nu langs de buitenkant
- 15:14: Telraam en manualcount zijn gedeployed, teams zijn toegevoegd op livesite (foto en naam), de tunnel naar asimov werkt
- 16:31: we zijn bezig een overzicht aan het maken van teams/hesjesnummers voor de organisatie en dit aan het configureren in Telraam
- 17:00: er zijn GPS traces van de binnen en buitenkant van het parcours gemaakt, met daarop de stations, de start, de ingang en de Zeustent
- 18:03: startschot, we beginnen in manualcount. We zien dat de RobustLapper veel te veel rondjes telt, dit komt omdat er nog veel overlap is tussen stations. We verhogen het aantal stations die een stok mag teruggaan om niet als 'veel stations geskipt' beschouwd te worden van 2 naar 3
- 18:30: we schakelen over van manualcount naar de baum-welch lapper: het verschil tussen manualcount en BW is max 1 rondje, het verschil tussen robust en BW is ook max 1 rondje
- 22:30: het dopje van 1 van de batons is er blijkbaar al de hele avond af aan het vallen. We doen een (niet helemaal, maar toch grotendeels) smooth swithover naar een nieuwe baton
- 23:00: we bevriezen het scorebord
- 23:30 ongeveer: vesalius komt naar ons met de melding dat hun baton al even kapot is, en effectief, de powerdraden zijn door, ze zeggen doordat het touwtje is blijven haperen aan een jas. We doen een batonswitchover. Het metaal van de batterijhouder is ook vervormd. De chip in de baton heeft hex nummer 06. VREEMD: we hebben niet gedetecteerd in de monitoring dat die baton kapot is.
- 00:00: Het event stopt, we beginnen met de afbraak. We hebben op voorhand 1 persoon toegewezen per stationbak, die is verantwoordelijk om die direct op te halen nadat de lopers gestopt zijn met lopen. De organisatie heeft bij de stop van het event omgeroepen dat de lopers hun batons en hesjes moeten indienen, wij halen die daar op en controleren dat we alle batons terughebben. Daarna halen we de ethernetkabels van de hekkens (en de tape ook, zo'n verhuurbedrijven vinden dat niet leuk als er nog tape aan hekkens hangt). We steken alles in de juiste bak (aan de hand van de afbraakchecklist.odt, die via de scriptjes in 21-22 is opgesteld aan de hand van de inventaris). We vinken items af als ze in de bak zitten, en vinken bakken af als ze in de auto zitten.
- 00:59: de afbraak is klaar. Gezien het veel vroeger is en we een pak minder dood zijn dan vorig jaar (mogelijks omdat we niet de hele dag in de kou hebben moeten zitten), beslissen we om direct al terug te gaan naar Gent, zonder overnachting in Brugge.

(kapotte HW zit in serial kabel doos)


## Nota's voor volgende editie

Ter info: deze lijst is opgesteld door mij (Jasper), via informatie van mezelf en andere mensen; dit is dus nog niet besproken of de voorgestelde oplossingen allemaal de beste aanpak zijn. Er zijn veel nota's, maar dat wil niet zeggen dat het een slechte editie was, integendeel: als je de nota's bekijkt, zal je zien dat dat vooral kleine quality of life issues zijn.

- er was geen truss, waardoor we netwerkkabels door een kabelgoot hebben moeten steken. Mogelijke oplossingen:
    - wifi-stralers lenen van SKO. Nadeel: dat heeft PoE nodig, dat hebben we niet in de stationboxen
    - zelf een lange paal meedoen om kabel over het terrein te spannen (bvb vishengel Jasper of een lange plank ofzo)
    - ...
- Warmtestralers waren super nice, ook klein elektrisch kacheltje was nuttig in de auto
- We hadden nu net te weinig walkies (6 gekregen van de orga van 6urenloop), volgend jaar mss 8, 12 of 16 lenen van DSA
- De walkies die we hebben, van DSA, Jasper en de 6urenloop-organisatie, zijn niet compatibel. Best een software defined radio (we hebben dat in de kelder) meedoen om configuratie van walkies te kunnen zien en evt veranderen bij walkies waar we dat mogen.
- De distanceFromStart bij stations is heel cruciaal bij de RobustLapper: als die allemaal op hetzelfde staan, dan werkt die lapper niet (de stations worden op basis van die distanceFromStart gesorteerd)
- stations langs de buitenkant van de piste zetten, anders heb je te veel overlap in je detecties, waardoor je algoritmes slechter presteren
- We zouden graag "undo"-functionaliteit hebben in manualcount
- In manualcount is er een bug waardoor het (met meerdere toestellen?) mogelijk is dat er rondjes van 0 seconden zijn. Racecondition? Best verifieren in de Telraamdatabase
- Als het regent en een teldoos moet open, dan regent het daarin. Naar volgend jaar dus een paraplu meedoen.
- We willen een lock-button op manualcount
- Meer snacks voor tijdens de dag => ingrediënten en kookmateriaal meenemen om pannenkoeken te bakken, er is toch tijd genoeg :D
- Meer Robbe
- Kabels niet buiten laten liggen, dat gaat daarvan kapot
- De livesite zou by default moeten een error geven als het start en er geen loxsi URL geconfigureerd is: nu is er een default om localhost te gebruiken, waardoor je dat dan moet debuggen als je dat vergeet in te stellen
- Hesjesnummers en IDs van teams is momenteel hetzelfde in Telraam, dat is niet praktisch als je de teams wil configureren, zeker als niet alle hesjes toegekend zijn: https://github.com/12urenloop/Telraam/issues/101
- TODO documentatie van onze printer en hoe je dat opzet in Linux op de zeuswiki zetten
- er had iemand die vaag betrokken was bij de organisatie een stekkerblok genomen om te gebruiken. We hebben dat gezien en die direct teruggevraagd, maar een betere afscherming zou zeker geen kwaad kunnen
- het is nu heel makkelijk om per ongeluk op het parcours te lopen doordat er een gat is tussen de auto en het parcours, dit dus best afzetten met plastic lint ofzo
- een beamer zou wel nice zijn om de status te projecteren
- Een team was gestopt met lopen (erasmus), en we hadden dat pas door na een half uur. Monitoring voor de tijd sinds de laatste volledige lap zou nice zijn
- Switchover protocol in geval van kapotte stok beter uitwerken
- er zijn geen banshee alerts voor een baton die lang niet gezien is/lange laptimes/... en de monitoring was kapot. Mss toch eens kijken naar testen?
- Meer displayport naar HDMI adapters kopen: dan zouden we 2 schermen per client kunnen doen
- De stationdozen zitten nu in een vuilzak, zodat die beter beschermd zijn tegen de regen. Best nog iets tussen het deksel van de bak en de vuilzak steken, zodat het water niet blijft staan op die vuilzak in de holte van het deksel
- Grotere gaten maken in alle bakken, de huidige gaten zijn soms te klein om ethernetkabels in te steken zonder heel hard te moeten duwen
- Een groot aantal batons zijn verkeerd in elkaar gestoken, zie HARDWARE.md voor hoe het touw aan de batterij zou moeten hangen
