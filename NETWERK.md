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
| ETH 4, connected to George switch 	| Bar		 	| 192.168.99.10-192.168.99.254  | Uplink, Bar 				|
| ETH 5, connected to Netgear switch 	| Telsysteem 	| 172.12.50.10-172.12.50.254   	| Uplink, Telsysteem 		|
| ETH 9,10                             	| Management 	| 172.12.10.128-172.12.10.254  	| All 						|
| ETH 2-3, 6-8                       	| LAN        	| 192.168.88.10-192.168.88.254 	| Uplink, LAN             	|

### Statip ip's
In Telsysteem: 172.12.50.X
| Name               	|  ip 	|
|--------------------	|-----------	|
| Netgear switch 24p 	| 10        	|
| Client 1           	| 21        	|
| Client 2           	| 22        	|
| ronny01-08           	| 101 - 108    	|


## MAC addresses

```
Address	MAC Network Hostname
;;; Netgear switch 24p
172.12.50.10	9C:C9:EB:E7:07:76		telsysteem			
;;; Dell Clients
172.12.50.21	90:8D:6E:8C:8A:01		telsysteem			Client1
172.12.50.22	90:8D:6E:8C:8A:9B		telsysteem			Client2
;;; ronny's
172.12.50.101	DC:A6:32:49:97:00		telsysteem			ronny01
172.12.50.102	DC:A6:32:49:9A:90		telsysteem			ronny02
172.12.50.103	E4:5F:01:4A:42:DE		telsysteem			ronny03
172.12.50.104	DC:A6:32:49:62:B4		telsysteem			ronny04
172.12.50.105	DC:A6:32:49:65:33		telsysteem			ronny05
172.12.50.106	E4:5F:01:4A:40:E2		telsysteem			ronny06
172.12.50.107	DC:A6:32:49:97:E7		telsysteem			ronny07
172.12.50.108	DC:A6:32:49:98:CD		telsysteem			ronny08
;;; Unifi NetworkVideoRecorder
192.168.99.100	80:2A:A8:4F:EE:5D		bar			
;;; Unifi Camera Finishline
192.168.99.101	68:D7:9A:CF:A6:0F		bar					UVC-G3-a60f
```

## Practical
Plug uplink internet access in ETH1. Plug the netgear router in ETH5. Plug all things that need acces to Telsysteem in the netgear switch.
Plug accesspoint (Zeus event router) for internet for regular people in one of the LAN ports on the router. Plug an accesspoint in the Telsysteem netgear switch for wireless for manualcount clients.

## Configuration
The router is configured with three bridge networks: lan, mgnt and telsysteem.
Via Bridge -> Ports, you can configure which interfaces/ports are in each bridge network.
Each bridge network has its own subnet and corresponding addresspool. These subnets need to be configured and assigne to the rlevant bridge network in multiple places: IP->Adresses; IP->Pool; IP->DHCP Server->Networks; IP->DHCP Server->DHCP.

The access is configured per bridge network, using the IP->Firewall rules
* Default rule to drop all traffic not coming from LAN is *disabled*
* For the different bridge networks rules are added specific for the allowed traffic (i.e. Telsysteem -> Uplink)
* Then, for each network a rule is added to drop all other traffic. (except for mgmt which is allowed everything)

Static ip's are assigned in IP->DHCP Server->Leases

A backup is saved in /network in this repo and can be restored via Files->Browse [upload button]


## Print this page
```
pandoc -V geometry:margin=0.7in -f gfm NETWERK.md -o netwerk.pdf
```
