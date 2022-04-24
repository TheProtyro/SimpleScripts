import argparse

parser = argparse.ArgumentParser(description="Print a python badchars variable to use in PoC script")
parser.add_argument("-f", "--file", help="File with hex stack dump inside to verify if any badchars", type=str)
args = parser.parse_args()

badchars = ['{:02x}'.format(x) for x in range(1,256)] # list of all possible bad characters in form [01, 02, 03, ...]

# Verification mode if "-f" argument is set
if args.file:
    badchars_file = args.file
    print("[+] Verifying mode...\n")
    with open(badchars_file, 'r') as badfile:
        content = badfile.read().split() # read the content of the file and parse it in form [01, 02, 03, ...]
        first_bad_char_found = False 
        for i, hex_char in enumerate(content):
            if hex_char != badchars[i]:  # check if the hex char is bad or not
                if first_bad_char_found == False: # first bad char ? if yes, it could break the execution flow and other bad chars will not be reliable
                    first_bad_char_found = True
                    print("[+] First bad char found : " + badchars[i])
                else:
                    print("[+] Possible other bad chars found : " + hex_char) # print other badchar for info
            
    
# Print a python badchars variable to use in PoC script
else:
    print("[+] Generating badchars variable...\n")
    print("badchars = (")
    for x in range(1,256):
        if x % 16 == 0:
            print('\n', end ='')
        print("\\x" + '{:02x}'.format(x),end='')
    print("\n)")
