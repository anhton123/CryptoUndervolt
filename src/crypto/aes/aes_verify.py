'''
NAME:
    aes_verify.py

DESCRIPTION:
    This source file is used verify the deciphered AES cipher with the original plaintext.


IMPLEMENTATION:
    This source file reads the AES cipher from <x>.txt. It then compares the
    original plaintext from "aes_data.txt" with the decrypted ciphers from <x>.txt
    using the public key (found in "aes_data.txt"), tag and nonce (found in <x>.txt).
    If these values don't match, a fault has occured, and it would be logged to the aes_faults.csv.

USAGE:
    # verifies <x>.txt to see if any faults have occured
        python aes_verify.py <x>.txt   

EXAMPLE:
    # verifies aes_u0_t60_1.txt to see if any faults have occured
        python aes_verify.py aes_u0_t60_1.txt 
'''

from Crypto.Cipher import AES
import ast
import sys
import csv

parse = sys.argv[1].strip(".txt").split("_")
undervolt_level = parse[1][1:]
temperature = parse[2][1:]
NUM_OF_ITERATIONS = 1000

# Stores contents of plaintext and public key from the "aes_data.txt" file in variable x
f_expected = open("aes_data.txt", 'r')
x = f_expected.readlines()
f_expected.close()

# Stores contents ciphertext, tag, and nonce from the <t>.txt file in variable y
f_actual = open("../../../data/crypto/aes/{}".format(sys.argv[1]), 'r')
y = f_actual.readlines()
f_actual.close()

# Compares the plaintext with deciphered AES cipher
experimental_index = 0
expected_index = 1
flag = 0
try:
    for line in x:
        key = bytes(ast.literal_eval(line.split("      ")[1]))
        for i in range(NUM_OF_ITERATIONS):
            ciphertext = bytes(ast.literal_eval(y[experimental_index + i].split("      ")[0]))
            tag        = bytes(ast.literal_eval(y[experimental_index + i].split("      ")[1]))
            copy_nonce = bytes(ast.literal_eval(y[experimental_index + i].split("      ")[2]))
            cipher1 = AES.new(key, AES.MODE_GCM, nonce=copy_nonce)                      
            plaintext = cipher1.decrypt_and_verify(ciphertext, tag)
        experimental_index += NUM_OF_ITERATIONS
        expected_index += 1
# Writes to aes_faults.csv if fault is detected.
except ValueError:
    with open("aes_faults.csv", "a", newline='') as f:
        fieldnames = ["experimental_file.txt", "undervolt_level", "temperature",
                      "num_of_iterations", "plaintext", "public_key", 
                      "experimental_cipher", "experimental_tag", "experimental_nonce",
                      "line_of_fault","line_of_expected"]
        writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
        dictlist = {
            "experimental_file.txt" : sys.argv[1],
            "undervolt_level"       : undervolt_level,
            "temperature"           : temperature,
            "num_of_iterations"     : NUM_OF_ITERATIONS,
            "plaintext"             : line.split("      ")[0],
            "public_key"            : line.split("      ")[1].strip("\n"),
            "experimental_cipher"   : y[experimental_index + i].split("      ")[0],
            "experimental_tag"      : y[experimental_index + i].split("      ")[1],
            "experimental_nonce"    : y[experimental_index + i].split("      ")[2].strip("\n"),
            "line_of_expected"      : expected_index,
            "line_of_fault"         : experimental_index + i + 1,

        }
        writer.writerow(dictlist)
        flag = 1
    f.close()
if flag == 0:
    print("Success! No faults occured.")
else:
    print("Oh no! A fault occured.")

