import math
def encryption(text,width):
    text=text.replace(" ","").replace("\n","").upper()
    rows=math.ceil(len(text)/width)
    cipher=""
    for col in range(width):
        for row in range(rows):
            index=row*width+col
            if index<len(text):
                cipher+=text[index]
    return cipher

def dypcryption(cipher,width):
    plained_text=[""]*len(cipher)
    t=0
    rows=math.ceil(len(cipher)/width)
    for col in range(width):
        for row in range(rows):
            index=row*width+col
            if index<len(cipher):
                plained_text[index]=cipher[t]
                t+=1
    return "".join(plained_text)
           


text="This is the computer Science Department"

encryption_text=encryption(text,4)
print("ENcrypted message:: ",encryption_text)
dypcryption_text=dypcryption(encryption_text,4)
print("DECRYPted message:",dypcryption_text)

