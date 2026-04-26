---
title: Deploying
nav_order: 91
has_children: true
---

# Deploying the (12)urenloop stack

# Requirements

## Inventory

Gather the following:

- [ ] 1 Flight case with router/switch:
    - See the [Network documentation](./NETWORK)

- [ ] 2 clients:
    - Dell thin clients
    - `snowball` & `meeseeks` from Zeus
    - These will be wiped!

- [ ] 8 ronnys:
    - Also known as stations
    - Raspberry Pi 4's
    - These will be wiped!

- [ ] 1 laptop with `uv` installed

Make everything is labelled:
    - [ ] `client1-2`
    - [ ] `ronny01-08`
    - [ ] What ports on the switch are to be used for the `telnet` (tel-network).

## Static DHCP leases

The router should automatically assign IP addresses based on MAC address via DHCP as follows:

| Host    | IP            | MAC               |
|---------|---------------|-------------------|
| client1 | 172.12.50.21  | 90:8D:6E:8C:8A:01 |
| client2 | 172.12.50.22  | 90:8D:6E:8C:8A:9B |
| ronny01 | 172.12.50.101 | DC:A6:32:49:97:00 |
| ronny02 | 172.12.50.102 | DC:A6:32:49:9A:90 |
| ronny03 | 172.12.50.103 | E4:5F:01:4A:42:DE |
| ronny04 | 172.12.50.104 | DC:A6:32:49:62:B4 |
| ronny05 | 172.12.50.105 | DC:A6:32:49:65:33 |
| ronny06 | 172.12.50.106 | E4:5F:01:4A:40:E2 |
| ronny07 | 172.12.50.107 | DC:A6:32:49:97:E7 |
| ronny08 | 172.12.50.108 | DC:A6:32:49:98:CD |

> If you replace any hardware, make sure to update the MAC in the router config, this table and the [Network documentation](./NETWORK)

## Preparing devices for ansible

### Clients

Wipe and install Debian on the clients as described in [Preparing a client for the ansible-config](deploying/prepare_a_client):
    - [ ] `client1`
    - [ ] `client2`

### Ronnys

Flash the ronnys and set a password as described in [Preparing a ronny for the ansible-config](deploying/prepare_a_ronny):
    - [ ] `ronny01`
    - [ ] `ronny02`
    - [ ] `ronny03`
    - [ ] `ronny04`
    - [ ] `ronny05`
    - [ ] `ronny06`
    - [ ] `ronny07`
    - [ ] `ronny08`

### Laptop

- [ ] Clone the [ansible-config](https://github.com/12urenloop/ansible-config/) repository on the laptop and follow the install instructions for dependencies in the `README.md`.

## Deploying

Ensure your `hosts.yml` is accurate.

Then, execute all relevant ansible playbooks:

```sh
ansible-playbook -kK playbook-01-common-init.yml
ansible-playbook -kK playbook-02-clients-init.yml
ansible-playbook -kK playbook-03-stations-init.yml
```

```sh
ansible-playbook -kK playbook-10-stations-ronny.yml
# ansible-playbook -kK playbook-11-stations-uwb.yml # prototype
```

```sh
ansible-playbook -kK playbook-20-client1-telraam.yml
...
```

```sh
ansible-playbook -kK playbook-30-client2-monitoring.yml
...
```
