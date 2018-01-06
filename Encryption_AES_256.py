import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
def encrypt(key, filename):
        chunksize=64*1024
        outputFile="(encrypted)"+filename
        filesize= str(os.path.getsize(filename)).zfill(16)
        IV=''

        for i in range(16):
            IV += chr(random.randint(0, 0xFF))

        encryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(filename, 'rb') as infile:
            with open(outputFile,'wb') as outfile:
                outfile.write(filesize)
                outfile.write(IV)
		while True:
                    chunk= infile.read(chunksize)
                    if len(chunk)== 0:
                        break
		    elif len(chunk) % 16 !=0:
                        chunk += '' * (16 - (len(chunk) % 16))
                outfile.write(encryptor.encrypt(chunk))
		  
			

def decrypt(key, filename):
    	chunksize=64*1024
    	outputFile=filename[11:]

    	with open(filename, 'rb') as infile:
        	filesize= long(infile.read(16))
        	IV= infile.read(16)

        	decryptor= AES.new(key, AES.MODE_CBC, IV)

        	with open(outputFile, 'wb') as outfile:
        		while True:
                		chunk= infile.read(chunksize)

                		if len(chunk) == 0:
					break

                    		outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)
def getkey(password):
    hasher= SHA256.new(password)
    return hasher.digest()
def Main():
    choice=raw_input("Give us a desired option (E)ncrypt or (D)ecrypt a file ?")
    if choice== 'E':
        filename=raw_input('File to Encrypt: ')
        password=raw_input('password: ')
        encrypt(getkey(password), filename)
        print('done.......wahoooo you have successfully encrypted the file')
    elif choice=='D':
        filename=raw_input('File to Decrypt: ')
        password=raw_input('password: ')
        decrypt(getkey(password), filename)
        print('done.......wahoooo you have successfully decrypted the file')
    else:
        print('OOOps you made a wrong choice..........enter a valid choice')
if __name__== '__main__':
	Main()



































