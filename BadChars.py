#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="Find badchars based on a selected binary copy of the Immunity Debugger stack")
parser.add_argument("-f", "--file", help="File with hex stack dump inside to verify if any badchars", type=str)
parser.add_argument("-b", "--bad", help="Already known badchars like \\xde\\xad\\xbe\\xef", type=str)
args = parser.parse_args()

badchars = ['{:02x}'.format(x) for x in range(1,256)] # list of all possible bad characters in form [01, 02, 03, ...]
result = []

if args.file:
    badchars_file = args.file
    print("[+] Finding badchars...\n")
    with open(badchars_file, 'r') as badfile:
        content = badfile.read().split() # read the content of the file and parse it like [01, 02, 03, ...]
        first_bad_char_found = False

        # check if there is already known badchars and remove them from the lists
        if args.bad:
            known_badchars = args.bad
            known_badchars_splited = known_badchars.split('\\x')[1:]
            for badchar in known_badchars_splited:
                bad_index = badchars.index(badchar)
                badchars.remove(badchar)
                del content[bad_index]
                

        for i, hex_char in enumerate(content):

            #next line is for debug purpose
            #print(str(i) + ' - ' + hex_char.lower() + ' - ' + str(badchars[i]))
            
            if hex_char.lower() != badchars[i]:  # check if the hex char is bad or not
                if first_bad_char_found == False: # first bad char ? if yes, it could break the execution flow and other bad chars will not be reliable
                    first_bad_char_found = True
                    print("[+] First bad char found : " + badchars[i])
                    result.append(badchars[i])
                else:
                    print("[+] Possible other bad chars found : " + badchars[i]) # print other not reliable badchars for info
                    result.append(badchars[i])

    # Print the result, including \x00, known badchars and badchars found
    print()
    print("[+] Possible result : \"", end='')
    print('\\x00', end='') 
    [print('\\x' + b, end='') for b in known_badchars_splited]   
    [print('\\x' + r, end='') for r in result]            
    print('"')
    
# Print a python badchars variable to use in PoC script
else:
    print("[+] Generating badchars variable...\n")
    print("badchars = (")
    for x in range(1,256):
        if x % 16 == 0:
            print('\n', end ='')
        print("\\x" + '{:02x}'.format(x),end='')
    print("\n)")
