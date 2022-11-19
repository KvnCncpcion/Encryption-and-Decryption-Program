print("=================== PROGRAMMED BY ======================")
print("============= KEVIN JOSEPH G. CONCEPCION ===============")
print("===================== BSCOE 2-2 ========================")

from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

# Defining Encode for Encryption
def encode(key, msg):
    encrypt = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        encrypt.append(list_enc)

    return base64.urlsafe_b64encode("".join(encrypt).encode()).decode()

# Defining Decode for Decryption
def decode(key, code):
    decrypt = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        decrypt.append(list_dec)

    return "".join(decrypt)
