import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.75.128")
print(results)
