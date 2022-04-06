#  Netwerk
## Hardware
Flightcase met volledige setup: 
* Powermaster VI 750 R1U UPS
* Mikrotik router	RB3011UiAS
* Netgear GS724TP 24 port managed switch 

Accespoints: van Zeus (eventrouter) en/of SKO
## Setup
| Interface (router)                 	| Function   	| IP-range                     	| Access                  	|
|------------------------------------	|------------	|------------------------------	|-------------------------	|
| ETH 1                              	| Uplink     	| /                            	| Nothing                 	|
| ETH 5, connected to Netgear switch 	| Telsysteem 	| 172.12.50.10-172.12.50.254   	| Uplink, LAN, Telsysteem 	|
| ETH 10                             	| Management 	| 172.12.10.128-172.12.10.254  	| Uplink, LAN, Telsysteem 	|
| ETH 2-4, 6-9                       	| LAN        	| 192.168.88.10-192.168.88.254 	| Uplink, LAN             	|

### Statip ip's 
In Telsysteem: 172.12.50.X
| Name               	|  ip 	|
|--------------------	|-----------	|
| Netgear switch 24p 	| 10        	|
| Client 1           	| 21        	|
| Client 2           	| 22        	|
| ronny01-08           	| 101 - 108    	|
| Zeus event router  	| 200       	|

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

Static ip's are assigned in IP->DHCP Server->Leases 

A backup is saved in /network in this repo and can be restored via Files->Browse [upload button]

## MAC addresses

```
Address	MAC Address	Client ID	Server	Active Address	Active MAC      Address	Active Host Name	Expires After	 
;;; Netgear switch 24p
-D		172.12.50.10	9C:C9:EB:E7:07:76	1:9c:c9:eb:e7:7:76	telsysteem
-D              172.12.50.10	9C:C9:EB:E7:07:76       GS724TPv2	00:08:38	
;;; Ubiquity Manualcount AP
-D		172.12.50.11	80:2A:A8:A0:2F:4D	1:80:2a:a8:a0:2f:4d	telsysteem			george		
;;; Dell Clients
-D		172.12.50.21	90:8D:6E:8C:8A:01		telsysteem			Client1		
-D		172.12.50.22	90:8D:6E:8C:8A:9B		telsysteem			Client2		
;;; ronny's
-D		172.12.50.101	DC:A6:32:49:97:00		telsysteem			ronny01		
-D		172.12.50.102	DC:A6:32:49:9A:90		telsysteem			ronny02		
-D		172.12.50.103	E4:5F:01:4A:42:DE		telsysteem			ronny03		
-D		172.12.50.104	DC:A6:32:49:62:B4		telsysteem			ronny04		
-D		172.12.50.105	DC:A6:32:49:65:33		telsysteem			ronny05		
-D		172.12.50.106	E4:5F:01:4A:40:E2		telsysteem			ronny06		
-D		172.12.50.107	DC:A6:32:49:97:E7		telsysteem			ronny07		
-D		172.12.50.108	DC:A6:32:49:98:CD		telsysteem			ronny08		
;;; Zeus event router op Telsysteem
-D		172.12.50.200	00:0A:CD:08:7A:4D		telsysteem			OpenWrt		
```
