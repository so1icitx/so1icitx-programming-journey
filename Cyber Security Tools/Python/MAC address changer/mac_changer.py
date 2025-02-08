#!/usr/bin/env python3
import subprocess
from mac_art import logo
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser(usage="Usage: %prog -i INTERFACE --mac MAC_ADDRESS\nExample: %prog -i wlan0 --mac 00:11:22:33:44:55",description="This script allows you to change the MAC address of a network interface.\nProvide the interface and the MAC address as options to change the address.")
    parser.add_option("-i", dest="interface",help="Specify the network interface (e.g., eth0, wlan0) to change its MAC address.")
    parser.add_option("--mac", dest="mac", help="Provide the new MAC address to set on the specified interface.")
    parser.add_option("--show", dest="show_interfaces", help="Show all the available network interfaces.",action="store_true")
    return parser.parse_args()

def change_mac(choice_mac, mac_add):
    try:
        subprocess.call(["sudo", "ifconfig", choice_mac, "down"])
        subprocess.call(["sudo", "ifconfig", choice_mac, "hw", "ether", mac_add])
        print(f"[+] Changing MAC address for {choice_mac} to {mac_add}")
        subprocess.call(["sudo", "ifconfig", choice_mac, "up"])

        ifconfig_output = subprocess.check_output(["ifconfig", choice_mac]).decode()
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)

        if mac_address_search_result:
            current_mac = mac_address_search_result.group(0)
            if current_mac.lower() == mac_add.lower():
                print("[+] MAC address changed successfully.")
                end_result = input("Do you want to see the end results? (yes/no): ").lower()
                if end_result == "yes":
                    subprocess.call(["ifconfig", choice_mac])
                    print("[+] Thanks for using MAC Changer.")
                elif end_result == "no":
                    print("[+] Thanks for using MAC Changer.")
                else:
                    print("[!] Invalid input, please try again.")
            else:
                print("[!] MAC address did not change to the desired value.")
        else:
            print("[!] Could not read MAC address")
    except Exception as e:
        print(f"[!] Error: {e}")

def start():
    print(logo)
    options, arguments = get_arguments()
    if options.show_interfaces:
        subprocess.call(["ifconfig"])
        return
    if not options.interface:
        print("[-] Invalid interface provided. Please try again or use --help for more information.")
    elif not options.mac:
        print("[-] Invalid MAC address provided. Please try again or use --help for more information.")
    else:
        change_mac(options.interface, options.mac)

if __name__ == "__main__":
    start()
