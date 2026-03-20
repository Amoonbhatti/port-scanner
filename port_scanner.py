import socket
import threading
import argparse
import os
from colorama import Fore, Style, init

init(autoreset=True)

# 🎯 Banner
def show_banner():
    os.system("clear")  # Kali/Linux ke liye

    print(Fore.CYAN + Style.BRIGHT + r"""
   
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

        ⚡ Advanced Port Scanner ⚡
           By Amoon Bhatti 😎
    """ + Style.RESET_ALL)


# 🔍 Common ports mapping
common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 8080: "HTTP-Alt"
}


# 🔎 Scan function
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


# 🧠 Argument parser (CLI mode)
parser = argparse.ArgumentParser(description="Advanced Port Scanner")
parser.add_argument("target", nargs='?', help="Target IP or domain")
parser.add_argument("-p", "--ports", help="Port range (e.g. 1-1000)")
parser.add_argument("-t", "--threads", type=int, default=50, help="Threads")

args = parser.parse_args()


# 🔥 Banner sab se pehle
show_banner()


# 🎯 HYBRID MODE

if args.target:
    target = args.target

    if args.ports:
        start_port, end_port = map(int, args.ports.split("-"))
    else:
        start_port, end_port = 1, 1000

else:
    # 👉 Interactive mode
    target = input("Enter target (IP or domain): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))


threads_count = args.threads

print(Fore.YELLOW + f"\n⚡ Scanning {target} from port {start_port} to {end_port} using {threads_count} threads...\n")


# ⚡ Multithreading
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

    if len(threads) >= threads_count:
        for th in threads:
            th.join()
        threads = []

for th in threads:
    th.join()


print(Fore.CYAN + Style.BRIGHT + "\nScan Completed ⚡🔥\n")