import dns.resolver
import sys

dns_record_type = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']

try:
    domain = sys.argv[1]
except IndexError:
    print("python3 demodns.py <example.com>")
for records in dns_record_type:
    
    try:
        example = dns.resolver.resolve(domain,records)
        print(30*"-")
        for out_example in example:
            print(f"{records}  {out_example.to_text()}")
            
    except NameError:
        pass
    except dns.resolver.NXDOMAIN:
        
        print(f"{domain} is not exist.")
        quit()
    except dns.resolver.NoAnswer:
        print(30*"-")
        print(f"{records} Not Found")
        pass
    except dns.resolver.LifetimeTimeout:
        print("The resolution lifetime expired.")
        quit()
    except KeyboardInterrupt:
        print("bye '_'")
        quit()