#!/usr/bin/python3

import socket
import argparse
import time
import concurrent.futures

def sock(user):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rhost, rport))
    s.send(bytes(user, encoding='utf-8'))
    r = s.recv(4096)
    s.close()
    bytes_list = r.strip().split()
    last1 = bytes_list[-1].decode('utf-8')
    last2 = bytes_list[-2].decode('utf-8')
    if last1 == '???' and last2 == user[:-1]:
        #print(f"user {user[:-1]} not found")
        return
    else:
        print(f"possible user {user[:-1]} found:")
        print(r.decode('utf-8'))
        return


parser = argparse.ArgumentParser()
parser.add_argument("rhost", help="set the remote host", type=str)
parser.add_argument("wordlist", help="enumerate user from this wordlist", type=str)
parser.add_argument("--rport", help="set the remote port", default=79, type=int)
parser.add_argument("--threads", help="set the number of threads", default=10, type=int)
args = parser.parse_args()

rhost = args.rhost
rport = args.rport
th = args.threads
wordlist = args.wordlist


print(f"""
[+] rhost: {rhost}
[+] rport: {rport}
[+] wordlist: {wordlist}
""")

# User not found

#Login       Name               TTY         Idle    When    Where
#info                  ???

# User found
#
#Login       Name               TTY         Idle    When    Where
#root     Super-User            console      <Dec 19 10:30>
#
#Login       Name               TTY         Idle    When    Where
#sunny           ???            console      <Dec 19 09:56>


start_time = time.perf_counter()

with open(wordlist, 'r') as userlist:
    with concurrent.futures.ThreadPoolExecutor(max_workers=th) as executor:
        results = [executor.submit(sock, user) for user in userlist]

duration = time.perf_counter() - start_time
print(f'Finished in {round(duration, 2)} second(s)')
