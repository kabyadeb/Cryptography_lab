"""
RSA is a secure asymmetric encryption algorithm when a sufficiently large key size, such as RSA-2048 or higher, is used. It uses a public key for encryption and a private key for decryption.
p = 1024-bit prime
q = 1024-bit prime

n = p × q

n.bit_length() = 2048
for example , 
 p = 156592146968232731077753861243403138324780811885287945508222796002809507182256972354401805152477428767395844486095665040794113985918946403792603523777338371060496657503758704972579285488215296776385972122824555634114794338044027149866596470940890755062631565057662682655569095191799667839606851856890876468229

q = 133729832868296280967577901290256443380530752415493447782323987478198871650360858572567637859432658102857237457737091629499764147550299261759238224575465951256099020896054621030359975523920170982066348516760872411912469820298621587824598658973091836153991225218979511237251847442601150883269020210038804151809

n = p * q

print(p.bit_length())  # 1024
print(q.bit_length())  # 1024
print(n.bit_length())  # 2048

বাস্তব RSA key হিসেবে নতুন cryptographically secure random primes ব্যবহার করতে হবে।
"""


from math import gcd

q=int(input("Enter a prime number:"))
p=int(input("Enter a prime number :"))
n=p*q
phi=(p-1)*(q-1)
e=7
while gcd(e,phi)!=1:
    e+=1
d=pow(e,-1,phi)
print("public key:",(e,n))
print("private key:",(d,n))
#encryption
plaintext=input("Enter the text:")
ciphertest=[pow(ord(char),e,n) for char in plaintext]
print("cipher text:",ciphertest)
#decription 
decryptedtext="".join([chr(pow(c,d,n)) for c in ciphertest])
print("decrypted text:",decryptedtext)