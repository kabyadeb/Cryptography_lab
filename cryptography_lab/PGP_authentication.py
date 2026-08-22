"""
🔐 PGP Authentication — Key Notes
Message তৈরি
Sender প্রথমে plaintext message তৈরি করে।
Hash তৈরি
Message-এর উপর Hash Algorithm (যেমন SHA-256) চালিয়ে message digest তৈরি করা হয়।
Message → Hash → Message Digest
Digital Signature তৈরি
Sender তার Private Key দিয়ে hash/digest-টি encrypt/sign করে।
এটিই Digital Signature।
Message + Signature পাঠানো
Sender message-এর সাথে digital signature receiver-এর কাছে পাঠায়।
Receiver Message পায়
Receiver message এবং signature আলাদা করে।
Signature Verify
Receiver sender-এর Public Key ব্যবহার করে signature verify/decrypt করে original hash বের করে।
আবার Hash তৈরি
Receiver পাওয়া message-এর উপর একই hash algorithm চালিয়ে নতুন hash তৈরি করে।
দুই Hash Compare
Original hash = নতুন hash হলে:
✅ Authentication successful
✅ Message পরিবর্তন হয়নি।
Hash আলাদা হলে:
❌ Authentication failed
❌ Message পরিবর্তিত হতে পারে।
"""
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
#generating receiver .sender public private key using rsa
sender_key=RSA.generate(2048)
sender_publickey,sender_privateKey=sender_key.publickey(),sender_key

#generating receiver pub, private key
receiver_key=RSA.generate(2048)
receiver_privatekey,reciver_publickey=receiver_key,receiver_key.publickey()

#from sender:
msg="I have ears.I am a liar"
hash=SHA256.new(msg.encode())
# sender er private key diye hash kore nisi jeno signature unique hoy
signature =pkcs1_15.new(sender_privateKey).sign(hash) 

#from receiver : 

try:
    hash2=SHA256.new(msg.encode())
    pkcs1_15.new(sender_publickey).verify(hash2,signature)
    print("Verification Successfull mama")

except(ValueError,TypeError):
    print("this not varified")