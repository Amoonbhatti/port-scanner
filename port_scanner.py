import socket

target = input("Enter target (IP or domain): ")

print(f"\nScanning {target}...\n")

for port in range(20, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    sock.close()

print("\nScan Completed ✅")