import socket

hostname = socket.gethostname()

ip_addr = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"ip_addr: {ip_addr}")
