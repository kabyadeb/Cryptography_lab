import math

def encryption(text,width):
    text=text.replace(" ","").replace("\n","").upper()
    cipher=""
    rows=math.ceil(len(text)/width)
    for col in range(width):
        for row in range(rows):
            index=row*width+col
            if len(text)>index:
                cipher+=text[index]
    return cipher

def depcryption(cipher,width):
    plain_txt=[""]*len(cipher)
    t=0
    rows=math.ceil(len(cipher)/width)
    for col in range(width):
        for row in range(rows):
            index=row*width+col
            if len(cipher)>index:
                plain_txt[index]+=cipher[t]
                t+=1
    return "".join(plain_txt)

text="a quick brown fox jump over a lazy dog"
encryption_text=encryption(encryption(text,4),4)
depcryption_text=depcryption(depcryption(encryption_text,4),4)
print("Decrypted text:",depcryption_text)

