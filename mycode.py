#Malcolm Gray
#Unix Lab Module 10
#Ceasar Cipher
class ccipher:
    def __init__(self):
        self.ckey=-1
    def setkey(self,k):
        self.key=k
    def encrypt(self,m,k):
        cur=0
        newstring=""
        while cur<len(m):
            num = ord(m[cur])                   
            num = num + k
            enLet=chr(num)
            newstring=newstring+enLet
            cur=cur+1
        if k==-1:
            print("Key Not Set")
            return
        else:
            print(newstring)
        
    def decrypt(self,m):
        print(m)
        

cur=0
message=str(input("What is your message"))
key=int(input("Enter Key"))
c=ccipher()
c.setkey(key)
c.encrypt(message,key)
c.decrypt(message)
        
