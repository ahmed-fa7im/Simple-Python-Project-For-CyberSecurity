try:
    import requests
    import sys
    import socket
    rhost = sys.argv[1]
    wordlist = sys.argv[2]

     
    print("[*] Checking RHOST.....")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        status = s.connect_ex((rhost, 80))
        s.close()
        if status == 0:
            print("[DONE]")
            pass
        else:
            print("[FAIL]")
            print(f"[!] ERROR: Cannot Reach RHOST %S\n{ rhost}")
            sys.exit(1)
    except socket.error:
            print("[FAIL]")
            print(f"[!] ERROR: Cannot Reach RHOST %S\n{ rhost}")
            sys.exit(1)


    print("[*] Parsing Wordlist....")
    try:
        with open(wordlist) as file:
            to_check = file.read().strip().split('\n')
        print("[Done]")
        print(f"[*] Total Paths to chek c: %s {str(len(to_check))}")
    except IOError:
        print("[FAIL]")
        print(f"[!] ERROR: Failed to Read Specified File \n")
        sys.exit(1)


    def checkPath(path):
        try:
            response = requests.get(f"http://{rhost}/{path}").status_code
        except Exception:
            print("[!] ERROR : An Unexpected Error Occured")
            sys.exit(1)
        if response == 200:
            print(f"[*] Valid Pah Found http://{rhost}/{path}")
       

    print("\n[*] Beginning Scan...\n")
    for i in range(len(to_check)):
        checkPath(to_check[i])
    print("\n Scan Complete _^^_")

except IndexError:
    print("please run script is true")
    print("python3 Directory-Brute-Forcing.py example.com wordlist.txt")
except KeyboardInterrupt:
    print("bye")
    exit()
