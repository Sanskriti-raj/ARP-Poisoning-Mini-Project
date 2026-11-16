import os
from datetime import datetime
from scapy.all import sniff, ARP

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "evidence")
LOG_FILE = os.path.join(LOG_DIR, "arp_alerts.log")

arp_table = {}  # IP -> MAC learned so far


def log(msg):
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def check_arp(packet):
    """Return 'ignored', 'learned', 'ok' or 'alert'."""
    if not packet.haslayer(ARP):
        return "ignored"
    ip, mac = packet[ARP].psrc, packet[ARP].hwsrc
    if ip == "0.0.0.0":  # ARP probe, no real sender IP
        return "ignored"
    if ip not in arp_table:
        arp_table[ip] = mac
        log(f"Learned  {ip} -> {mac}")
        return "learned"
    if arp_table[ip] != mac:
        old = arp_table[ip]
        log(f"WARNING possible ARP spoofing: {ip} was {old}, now {mac}")
        return "alert"
    return "ok"


def handle(packet):
    check_arp(packet)  # no return value, so sniff() prints nothing extra


if __name__ == "__main__":
    log("ARP Monitoring Started...")
    sniff(filter="arp", prn=handle, store=False)