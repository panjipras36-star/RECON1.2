import socket
import argparse
import sys
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
        return port
    s.close()
    return None

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="RECON1.2 - Tactical Network Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP Address")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g., 22,80,443)", default="22,80,443,8000,8888")
    parser.add_argument("-o", "--output", help="Save results to a file (.txt)")
    args = parser.parse_args()

    target = args.target
    ports = [int(p) for p in args.ports.split(",")]

    print(f"\033[1;34m[*] Starting high-speed scan on {target}...\033[0m\n")
    
    open_ports = []
    
    try:
        with ThreadPoolExecutor(max_workers=20) as executor:
            
            future_to_port = {executor.submit(scan_port, target, p): p for p in ports}
            for future in future_to_port:
                result = future.result()
                if result:
                    open_ports.append(result)
        
        print("\n\033[1;34m[*] Scan complete.\033[0m")
        
    
        if args.output:
            with open(args.output, "w") as f:
                f.write(f"Scan results for {target}\n")
                f.write("-" * 30 + "\n")
                for port in sorted(open_ports):
                    f.write(f"Port {port}: OPEN\n")
            print(f"\033[1;32m[+] Results saved to {args.output}\033[0m")

    except KeyboardInterrupt:
        print("\n\n\033[1;31m[!] Scan interrupted by user. Exiting...\033[0m")
        sys.exit()
    except Exception as e:
        print(f"\n\033[1;31m[!] An error occurred: {e}\033[0m")

if __name__ == "__main__":
    main()
