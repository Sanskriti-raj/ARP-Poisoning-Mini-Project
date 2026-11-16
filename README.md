# ARP Poisoning - Safe Simulation and Detection (Cyber Security Lab 7CS4-22, Experiment 6)
Roll No: 23ESKCY046 | Project Code: CSL-G35 | Environment: Ubuntu 22.04 on WSL2

Ethical note: everything here runs only on my own VMs / isolated host-only network with dummy data.
No spoofed packets are ever sent. Poisoning and MITM are simulated; the detector only monitors.

## Requirements
Ubuntu 22.04 (WSL2), Python 3, Wireshark, Scapy: `sudo apt install python3-scapy wireshark -y`

## Files
| File | Purpose |
|---|---|
| arp_poison_simulation.py | Before/after ARP tables (simulation) |
| arp_mitm_simulation.py | Alice -> Mallory -> Gateway path (simulation) |
| arp_detector.py | Scapy monitor; logs learned mappings and MAC-change warnings |
| test_detector.py | 6 test cases with fake ARP packets |
| run_demo.sh / final_check.sh | Demo runner / pre-submission check |
| evidence/ | arp_alerts.log, test_alerts.log, screenshots/ |

## Run
    python3 arp_poison_simulation.py
    python3 arp_mitm_simulation.py
    python3 test_detector.py
    sudo python3 arp_detector.py      # terminal 1, Ctrl+C to stop
    sudo ip neigh flush all; ping -c 3 $(ip route | awk '/default/ {print $3; exit}')   # terminal 2
