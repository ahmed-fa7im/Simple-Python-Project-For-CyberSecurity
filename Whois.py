import socket

def whois_lookup(domain):
    server = "whois.iana.org"
    port = 43
    query = domain + "\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    sock.send(query.encode())

    response = b""
    while True:
        data = sock.recv(4096)
        response += data
        if not data:
            break

    sock.close()
    return response.decode()

if __name__ == "__main__":
    domain = input("Enter domain: ")
    result = whois_lookup(domain)
    print(result)