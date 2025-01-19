import socket
from datetime import datetime
import sys

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on {target}")
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Temps d'attente de 1 seconde
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port}: \tOuvert")
        sock.close()
    
    return open_ports

def main():
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <target> <start_port> <end_port>")
        sys.exit(1)
    
    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    # Résolution du nom d'hôte en adresse IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Nom d'hôte non valide.")
        sys.exit(1)
    
    print(f"Début du scan à {datetime.now()}")
    open_ports = scan_ports(target_ip, start_port, end_port)
    print(f"Scan terminé à {datetime.now()}")
    print(f"Ports ouverts sur {target_ip}: {open_ports}")

if __name__ == "__main__":
    main()
