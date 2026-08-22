"""
You are supplied a file of large nonrepeating set of truly random key letter. Your job is to encrypt the
plaintext using ONE TIME PAD technique. Then perform the reverse operation to get original plaintext.

OTP-তে একটা key থাকে এবং প্রতিটি character-এর জন্য key-এর আলাদা value ব্যবহার হয়।
CONS: 
1. Key-এর length plaintext-এর সমান হতে হবে
2. Key securely share করা কঠিন
3. Key একবারের বেশি ব্যবহার করা যাবে না
"""

def encryption(txt,shift):
    encryption_text=""
    for i in range(len(txt)):
        encryption_text+=chr((ord(txt[i])+ord(shift[i])-2*ord("A"))%26+ord('A'))
    return encryption_text
def decryption(cipher,shift):
    plain_text=""
    for i in range(len(cipher)):
        plain_text+=chr((ord(cipher[i])-ord(shift[i])-2*ord("A"))%26+ord('A'))
    return plain_text
with open("key.txt","r") as file:
    shift=file.read().strip().upper()
text="afterFcuk"
text=text.replace(" ","").upper()

encryption_msg=encryption(text,shift)
print("Encrypted text:",encryption_msg)

print("Plaintext length:", len(text))
print("Ciphertext length:", len(encryption_msg))
decryption_msg=decryption(encryption_msg,shift)
print("Decrypted:",decryption_msg)
