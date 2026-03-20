import socket
import threading
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

# 🔥 Hacker Banner
def show_banner():
    print(Fore.RED + r"""
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                ⚡ Advanced Port Scanner | By Amoon Bhatti ⚡
    """ + Style.RESET_ALL)

common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 8080: "HTTP-Alt"
}

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = common_ports.get(port, "Unknown")

            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"

            print(Fore.GREEN + f"[OPEN] Port {port} ({service}) | {banner}")

        sock.close()

    except:
        pass


# 🔥 CLI arguments
parser = argparse.ArgumentParser(description="Advanced Port Scanner")
parser.add_argument("target", help="Target IP or domain")
parser.add_argument("-p", "--ports", default="1-1000", help="Port range")
parser.add_argument("-t", "--threads", type=int, default=50, help="Threads")

args = parser.parse_args()

target = args.target
start_port, end_port = map(int, args.ports.split("-"))

show_banner()

print(Fore.YELLOW + f"\n⚡ Scanning {target} from port {start_port} to {end_port} using {args.threads} threads...\n")

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

    if len(threads) >= args.threads:
        for th in threads:
            th.join()
        threads = []

for th in threads:
    th.join()

print(Fore.CYAN + "\nScan Completed ⚡🔥")