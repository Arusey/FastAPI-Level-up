from types import SimpleNamespace
from scapy import all
from scapy.all import *
import sys
import signal
import os

def signal_handler(signal, frame):
    print('\n===============')
    print('Execution aborted by User')
    print('==================')
    os.system("kill -9" + str(os.getpid()))
    sys.exit()


def signal_exit(signal, frame):
    print("Signal exit")
    sys.exit(1)


def usage():
    if len(sys.argv) < 3:
        print("\nUsage: ")
        print("\twifi-scanner.py -i <interface>\n")
        sys.exit(1)


# Function to sniff wifi packets
def sniffpackets(packet):
    try:
        SRCMAC = packet[0].addr2
        DSTMAC = packet[0].addr1
        BSSID = packet[0].addr3
    except:
        print("Cannot read MAC address")
        print(str(packet).encode("hex"))
        sys.exc_clear()

    try:
        SSIDSize = packet[0][Dot11Elt].len
        SSID = packet[0][Dot11Elt].info


    except:
        SSID = ""
        SSIDSize = 0

    # check to see whethre the packet type = 0 and subtype 8 (Beacon frames)
    
    if packet[0].type == 0:
        ST = packet[0][Dot11].subtype
        if str(ST) == "8" and SSID != "" and DSTMAC.lower() == "ff:ff:ff:ff:ff:ff":
            p = packet[Dot11Elt]
            cap = packet.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}"
                                "{Dot11ProbeResp:%Dot11ProbeResp.cap%}").split('+')
            channel = None
            crypto = set()



def init_process(newiface):
    global ssid_list
    ssid_list = {}
    global s
    # s = conf.L2socket(iface=newiface)
    s = conf.L2socket(iface=newiface)


def setup_monitor(iface):

    print("Setting up sniffing options ...")
    os.system('ifconfig ' + iface + ' down')
    try:
        os.system('iwconfig ' + iface + ' mode monitor')
    except:
        print("Failed to setup your interface in monitor mode")
        sys.exit(1)
    os.system('ifconfig ' + iface + ' up')
    return iface

def check_root():
    if not os.geteuid() == 0:
        print("You must run this script with root privileges")
        exit(1)




if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    usage()
    check_root()
    parameters = {sys.argv[1]:sys.argv[2]}
    if "mon" not in str(parameters["-i"]):
        newiface = setup_monitor(parameters["-i"])
    else:
        newiface = str(parameters["-i"])
    init_process(newiface)
    print("Starting sniffing")
    print("Sniffing on interface " + str(newiface) + " ... \n")
    sniff(iface=newiface, prn=sniffpackets, store=0)

