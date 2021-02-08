import string
import secrets

constantNum = 1000

g = int(input("Input shared value for g: "))
p = int(input("Input shared value for p: "))

AlicePrivateKey = int(secrets.randbelow(constantNum))
BobPrivateKey = int(secrets.randbelow(constantNum))

# print("Alice private key: ", AlicePrivateKey)
# print("Bob private key: ", BobPrivateKey)

AliceKey = pow(g,AlicePrivateKey,p)
BobKey = pow(g,BobPrivateKey,p)

#computation of secret key
AliceKey1 = pow(BobKey,AlicePrivateKey,p)
BobKey1 = pow(AliceKey,BobPrivateKey,p)

if AliceKey1 != BobKey1:
    #if true then exit
    print("error, the shared key is not the same")
    exit()
#false continue get the secret key to bobkey1 or alicekey1
print("SECRET KEY: ", AliceKey1)
#getting the message to be encrypted and converting it to its equivalent ascii code
message = input("\nEnter your message:")
asciiOfMessage = [ord(c) for c in message]

#finding the xor value for each character
xorList = []
for x in asciiOfMessage:
    a = bin(x^AliceKey1)#this line is where the conversion of ascii message and secret key is happening and at the same time finding its XOR value
    xorList.append(a)

#xorLIst is the list of binaries encrypted using diffie hellman key exchange and XOR encryption
#printing the encrypted message in output file (encryptedMessage.txt)
f = open("encryptedMessage.txt", "w")
for a in xorList:
    f.write("%s " % a)

f.close()

input("Kindly press any key to exit")




