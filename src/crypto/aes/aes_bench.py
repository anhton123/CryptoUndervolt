'''
NAME:
    aes_bench.py

DESCRIPTION:
    This source file is used for running the benchmark for the guardband analysis of the AES GCM algorithim.

IMPLEMENTATION:
    This source file reads in a file called "aes_data.txt" to get the random valued operands (plaintext) and 
    a 16 byte key. It then takes these operands applies the AES GCM algorithim and writes the cipher,
    tag, and nonce to the <x>.txt NUM_OF_ITERATION times.  

USAGE:
    # runs the benchmark and writes to <x>.txt
        python aes_bench.py <x>.txt

EXAMPLE:
    # runs benchmark and writes to aes_u0_t60_1.txt
        python aes_bench.py aes_u0_t60_1.txt
'''

from Crypto.Cipher import AES
import ast
import sys

NUM_OF_ITERATIONS = 1000

# reads in plaintext and 16 byte key
f_in = open("aes_data.txt", 'r')
lines = f_in.readlines()
f_in.close()

# encrypts plaintext with key and writes cipher, tag, and nonce to <x>.txt
f_out = open("../../../data/crypto/aes/{}".format(sys.argv[1]), 'a') 
for line in lines:
    for i in range(NUM_OF_ITERATIONS):
        cipher = AES.new(bytes(ast.literal_eval(line.split("      ")[1])), AES.MODE_GCM)                # key
        ciphertext, tag = cipher.encrypt_and_digest(bytes(ast.literal_eval(line.split("      ")[0])))   # data
        f_out.write(str(list(ciphertext)) + "      "\
                  + str(list(tag)) + "      " \
                  + str(list(cipher.nonce)) + "\n") # ciphertext, tag, nonce
f_out.close() 
