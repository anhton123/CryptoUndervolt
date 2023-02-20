'''
NAME:
    rsa_bench.py

DESCRIPTION:
    This source file is used for running the benchmark for the guardband analysis of the RSA algorithim.


IMPLEMENTATION:
    This source file reads in a file called "rsa_data.txt" to get the random valued operands (plaintext). 
    It then takes these operands and writes the rsa encryption using the public keys (receiverX.pem)
    for each of the operands to <x>.txt NUM_OF_ITERATION times.  

USAGE:
    # runs the benchmark and writes to <x>.txt
        python rsa_bench.py <x>.txt  

EXAMPLE:
    # runs the benchmark and writes to rsa_u1_t65_1.txt
        python rsa_bench.py rsa_u1_t65_1.txt
'''
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast
import sys

NUM_OF_ITERATIONS = 10

# Reads plaintext from the "rsa_data.txt" file
f_in = open("rsa_data.txt", 'r')
lines = f_in.readlines()
f_in.close()

# Encrypts data with public key
f_out = open("../../../data/crypto/rsa/{}".format(sys.argv[1]), 'a')
keyIndex = 1
for line in lines:
    for i in range(NUM_OF_ITERATIONS):
        recipient_key = RSA.import_key(open("receiver{}.pem".format(keyIndex)).read())
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_plaintext = cipher_rsa.encrypt(bytes(ast.literal_eval(line)))
        f_out.write(str(list(enc_plaintext)) + "\n")
        keyIndex += 1
        if keyIndex % 5 == 0:
            keyIndex = 5
        else:
            keyIndex =  keyIndex % 5
    keyIndex = 1
f_out.close()


