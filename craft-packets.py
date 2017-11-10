# Creating packet
p = IP()

# Showing packet with .show function
p.show()

# Stacking the packets together
p = IP()/TCP()
p.show()

# Moving up the TCP packet
# show() command makes easy to see the changes you are doing on the packets
p.payload.show()

# Changing the TCP port to 444
p.payload.dport=444
p.show()

# Changing the flag to 2
p.payload.flags=2
p.show()
## You will notice the flags will not change, and will remain "S", as it was before. It happens because S
## is the second flag in the bitmask (2^1)

# Now, let's try to change the flags to 18
p.payload.flags=18
p.show()
# You will notice the flags will change to SA


