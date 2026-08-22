def deffie_hell(p,g,a_key,b_key):
    a_pub=pow(g,a_key,p)
    b_pub=pow(g,b_key,p)
    a_shared=pow(b_pub,a_key,p)
    b_shared=pow(a_pub,b_key,p)
    return a_pub,b_pub,a_shared,b_shared

p=int(input("enter Public key"))
g=int(input("enter public base g"))
a=int(input("Alice private key"))
b=int(input("Bob private key"))

a,b,key1,key2=deffie_hell(p,g,a,b)
print("alice public key:",a)
print("bob public key",b)

if key1==key2:
    print("both parties generated the same shared key")
else:
    print("failed as same key. they are different")
