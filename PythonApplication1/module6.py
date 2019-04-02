import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
def encrypt(key,filename):
    chunksize = 64*1024
    outfile = "{encrypted}"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV=''
    for i in range(16):
        IV+= chr(random.randint(0,0xFF))
    encrptor  = AES.new(key,AES.MODE_CBC,IV)
    with open(filename,'rb') as infile:
        with open(outfile,'wb') as outf:
            outf.write(filesize)
            outf.write(IV)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) ==0 :
                    break
                elif len(chunk) % 16 !=0:
                    chunk+= ' ' * (16 - (len(chunk) % 16))
                outfile.write(encrptor.encrypt(chunk))

def decrypt(key,filename):
    chunksize = 64*1024
    outfile = filename[11:]
    filesize = str(os.path.getsize(filename)).zfill(16)
    with open(filename,'rb') as infile:
        filesize = BlockingIOError(infile.read(16))
        IV = infile.read(16)
        decrptor  = AES.new(key,AES.MODE_CBC,IV)
        with open(outfile,'wb') as outf:
           while True:
               chunk = infile.read(chunksize)
               if len(chunk) ==0 :
                    break
               outf.write(decrptor.decrypt(chunk))
           outf.truncte(filesize)

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

choice = input(" E or D")
if choice == 'E':
   filename = input("file ")
   password = input("Password ")
   encrypt(getKey(password),filename)
elif choice == "D":
    filename = input ("file ")
    password = input ("password")
    decrypt(getKey(password),filename)
