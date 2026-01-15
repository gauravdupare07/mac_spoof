#!/usr/bin/env python3

import subprocess
import optparse
import re
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# ---------------- BANNER ---------------- #
def banner():
    print(Fore.CYAN + r"""
  ███╗   ███╗  █████╗  ██████╗     ███████╗██████╗  ██████╗  ██████╗ ███████╗
  ████╗ ████║ ██╔══██╗██╔════╝     ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝
  ██╔████╔██║ ███████║██║          ███████╗██████╔╝██║   ██║██║   ██║█████╗
  ██║╚██╔╝██║ ██╔══██║██║          ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝
  ██║ ╚═╝ ██║ ██║  ██║╚██████╗     ███████║██║     ╚██████╔╝╚██████╔╝██║
  ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝
    """)

    print(Fore.YELLOW + "                Version : 1.0")
    print(Fore.GREEN  + "        [+] MACSpoof – MAC Address Spoofing Tool")
    print(Fore.RED    + "        [-] Created by Giga_Byte_Flow\n")


# ---------------- ARGUMENT PARSER ---------------- #
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Network interface (e.g., eth0, wlan0)")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="New MAC address (e.g., 00:11:22:33:44:55)")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for info")
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for info")

    return options


# ---------------- MAC FUNCTIONS ---------------- #
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(
        ["ifconfig", interface], text=True
    )
    mac_search = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result
    )

    if mac_search:
        return mac_search.group(0)
    else:
        print(Fore.RED + "[-] Could not read MAC address")
        return None


def change_mac(interface, new_mac):
    print(Fore.YELLOW + f"[+] Spoofing MAC address for {interface} → {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# ---------------- MAIN ---------------- #
if __name__ == "__main__":

    if not sys.platform.startswith("linux"):
        print(Fore.RED + "[-] MACSpoof works only on Linux systems")
        sys.exit(1)

    if os.geteuid() != 0:
        print(Fore.RED + "[-] Please run MACSpoof as root (sudo)")
        sys.exit(1)

    banner()

    options = get_arguments()

    current_mac = get_current_mac(options.interface)
    print(Fore.CYAN + f"[+] Current MAC → {current_mac}")

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)

    if current_mac == options.new_mac:
        print(Fore.GREEN + f"[✔] MAC successfully spoofed → {current_mac}")
    else:
        print(Fore.RED + "[-] MAC spoofing failed")
