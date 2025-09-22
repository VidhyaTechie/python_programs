arp_a="""Internet Address      Physical Address      Type
 10.1.1.1              0030.f29b.0c01        dynamic
 10.1.1.2              000d.bd5d.2eb0        dynamic
"""
pattern=r"(\d+.*)"
match=re.findall(pattern,arp_a)
for item in match:
    print(item)
