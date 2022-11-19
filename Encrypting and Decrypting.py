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

# Adding Code for window
window = Tk()
window.geometry("500x500")
window.configure(bg="azure2")
window.title("Encrypt and Decrypt your Messages with ProjectGurukul")

# Adding Variables for Message, Key, Mode and Input
message = StringVar()
pass_key = StringVar()
mode = IntVar()
output = StringVar()

# Adding Heading Frame for the Window
heading_frame = Frame(window, bg ="gray91", bd = 5)
heading_frame.place(relx = 0.2, rely = 0.1, relwidth = 0.7, relheight = 0.16)

# Adding Heading Label for the Heading Frame
heading_label = Label(heading_frame, text="Welcome to Encryption and \nDecryption with ProjectGurukul", fg='grey19', font=('Courier', 15, 'bold'))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Adding Instructions for the user to Enter the Message
text_instruction = Label(window, text="Enter the Message", font=("Courier", 10))
text_instruction.place(x=10, y=150)

# Adding the dedicated space for the text inputted by the user
txt_msg = Entry(window, textvariable=message, width=35, font=("calibre", 10, "normal"))
txt_msg.place(x=200, y=150)

# Adding Instructions for the user to Enter the Key
passkey_instruction = Label(window, text="Enter the key", font=("Courier", 10))
passkey_instruction.place(x=10, y=200)

# Adding the dedicated space for the passkey inputted by the user
passkey_space = Entry(window, textvariable=pass_key, width=35, font=("calibre", 10, "normal"))
passkey_space.place(x=200, y=200)

# Adding the instructions for user to choose between encrypt and decrypt
enc_dec_instructions = Label(window, text="Check one of encrypt or decrypt", font=("Courier", 10))
enc_dec_instructions.place(x=10, y=250)

# Adding the buttons for Encryption and Decryption
Radiobutton(window, text="Encrypt", variable=mode, value=1).place(x=100,y=300)
Radiobutton(window, text="Decrypt", variable=mode, value=2).place(x=200,y=300)

# Adding the label for result
result_label = Label(window, text="Result", font=("Courier", 10))
result_label.place(x=10, y=350)

# Adding the dedicated space for the result
result_space = Entry(window, textvariable=output, width=35, font=("calibre", 10, "normal"))
result_space.place(x=200, y=350)

# Defining the result function
def result():
    txt_msg = message.get()
    k = pass_key.get()
    i = mode.get()
    if (i==1):
        output.set(encode(k, txt_msg))
    elif(i==2):
        output.set(decode(k, txt_msg))
    else:
        messagebox.showinfo("ProjectGurukul", "Please Choose one of Encryption or Decryption. Try again.")

# Defining the reset function
def reset():
    message.set("")
    pass_key.set("")
    mode.set(0)
    output.set("")

