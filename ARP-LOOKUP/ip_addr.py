import socket

hostname = socket.gethostname()

ip_addr = socket.gethostbyname(hostname)


print(f"Hostname: {hostname}")
# print(f"ip_addr: {ip_addr}")



def  GetHostName():
    result = socket.gethostbyname(hostname)
    return result


# result = GetHostName()
# print(result)