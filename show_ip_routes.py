import re
data="""C    10.1.1.0/24 is directly connected, FastEthernet0/0
R    192.168.12.0/24 [120/1] via 192.168.23.2, 00:00:26, FastEthernet1/0
O    10.2.2.0/24 [110/2] via 10.1.1.2, 00:00:22, FastEthernet0/1
R    172.16.0.0/16 [120/1] via 192.168.12.1, 00:00:05, FastEthernet1/0
S    0.0.0.0/0 [1/0] via 10.1.1.254
R    10.20.30.0/24 [120/1] via 172.16.1.2, 00:00:12, Serial1/0
C    192.168.23.0/24 is directly connected, FastEthernet1/0  """

pattern=r"\b((R)\s+.*)\b"
print(re.findall(pattern,data))
