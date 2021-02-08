import string

f = open("encryptedMessage.txt", "r")
fileIn = (f.read()).replace("0b","")
encryptedMessage = fileIn.split()

key = input("Please input the secret key to decrypt in XOR: ")

xorList = []
for x in encryptedMessage:
    a = bin(int(x,2)^int(key))#this line is where the XOR encryption happens
    xorList.append(a)

#print the decrypted message
print("\nThe message is: ", end = " " )

msg = ""
for i in xorList:
    msg += chr(int(i,2))
print(msg)

input("Kindly press any key to exit")
 
