
from string import ascii_lowercase , ascii_uppercase
from sys import exit
import math
num="0123456789"
sym="~!@#$%^&*()_+`:,.<>?/\[]|-"
print("Welcome to ROT-13 Encryption Program".center(90))
def main():
    print("What do you want to do?")
    print("1:Encryption\n2:Decryption\n")
    ask=int(input("Enter your choice: "))
    if ask==1:
        encryption()
        more()
    elif ask==2:
        decryption()
        more()
    else:
        print("Please Enter Valid choice either 1,2 or 3 got {}".format(ask))


def rot13(ask):
    total=[]
    n=" "
    for i in ask:
        if i in ascii_lowercase:
            index=(ascii_lowercase.find(i)+13)%26
            total.append(ascii_lowercase[index])
        if i in  ascii_uppercase:
            index=(ascii_uppercase.find(i)+13)%26
            total.append(ascii_uppercase[index])
        elif i in num:
            index=(num.find(i)+5)%10
            total.append(num[index])
        elif i in sym:
            index=(sym.find(i)+len(sym)/2)%len(sym)
            total.append(sym[int(index)])
        elif i in n:
            total.append(n)
    return "".join(total)

def encryption():
    ask=input("Enter string to encrypt: ")
    try:
        o=open("encryption.txt","a")
    except:
        o=open("encryption.txt","x")
    print(rot13(ask),file=o)
    o.close()
    print("Encrypted text:\n{} ==> {}".format(ask,rot13(ask)))

def decryption():
    f=open("encryption.txt")
    for line in f:
        print("\nDecrypted text:\n{} ==> {}\n".format(line,rot13(line)))
    f.close()

def more():
    req=input("Do you want to encrypt/decrypt more data?(Y/N)")
    if req.lower()=="yes" or req.lower()== "y":
        main()
    elif req.lower()=="no" or req.lower()=="n":
        exit()
    else:
        print("Please enter either Y/N or Yes/No")
        more()


if __name__=="__main__":main()


