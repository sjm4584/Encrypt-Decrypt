#!/usr/bin/python

#This script encrypts and decrypts a username and password from a
#given file using the external module PyCrypto. It also does padding
#so we don't need to have a certain length for either the password
#or the username, and this is done through the use of lambda functions


import hashlib, binascii, os, sys, getopt, smtplib
from Crypto.Cipher import AES

#This function uses the password stored in $password_dc to decrypt our
#username and password, as this was what it was encrypted with.
def decrypt_val():
   password_dc = "i'm a password"
   
   #you create the hash of the password so it can be used with AES256 since
   #without it being a hash you have to have the password be a multiple of 16
   key_dc = hashlib.sha256(password_dc).digest()

   f = open('login_info.txt', 'r')

   #readline() only gets 1 ilne and each piece of data is stored on its own
   username_en_r = f.readline()
   password_en_r = f.readline()

   #strip to remove any unwatned whitespace
   username_en_r.strip()
   password_en_r.strip()

   #you have to unhexify it because when it's written after being encrypted
   #it's written in hex
   username_en = binascii.unhexlify(username_en_r)
   password_en = binascii.unhexlify(password_en_r)

   print '-'*10, 'Decrypting', '-'*10

   #This is where the actual decryption takes place   
   de_obj = AES.new(key_dc, AES.MODE_CBC, iv)
   username_p = de_obj.decrypt(username_en)
   password_p = de_obj.decrypt(password_en)
   
   #removes the padding that was done in the encryption process
   username_p_r = unpad(username_p_r)
   password_p_r = unpad(password_p_r)

   print"Username is: ", username_p_r
   print"Password is: ", password_p_r


#This function encrypts our username and password that is stored in the file
def encrypt_val():
   #this lambda is used to pad our file contents that's going to be encrypted
   #so it doesn't have to be the length of a multiple of 16
   pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
   
   password_en = "i'm a password"
   
   #hashlib creates a hash for our key so we don't need our passwords to be
   #a multiple of 16 which can be annoying. Hashes cannot be reversed.
   key_en = hashlib.sha256(password_en).digest()
   
   #Block Size for AES is 128 bits (16 bytes), and is the size of the string
   #of plaintext + key that gets fed into the cipher
   BS = 16

   #initalization vector, best to give it a random val each time and has to
   #be 16 bytes for CBC
   iv = os.urandom(BS)

   f = open('try1.txt', 'r+b')
   username_p = f.readline()
   password_p = f.readline()

   print '-'*10, 'Encrypting', '-'*10

   en_obj = AES.new(key_en, AES.MODE_CBC, iv)
   username_p = pad(username_p)
   password_p = pad(password_p)
   
   username_en = en_obj.encrypt(username_p)
   password_en = en_obj.encrypt(password_p)

   #encode it in hex so it's readable when you open the file
   f.write(username_en.encode('hex'))
   f.write(password_en.encode('hex'))
   f.close()


def main():
   encrypt_val()
   decrypt_val()



if __name__ == '__main__':
   main()




















   
