import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def display_banner():
    print("\033[1;31m" + "="*60)
    print("   ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗ ██╗  ██╗")
    print("   ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║███║  ██║")
    print("   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║╚██║  ╚██║")
    print("   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██║   ██║")
    print("   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║ ██║   ██║")
    print("   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝   ╚═╝")
    print("                 RECON TOOL v1.2 // BY NEUROPRASSSSS")
    print("="*60 + "\033[0m\n")

def scan_port(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"\033[1;32m[+] Port {port:<5} : OPEN\033[0m")
    s.close()

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="RECON1.1 - Tactical Network Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP Address")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g., 22,80,443)", default="22,80,443,8000,8888")
    args = parser.parse_args()

    target = args.target
    ports = [int(p) for p in args.ports.split(",")]

    print(f"\033[1;34m[*] Starting high-speed scan on {target}...\033[0m\n")
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)
    
    print("\n\033[1;34m[*] Scan complete.\033[0m")

if __name__ == "__main__":
    main()
