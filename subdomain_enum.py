import dns.resolver
import sys

readFile = open(r"C:\\Users\\AHMED\\Downloads\\subdomains-top1mil-5000.txt", "r")
name = readFile.read()
sub_dom = name.splitlines()

try:
    domain = sys.argv[1]
except IndexError:
    print("python3 subdomain.py <example.com>")
    quit()



for sub in sub_dom:
    try:
        finder = dns.resolver.resolve(f"{sub}.{domain}", "A")
        if finder:
            print(f"{sub}.{domain}")

    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    except KeyboardInterrupt:
        quit()

