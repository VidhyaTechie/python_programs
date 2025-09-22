import re
data= """
Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 192.168.1.100
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
"""
ip_pattern=r"IPv4 Address.*:\s+(\d+\.\d+\.\d+\.\d+)"
subnet_pattern=r"Subnet Mask.*:\s+(\d+\.\d+\.\d+\.\d+)"
default=r"Default Gateway.*:\s+(\d+\.\d+\.\d+\.\d+)"

ip = re.search(ip_pattern, data).group(1)
subnet = re.search(subnet_pattern, data).group(1)
gateway = re.search(default, data).group(1)

print(f"IP Address: {ip}")
print(f"Subnet Mask: {subnet}")
print(f"Default Gateway: {gateway}")
