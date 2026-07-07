import socket
import time
from concurrent.futures import ThreadPoolExecutor

services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    111: "RPC",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD",
    587: "SMTP Submission",
    631: "IPP (Printing)",
    636: "LDAPS",
    873: "Rsync",
    989: "FTPS Data",
    990: "FTPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    1723: "PPTP VPN",
    1812: "RADIUS Authentication",
    1813: "RADIUS Accounting",
    2049: "NFS",
    2375: "Docker",
    3306: "MySQL",
    3389: "Remote Desktop (RDP)",
    3690: "Subversion (SVN)",
    4369: "Erlang Port Mapper",
    5000: "Flask/UPnP",
    5432: "PostgreSQL",
    5672: "RabbitMQ",
    5900: "VNC",
    5985: "WinRM HTTP",
    5986: "WinRM HTTPS",
    6379: "Redis",
    8000: "HTTP Alternate",
    8080: "HTTP Proxy/Alternate",
    8081: "HTTP Alternate",
    8443: "HTTPS Alternate",
    8888: "Jupyter Notebook",
    9000: "SonarQube/PHP-FPM",
    9090: "Prometheus",
    9200: "Elasticsearch",
    9418: "Git",
    10000: "Webmin",
    11211: "Memcached",
    27017: "MongoDB"
}

Ip = input("Enter the IP address: ").strip()
print(repr(Ip))

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((Ip,port))
    if result==0:
        service = services.get(port, "Unknown Service")
        print(f"Port {port} is open ({service})")
    sock.close()
    

print("1. Default scan")
print("2. Multithread scan")

choice = int(input("Choice: "))

if choice==1:
    start=time.time()
    for port in range(1,1025):
        scan_port(port)
        
    end=time.time()
    print(f"Time taken: {end-start}")

elif choice==2:
    strt=time.time()
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, range(1, 1025))
    end_time=time.time()
    print(f"Time taken: {end_time-strt}")