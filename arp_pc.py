arp_a="""Internet Address      Physical Address      Type
 10.1.1.1              0030.f29b.0c01        dynamic
 10.1.1.2              000d.bd5d.2eb0        dynamic
"""

output = re.findall(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\.]+)\s+(\w+)', arp_a)
for ip,mac,dynamic in output:
     print(f"IP: {ip}, MAC: {mac}, Type: {dynamic}")
