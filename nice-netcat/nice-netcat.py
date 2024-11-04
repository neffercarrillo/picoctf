# nice-netcat.py
# solution to Nice netcat... @ picoCTF

import sys

if __name__ == "__main__":
    cleartext = ""
    for c in sys.stdin.readlines():
        cleartext += chr(int(c))

    print(cleartext)
