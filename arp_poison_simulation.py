# Safe ARP Poisoning Simulation - no real packets are sent

alice_arp = {"192.168.1.1": "AA:AA:AA:AA:AA:AA"}     # Alice thinks gateway = AA..
gateway_arp = {"192.168.1.10": "BB:BB:BB:BB:BB:BB"}  # Gateway thinks Alice = BB..
mallory_mac = "CC:CC:CC:CC:CC:CC"

def show(title):
    print(f"\n===== {title} =====")
    print("Alice ARP Table:")
    for ip, mac in alice_arp.items():
        print(" ", ip, "->", mac)
    print("Gateway ARP Table:")
    for ip, mac in gateway_arp.items():
        print(" ", ip, "->", mac)

show("BEFORE ARP POISONING")
alice_arp["192.168.1.1"] = mallory_mac      # Mallory pretends to be the gateway
gateway_arp["192.168.1.10"] = mallory_mac   # Mallory pretends to be Alice
show("AFTER ARP POISONING")