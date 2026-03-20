import socket

target = input("Enter target (IP or domain): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    sock.close()

print("\nScan Completed ✅")