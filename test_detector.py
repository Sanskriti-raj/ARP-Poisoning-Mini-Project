import os
import sys
from scapy.all import ARP, Ether
import arp_detector
from arp_detector import check_arp, arp_table

# Keep test output separate from the live-monitoring log
os.makedirs(arp_detector.LOG_DIR, exist_ok=True)
arp_detector.LOG_FILE = os.path.join(arp_detector.LOG_DIR,
                                     "test_alerts.log")
open(arp_detector.LOG_FILE, "w").close()


def fake(ip, mac):
    return ARP(op=2, psrc=ip, hwsrc=mac)


GW = "192.168.1.1"
MAC_A = "AA:AA:AA:AA:AA:AA"
MAC_B = "BB:BB:BB:BB:BB:BB"
MAC_C = "CC:CC:CC:CC:CC:CC"
MAC_D = "DD:DD:DD:DD:DD:DD"

tests = [
    ("TC1 first sighting is learned", fake(GW, MAC_A), "learned"),
    ("TC2 same MAC again, no alert", fake(GW, MAC_A), "ok"),
    ("TC3 MAC changed -> spoof alert", fake(GW, MAC_C), "alert"),
    ("TC4 different host learned fresh",
     fake("192.168.1.10", MAC_B), "learned"),
    ("TC5 ARP probe 0.0.0.0 ignored", fake("0.0.0.0", MAC_D), "ignored"),
    ("TC6 non-ARP packet ignored", Ether(), "ignored"),
]

arp_table.clear()
failed = 0
for name, pkt, expected in tests:
    got = check_arp(pkt)
    ok = got == expected
    failed += not ok
    status = "PASS" if ok else "FAIL"
    print(f"{status}  {name}  (expected={expected}, got={got})")

print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
sys.exit(1 if failed else 0)