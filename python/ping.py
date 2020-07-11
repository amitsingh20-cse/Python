import nmap3
nmap = nmap3.NmapScanTechniques()
result = nmap.nmap_ping_scan("192.168.178.1")
print(result)
