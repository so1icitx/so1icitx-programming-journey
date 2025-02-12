#!/usr/bin/env python3
import argparse
import scapy.all as scapy
#install scapy before using it `pip install scapy`

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", dest="range", help="IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list= scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    target_list = []
    for i in answered_list:
        target_dic = {"ip" : i[1].psrc, "mac" : i[1].hwsrc}
        target_list.append(target_dic)
    return target_list

def print_result(result_list):
    print("IP\t\tMAC Address\n" + "- " * 30)
    for i in result_list:
        print(i["ip"] + "\t" + i["mac"] + "\n")

def main():
    options = get_arguments()
    scan_results = scan(options.range)
    print_result(scan_results)

if __name__ == "__main__":
    main()
