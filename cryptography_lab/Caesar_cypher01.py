"""
Given a line of plaintext, find the Caesar Cipher by shifting every
alphabetic character 3 positions to the right modulo 26.
Then decrypt the ciphertext to recover the original plaintext."""

def encryption(txt,shift):
    final=""
    for ch in txt:
        if 'A'<=ch<='Z':
            final+=chr((ord(ch)-ord('A')+shift)%26+ord('A'))
        elif 'a'<=ch<='z':
            final+=chr((ord(ch)-ord('a')+shift)%26+ord('a'))
        else:
            final+=ch
    return final

def decryption(txt,shift):
    return encryption(txt,-shift)

plaintext=input("meo")
cyphertext=encryption(plaintext,3) # how many letters to move 
recovered=decryption(cyphertext,3)

print("\n plain text:",plaintext)
print("\n Cypher text:",cyphertext)
print("\n Depcrypted text:",recovered)