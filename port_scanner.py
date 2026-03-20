import socket

# Common ports with service names
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    8080: "HTTP-Alt"
}

try:
    target = input("Enter target (IP or domain): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                service = common_ports.get(port, "Unknown")
                print(f"[OPEN] Port {port} ({service})")

            sock.close()

        except:
            continue

    print("\nScan Completed ✅")

except ValueError:
    print("❌ Please enter valid port numbers!")

except socket.gaierror:
    print("❌ Invalid target. Check domain/IP!")

except KeyboardInterrupt:
    print("\n⛔ Scan stopped by user")