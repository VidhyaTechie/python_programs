import re
mac_adrress="""
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0001.9722.000d    DYNAMIC      Fa0/2
   1    000d.bd5d.2eb0    DYNAMIC      Fa0/1
   1    0030.f29b.0c01    DYNAMIC      Fa0/3
"""
output= re.findall(r"(\d+)\s+([0-9a-zA-Z\.]+)\s+(\S+)\s+(\S+)",mac_address)
print(output)
