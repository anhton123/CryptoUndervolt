'''
NAME:
    sha256_bench.py

DESCRIPTION:
    This source file is used for running the benchmark for the sha256 hashing algorithim.


IMPLEMENTATION:
    This source file reads in a file called "sha256_data.txt" to get 10 operands. 
    It then takes these operands and writes the sha256 digest for each of the operands
    to the <x>.txt file 10,000 times.  

USAGE:
    # runs the benchmark and writes to <x>.txt:
        python sha256_bench.py <x>.txt   

EXAMPLE:
    # runs benchmark and writes to sha256_u0_t65_1.txt
        python sha256_bench.py sha256_u0_t65_1.txt
'''
from Crypto.Hash import SHA256
import ast
import sys

NUM_OF_ITERATIONS = 10000

# Reads contents of "sha256_data.txt" file
f_in = open("sha256_data.txt", 'r')
lines = f_in.readlines()
f_in.close()

# Writes the experimental digest to <t>.txt 
f_out = open("../../../data/benchmark/sha256/{}".format(sys.argv[1]), 'a')
for line in lines:
    for i in range(NUM_OF_ITERATIONS):
        h = SHA256.new()
        h.update(bytes(ast.literal_eval(line.split("      ")[0])))
        f_out.write(h.hexdigest() + "\n")
f_out.close() 