#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"
DEBUG = False

def debug(*args):
    if DEBUG:
        print("DEBUG:",*args)

def startup(key_location):
    flag = open(FLAG_FILE).read()
    kf = open(KEY_FILE, "rb").read()

    start = key_location
    stop = key_location + len(flag)

    key = kf[start:stop]
    key_location = stop

    debug("flag:" + flag)
    debug(key)
    debug(len(flag),len(key))
    for i in (range(0,len(flag))):
        debug(flag[i],ord(flag[i]),key[i],"{:02x}".format(ord(flag[i])^key[i]))
    
    result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
    print("This is the encrypted flag!\n{}\n".format("".join(result)))

    return key_location

def encrypt(key_location):
    ui = input("What data would you like to encrypt? ").rstrip()
    if len(ui) == 0 or len(ui) > KEY_LEN:
        return -1

    start = key_location
    stop = key_location + len(ui)

    debug(f"encrypt: key start: {start}")
    debug(f"encrypt: key stop: {stop}")
    
    kf = open(KEY_FILE, "rb").read()

    debug(f"encrypt: this is the keyfile length:",len(kf))
    
    if stop >= KEY_LEN:
        stop = stop % KEY_LEN
        key = kf[start:] + kf[:stop]
    else:
        key = kf[start:stop]
    key_location = stop

    debug(f"this is the key value: {key}")
    
    result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

    print("Here ya go!\n{}\n".format("".join(result)))

    return key_location

print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
    c = encrypt(c)
