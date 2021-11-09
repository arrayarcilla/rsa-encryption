import math


def RSAencryption(p , q, str):
    n = p * q
    z = (p - 1) * (q - 1)
    for e in range(2, n - 1):
        if z % e != 0:
            break
    for d in range(z + n, 2, -1):
        if (e * d - 1) % z == 0:
            break
    newStr=""
    for x in str:
        i = 0
        m = pow(ord(x), e)%n
    
        newStr = newStr + chr(m)
        i += 1

    return newStr

def RSAdecryption(p,q,str):
    n = p * q
    z = (p - 1) * (q - 1)
    for e in range(2, n - 1):
        if z % e != 0:
            break
    for d in range(z + n, 2, -1):
        if (e * d - 1) % z == 0:
            break
    newStr=""
    for x in str:
        c = pow(ord(x), d) % n
        newStr += chr(c)
        
    return newStr

num1 = 11
num2 = 13
print("Input string:")
str = input()

newStr = RSAencryption(num1, num2, str)
print("Encrypted key: "+ newStr)

newStr = RSAdecryption(num1, num2, newStr)
print("Decrypted key: "+ newStr)

