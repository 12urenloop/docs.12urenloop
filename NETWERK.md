#  Netwerk
## Hardware
Flightcase met volledige setup: 
* Powermaster VI 750 R1U UPS
* Mikrotik router	RB3011UiAS
* Netgear GS724TP 24 port managed switch 

Accespoints: van Zeus (eventrouter) en/of SKO
## Setup
| Interface                          	| Function   	| IP-range                     	| Access                  	|
|------------------------------------	|------------	|------------------------------	|-------------------------	|
| ETH 1                              	| Uplink     	| /                            	| Nothing                 	|
| ETH 5, connected to Netgear switch 	| Telsysteem 	| 172.12.50.10-172.12.50.254   	| Uplink, LAN, Telsysteem 	|
| ETH 10                             	| Management 	| 172.12.10.128-172.12.10.254  	| Uplink, LAN, Telsysteem 	|
| ETH 2-4, 6-9                       	| LAN        	| 192.168.88.10-192.168.88.254 	| Uplink, LAN             	|

## Practical
Plug uplink internet access in EHT1. Plug the netgear router in ETH5. Plug all things that need acces to Telsysteem in the netgear switch.
Plug accesspoint (Zeus event router) for internet for regular people in one of the LAN ports on the router. Plug an accesspoint in the Telsysteem netgear switch for wireless for manualcount clients.

## Configuration
The router is configured with three bridge networks: lan, mgnt and telsysteem.
Via Bridge -> Ports, you can configure which interfaces/ports are in each bridge network.

The access is configured per bridge network, using the IP->Firewall rules
* Default rule to drop all traffic not coming from LAN is *disabled*
* New rule to drop all packets from LAN to Telsysteem
* New rule to allow packets from mgmt to Telsysteem (default for packets not destined for uplink, from other networks, is to drop)
* New rule to allow packets from Telsysteem to all (same as above)
