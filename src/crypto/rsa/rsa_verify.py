'''
NAME
    rsa_verify.py

DESCRIPTION:
    This source file is used verify the deciphered rsa cipher with the original plaintext.

IMPLEMENTATION:
    This source file reads the rsa cipher from <x>.txt. It then compares the
    original plaintext from "rsa_data.txt" with the decrypted ciphers from <x>.txt
    using the private key files (privateX.pem). If these values don't match, a fault has occured,
    and it would be logged to the rsa_faults.csv.

USAGE:
    # verifies <x>.txt to see if any faults occured.
        python rsa_verify.py <x>.txt   

EXAMPLE:
    # verifies rsa_u1_t60_1.txt to see if any faults occured.
        python rsa_verify.py rsa_u1_t60_1.txt
'''
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast
import sys
import csv

parse = sys.argv[1].strip(".txt").split("_")
undervolt_level = parse[1][1:]
temperature = parse[2][1:]
NUM_OF_ITERATIONS = 10

# Stores contents of original plaintext in variable f1
f_expected = open("rsa_data.txt", 'r')
f1 = f_expected.readlines()
f_expected.close()

# Stores contents of experimental rsa cipher in variable f2
f_experimental = open("../../../data/crypto/rsa/{}".format(sys.argv[1]), 'r')
f2 = f_experimental.readlines()
f_experimental.close()

# Compares the original plaintext with the deciphered rsa ciphers
experimental_index = 0
expected_index = 1
flag = 0
keyIndex = 1
try:
    for line in f1:
        for i in range(NUM_OF_ITERATIONS):
            private_key = RSA.import_key(open("private{}.pem".format(keyIndex)).read())
            cipher_rsa = PKCS1_OAEP.new(private_key)
            if bytes(ast.literal_eval(line)) != cipher_rsa.decrypt(bytes(ast.literal_eval(f2[experimental_index + i]))):
                print(keyIndex)
                raise ValueError
            keyIndex += 1
            if keyIndex % 5 == 0:
                keyIndex = 5
            else:
                keyIndex =  keyIndex % 5
        experimental_index += NUM_OF_ITERATIONS
        expected_index += 1
        keyIndex = 1

except ValueError:
    with open("rsa_faults.csv", "a", newline='') as f:
        fieldnames = ["experimental_file.txt", "undervolt_level", "temperature",
                      "num_of_iterations", "plaintext", "public_key_file", "private_key_file",
                      "experimental_cipher", "line_of_fault","line_of_expected"]
        writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
        dictlist = {
            "experimental_file.txt" : sys.argv[1],
            "undervolt_level"       : undervolt_level,
            "temperature"           : temperature,
            "num_of_iterations"     : NUM_OF_ITERATIONS,
            "plaintext"             : line.strip("\n"),
            "public_key_file"       : "receiver{}.pem".format(keyIndex),
            "private_key_file"      : "private{}.pem".format(keyIndex),
            "experimental_cipher"   : "Wrong Decryption!",
            "line_of_expected"      : expected_index,
            "line_of_fault"         : experimental_index + i + 1,
        }
        writer.writerow(dictlist)
        flag = 1
    f.close()
  
if flag == 0:
    print("Success! No Faults Occured")
else:
    print("Oh no! Fault occured")