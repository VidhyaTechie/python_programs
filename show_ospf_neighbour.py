show_op="""Neighbor ID     Pri   State           Dead Time   Address         Interface
100.1.1.1         1   FULL/BDR        00:00:35    2.0.0.1         GigabitEthernet0/0
102.1.1.1         1   FULL/DR         00:00:35    3.0.0.2         GigabitEthernet0/1
107.1.1.1         0   FULL/  -        00:00:35    4.0.0.2         Serial0/0/0"""
pattern=r"(\d+\.\d+\.\d+\.\d+).*?(\d+\.\d+\.\d+\.\d+)\s+(\S+)"
result=re.findall(pattern,show_op)
for i,j,k in result:
    if j =='2.0.0.1':
        print(j,"neighbour's id is",i,"connected via",k)
