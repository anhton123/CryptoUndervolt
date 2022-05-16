'''
NAME
    rsa_key_generate.py

DESCRIPTION
    This source file is used create the .pem files used as the public and private key for RSA benchmark.

IMPLEMENTATION
    Uses reference code on pycrytodome to generate public and private key.  
'''

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private10.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("receiver10.pem", "wb")
file_out.write(public_key)
file_out.close()