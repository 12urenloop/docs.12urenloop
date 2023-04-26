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
| ETH 1                              	| Uplink Static | /                            	| Nothing                 	|
| ETH 2                              	| Uplink DHCP   | /                            	| Nothing                 	|
| ETH 4, connected to George switch 	| Bar		 	| 192.168.99.10-192.168.99.254  | Uplink, Bar 				|
| ETH 5, connected to Netgear switch 	| Telsysteem 	| 172.12.50.10-172.12.50.254   	| Uplink, Telsysteem 		|
| ETH 9,10                             	| Management 	| 172.12.10.128-172.12.10.254  	| All 						|
| ETH 3, 6-8                       	| LAN        	| 192.168.88.10-192.168.88.254 	| Uplink, LAN             	|

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
## Security
Disable unneeded services and limit the active services to the needed subnets under IP->Services.
### Uplink
There are 2 uplink ports configured:
- ETH1: where the router takes a static IP -> use for connection with **ABDIJ**
- ETH2: where the router acts as a DHCP Client and expects to receive an IP address -> use for **TADAAM**

Interafces->Interface list: configure uplinks as WAN 
Make sure the interfaces are not part of a bridge network (slaves)

TOEKOMST: https://help.mikrotik.com/docs/pages/viewpage.action?pageId=26476608
#### ETH1
Make sure no DHCP client rule is enabled for this interface: IP->DHCP Client
Add an address (given addres from ABDIJ was 84.199.68.116): under IP->Adresses add address 84.199.68.116/24, gateway 84.199.68.0 and select the corresponding interface. 
Add a route under IP->routes: Dest. Address 0.0.0.0/0, gateway 84.199.68.97
Pinging an external IP like 1.1.1.1 shoud work now.
Configure DNS under IP->DNS: set server to 1.1.1.1 and make sure that remote requests are allowed.

#### ETH2
Add a config for the interface under IP->DHCP Client

### Networks
The router is configured with three bridge networks: lan, mgnt and telsysteem.
Via Bridge -> Ports, you can configure which interfaces/ports are in each bridge network.
Each bridge network has its own subnet and corresponding addresspool. These subnets need to be configured and assigne to the relevant bridge network in multiple places: IP->Adresses; IP->Pool; IP->DHCP Server->Networks; IP->DHCP Server->DHCP.
### Firewall
The access is configured per bridge network, using the IP->Firewall rules
* Default rule to drop all traffic not coming from LAN is *disabled*
* For the different bridge networks rules are added specific for the allowed traffic (i.e. Telsysteem -> Uplink)
* Then, for each network a rule is added to drop all other traffic. (except for mgmt which is allowed everything)

### IP adresses
Static ip's are assigned in IP->DHCP Server->Leases. All connected devices will get listed with an IP address here. 

### Backup config
A backup is saved in /network in this repo and can be restored via Files->Browse [upload button]


## Print this page
```
pandoc -V geometry:margin=0.7in -f gfm NETWERK.md -o netwerk.pdf
```
