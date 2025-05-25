
def encryption():
    a=str(input("Enter the message to encrypt:"))
    # print(a.split())
    b=a.split()
    for i,x in enumerate(b):
        word=b[i]

        if len(word)>2:
            word1=word[0:2]
            word2=word[2:]+word1
            print("be"+word2 , end=" ")
        else:
            word1=word[0]
            word2=word[1:]+word1
            print("be"+word2 , end=" ")
    
          
            
def decryption():
    a=str(input("Enter the message to decrypt:"))
    # print(a.split())
    b=a.split()
    for i,x in enumerate(b):
        word=b[i]

        if len(word)>4:
            word1=word[-2:]
            word2=word1+word[2:-2]
            print(word2 , end=" ")
        else:
            word1=word[-1:]
            word2=word1+word[2:-1]
            print(word2 , end=" ")

print("Secret Language Of Shimla:\n" )
import time
time.sleep(1.5)
try:
    A=int(input("You want to (1) Encrypt a message or  (2) Decrypt a message (1 or 2) : "))
    if A==1:
        encryption()
    elif A==2:
        decryption()
    else:
        print("Please answer with 1 or 2 only")
except ValueError:
    print("Please restart your programme and answer with 1 or 2 only.")