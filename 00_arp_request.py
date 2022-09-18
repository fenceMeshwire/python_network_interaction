#!/usr/bin/env python3

# 00_arp_request.py

# Purpose:
# Concept of showing IP addresses of local machines within your private owned network.
# The ARP (Address Resolution Protocol, RFC 826) is used to find the IP and MAC address 
# of the neighbors in a network. 

# This can be also achieved much easier, by typing 'arp -a' in the command line 
# if you work on a windows computer.

# Dependency
import scapy.all as scapy

def do_arp(ip_router):
    arp_request = scapy.ARP(pdst=ip_router)
    broadcast = scapy.Ether()
    broadcast.dst='ff:ff:ff:ff:ff:ff' # Do an arp-request by sending the broadcast address.
    broadcast_over_arp_request = broadcast/arp_request
    replies = scapy.srp(broadcast_over_arp_request, timeout = 1)[0]
    print('IP address', '\t|  ', 'MAC address')
    print('-' * 40)
    for reply in replies:
        print(reply[1].psrc, '\t|  ', reply[1].hwsrc)

if __name__ == '__main__':
    ip_router = '192.168.0.1/24'
    do_arp(ip_router)
