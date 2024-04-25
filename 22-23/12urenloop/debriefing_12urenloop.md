---
grand_parent: 22-23
parent: 22-23_12urenloop
---

# 12urenloop 2022-2023

- Stylos vinden tijdens het event was moeilijk omdat er geen Zeus stylos mee waren => breng er ~10.
- De baton wissels zijn meestal door doppen die loskomen => maak deze vast met ductape, 1 laag ductape is genoeg.
- er zijn te weinig doppen voor de batons (PVC buis van 40mm buitendiameter), koop die bij
- heatshrink die de kabels van de li-ion battery van batons samenhoudt zodat er niets kan tussenkomen die die apart/los trekt
- kabels van autobatterijen verbinden met spade connectors die ge-heat-shrinkt zijn ipv los daarin draaien


## Netwerk
Eerste editie waar we netwerk voor alle kassa's moeten voorzien, is redelijk goed verlopen mar zorgt voor extra werk. Het barnetwerk is nodig tot het einde van de afterparty waardoor we pas alles kunnen opruimen om 2u00 ipv meteen na het lopen om 21u00. 
- Er is meer netwerk monitoring nodig, en vooral op een manier dat die monitoring blijft werken als dingen fout gaan, want anders verlies je veel info en data en is dingen terug fixen moeilijker. Ideeën voor netwerk monitoring: aantal connected clients op de verschillende subnets, packet loss, gateway en uplink pings en traffic.
- De **meeste** betaalterminals hebben 4g backup en switchen daar meteen naartoe als de uplink wegvalt, en keren terug naar wifi als het weer werkt. 
- Alle ethernetkabels hebben het overleefd, de dubbele kabels voor het barnetwerk hebben we niet nodig gehad, maar op veel van die locaties was het ook effectief niet mogelijk om tijdens het event een kabel te vervangen dus niet echt overbodige luxe?

## 't is kapot
Omstreeks 22u54 kregen we te horen dat het barnetwerk geen internet meer had, na zelf te verbinden met de bar accesspoint in de container en de android melding dat er geen internet is op die wifi hebben we dat ook als situatie aangenomen. We hebben de uplink van de abdij uitgetrokken uit ETH1 en de tadaam ingestoken in ETH2. De statische route om verkeer naar 0.0.0.0/0 via de gateway van de abdij te sturen werd uitgeschakeld en al snel kwam de dynamishce route om alles via de tadaam uplink te sturen er bij. 

Op dat moment had de laptop op het mgmt netwerk terug internet, iedereen in de container op de andere netwerken niet, incl het bar netwerk. Niet meteen een antwoord gevonden waarom, dus dan besloten om het barnetwerk over te schakelen naar het management netwerk. Dit was volgens ons de beste oplossing en niet zo'n groot probleem aangezien het telsysteem al was afgebroken en de applicaties al afgesloten waren. Het barnetwerk had terug internet, maar kreeg IP adressen uit een ander subnet, dus de monitoring kon niet zien dat die allemaal terug online kwamen. Geschatte downtime: 5 - 10 min.

De reden dat enkel het managementnetwerk internet had was omdat de firewall niet juist was ingesteld. Vroeger was er maar 1 poort/interface voorzien voor de uplink en moesten de configuratie tussen static IP en DHCP client en default gateway allemaal aangepast worden tijdens een switch van de ene uplink naar de andere. Nu was er gekozen om elk een aparte interface te voorzien waardoor er minder configuratie aangepast moest worden tijdens zo'n switch. De firewall rules die by default alle verkeer van een bridgenetwerk (i.e. bar of telsysteem netwerk) dropt en enkel verkeer naar een specifieke interface toelaten waren niet aangepast en lieten enkel verkeer naar ETH1 voor de static uplink van de abdij toe. Behalve voor het mgmt netwerk dat by default overal toegang tot had. Het aanpassen van die firewall rules dat ze niet enkel verkeer naar die ene uplink interface maar naar de interface list WAN, waar alle uplinks aan toegevoegd waren, toelaten was de oplossing daarvoor. 

Het barnetwerk hebben we op het management netwerk gelaten om niet nog een onderbreking te veroorzaken. We hebben geprobeerd om terug naar de abdij uplink over te schakelen, maar dat werkte niet. Pings en internet kwam niet door de router ook al hadden we ervoor wel op een laptop internet via die abdij uplink. Terug naar de tadaam uplink overgegaan en daar zijn we voor de rest van de nacht bij gebleven. 

De abdij uplink opnieuw met een laptop succesvol getest met iperf3, dus daar leek niets mis mee te zijn. Op de laptop hadden we hetzelfde statische ip en gateway ingesteld als op de router. 
We hebben de abdij uplink nog wat verder getest op de router, maar enkel selectief verkeer naar eigen servers daarover geroute en de tadaam uplink nog als default gateway gelaten. We kregen er geen pings of traffic door. Op een gegeven moment hebben we op de router de tool 'packet sniffer' opgestart en daarna gingen pings wel door en werkte de abdij uplink magisch wel weer. We hebben geen idee waarom. The End.

## Batterijvoltages

Dit zijn de batterijvoltages zonder load vlak na de afbraak (dus na ~13 uur uptime). De batterijen waren voordien tot minstens 12.7 volt opgeladen: de meting na het opladen werd genomen 5 minuten nadat de batterij afgekoppeld was van de lader.

Er zijn mogelijks 2 gedegradeerde batterijen: G en J

 - Auto B - 12.33V
 - Auto C - 12.33V
 - Auto D - 12.65V
 - Auto G - 10.54V !
 - Auto I - 12.68V
 - Auto J - 11.46V !
 - Auto K - 12.36V

## Livesite

- Teams met zelfde aantal rondes moeten hetzelfde positie nummer krijgen op de livesite (https://github.com/12urenloop/livesite/issues/5)
- Config zou apart moeten zijn van source code, zodat de config vergeten veranderen tijdens de deploy duideijk is (https://github.com/12urenloop/livesite/issues/4)

## MISC

- Dozen die op het terrein staan labelen langs alle kanten met een nummer, zodat die makkelijk herkenbaar zijn
- Klaas moet een kabels met een ervaren iemand leggen zodat deze niet rond harnassen en door harnasblokken worden gewikkeld
- Meer stoffen spanbandjes voor batons, ethernetkabels, etc.
- ethernetkabels enkel met gaffa vastmaken, niet met spanbandjes aan herassen (tijdens afbraak zijn die moeilijk los te maken)
- Betere ethernetkopjes kopen? Eens testen met verschillende tangen ook want sommige kopjes bleven niet goed zitten in switches of maakten slecht contact.
