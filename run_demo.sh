#!/bin/bash
#run from the project folder:  bash run_demo.sh
cd "$(dirname "$0")" || exit 1
pause() { echo; read -r -p ">>> Press Enter to continue..."; clear; }

clear
echo "STEP 1: Current ARP table (normal state)"
ip neigh
pause

echo "STEP 2: ARP poisoning simulation (no real packets)"
python3 arp_poison_simulation.py
pause

echo "STEP 3: MITM / sniffing simulation"
python3 arp_mitm_simulation.py
pause

echo "STEP 4: Detector test cases (fake ARP packets)"
python3 test_detector.py
echo; echo "Test log:"; cat evidence/test_alerts.log
pause

GW=$(ip route | awk '/default/ {print $3; exit}')
echo "STEP 5: Live ARP monitor (needs root). Gateway detected: $GW"
echo "        Open a 2nd WSL terminal in VS Code and run:"
echo "        sudo ip neigh flush all ; ping -c 3 $GW"
echo "        Press Ctrl+C here when done."
sudo python3 arp_detector.py
echo; echo "Saved log:"; cat evidence/arp_alerts.log