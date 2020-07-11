import nmap3
nmap = nmap3.Nmap()
os_results = nmap.nmap_os_detection("172.17.0.1")
print(os_results)
