import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust the timeout as needed

        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter target host: ")
    port_range = input("Enter port range (e.g., 1-100): ")

    try:
        start_port, end_port = map(int, port_range.split('-'))
        ports_to_scan = range(start_port, end_port + 1)
    except ValueError:
        print("Invalid port range format. Please use the format 'start-end'.")
        exit()

    open_ports = scan_ports(target_host, ports_to_scan)

    if open_ports:
        print("Open ports on", target_host, "are:", open_ports)
    else:
        print("No open ports found on", target_host)
