# Safe ARP MITM and Sniffing Simulation
message = "Hello Gateway, this is Alice"

print("Alice sends:\n ", message)
print("\nTraffic is redirected through Mallory (poisoned ARP cache).")
print("\nMallory sniffs the message:\n ", message)
print("\nMallory forwards the message to Gateway.")
print("\nGateway receives:\n ", message)
print("\nNote: Alice and Gateway notice nothing, which is why MITM is dangerous.")