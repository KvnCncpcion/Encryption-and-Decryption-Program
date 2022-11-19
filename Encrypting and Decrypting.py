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
wn = Tk()
wn.geometry("500x500")
wn.configure(bg='azure2')
wn.title("Encrypt and Decrypt your Messages with ProjectGurukul")

# Adding Variables for Message, Key, Mode and Input
Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

# Adding Heading Frame for the Window
headingFrame1 = Frame(wn,bg="gray91",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.7,relheight=0.16)

# Adding Heading Label for the Heading Frame
headingLabel = Label(headingFrame1, text=" Welcome to Encryption and \nDecryption with ProjectGurukul", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Adding Instructions for the user to Enter the Message
label1 = Label(wn, text='Enter the Message', font=('Courier',10))
label1.place(x=10,y=150)

# Adding the dedicated space for the text inputted by the user
msg = Entry(wn,textvariable=Message, width=35, font=('calibre',10,'normal'))
msg.place(x=200,y=150)

# Adding Instructions for the user to Enter the Key
label2 = Label(wn, text='Enter the key', font=('Courier',10))
label2.place(x=10,y=200)

# Adding the dedicated space for the passkey inputted by the user
InpKey = Entry(wn, textvariable=key, width=35,font=('calibre',10,'normal'))
InpKey.place(x=200,y=200)

# Adding the instructions for user to choose between encrypt and decrypt
label3 = Label(wn, text='Check one of encrypt or decrypt', font=('Courier',10))
label3.place(x=10,y=250)

# Adding the buttons for Encryption and Decryption
Radiobutton(wn, text='Encrypt', variable=mode, value=1).place(x=100,y=300)
Radiobutton(wn, text='Decrypt', variable=mode, value=2).place(x=200,y=300)

# Adding the label for result
label3 = Label(wn, text='Result', font=('Courier',10))
label3.place(x=10,y=350)

# Adding the dedicated space for the result
res = Entry(wn,textvariable=Output, width=35, font=('calibre',10,'normal'))
res.place(x=200,y=350)

# Defining the result function
def Result():
    msg = Message.get()
    k= key.get()
    i = mode.get()
    if (i==1):
        Output.set(encode(k, msg))
    elif(i==2):
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('ProjectGurukul', 'Please Choose one of Encryption or Decryption. Try again.')

# Defining the reset function
def Reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")

# Adding interactable buttons for show, reset and quit
ShowBtn = Button(wn,text="Show Message",bg='lavender blush2', fg='black',width=15,height=1,command=Result)
ShowBtn['font'] = font.Font( size=12)
ShowBtn.place(x=180,y=400)

ResetBtn = Button(wn, text='Reset', bg='honeydew2', fg='black', width=15,height=1,command=Reset)
ResetBtn['font'] = font.Font( size=12)
ResetBtn.place(x=15,y=400)

QuitBtn = Button(wn, text='Exit', bg='old lace', fg='black',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=12)
QuitBtn.place(x=345,y=400)

wn.mainloop()

# https://projectgurukul.org/python-message-encryption-decryption-project/#:~:text=Python%20Message%20Encryption%20Decryption%20Project%20File%20Structure%201,7.%20Adding%20the%20buttons%20and%20their%20functions%20