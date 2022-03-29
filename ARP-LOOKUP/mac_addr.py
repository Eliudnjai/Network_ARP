from getmac import get_mac_address
import ip_addr


name = ip_addr.GetHostName()


# Ethernet_mac = get_mac_address(interface="Ethernet")
# print(f"Ethernet: {Ethernet_mac}")
# print(f"eth0: {find_mac}")

def GetHostMac():
    result = get_mac_address(hostname=name)
    return result