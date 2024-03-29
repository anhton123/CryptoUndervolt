'''
NAME:
    sha256_verify.py

DESCRIPTION:
    This source file is used verify the expected sha256 digests with the sha256 digests generated
    in the benchmark (sha256_bench.py).

IMPLEMENTATION:
    This source file reads in the expected sha256 digests from the "sha256_data.txt".
    It then reads in the sha256 digests generated from <x>.txt. If any of the expected digests
    doesn't equal to the appropriate experimental digests, a fault has occured, and it will be
    logged to sha256_faults.csv.

USAGE:
    # verifies <x>.txt to see if any faults have occured
        python sha256_verify.py <x>.txt  

EXAMPLE:
    # verifies sha256_u0_t65_1.txt to see if any faults have occured
        python sha256_verify.py sha256_u0_t65_1.txt
'''
import sys
import csv

parse = sys.argv[1].strip(".txt").split("_")
undervolt_level = parse[1][1:]
temperature = parse[2][1:]
NUM_OF_ITERATIONS = 10000

# Stores contents of expected digests in variable x
f_expected = open("sha256_data.txt", 'r')
x = f_expected.readlines()
f_expected.close()

# Stores contents of experimental experimental digests in variable y
f_actual = open("../../../data/crypto/sha256/{}".format(sys.argv[1]), 'r')
y = f_actual.readlines()
f_actual.close()

# Compares the expected digets and experimental digests
experimental_index = 0
expected_index = 1
flag = 0
try:
    for line in x:
        for i in range(NUM_OF_ITERATIONS):
            if line.split("      ")[1] != y[experimental_index + i]:
                raise ValueError()
        experimental_index += NUM_OF_ITERATIONS
        expected_index += 1
except ValueError:
    with open("sha256_faults.csv", "a", newline='') as f:
        fieldnames = ["experimental_file.txt", "undervolt_level", "temperature",
                      "num_of_iterations", "plaintext", "expected_digest", 
                      "experimental_digest", "line_of_expected", "line_of_fault", "xor"]
        writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
        dictlist = {
            "experimental_file.txt" : sys.argv[1],
            "undervolt_level"       : undervolt_level,
            "temperature"           : temperature,
            "num_of_iterations"     : NUM_OF_ITERATIONS,
            "plaintext"             : line.split("      ")[0],
            "expected_digest"       : "0x" + line.split("      ")[1].strip("\n"), 
            "experimental_digest"   : "0x" + y[experimental_index + i].strip("\n"),
            "line_of_expected"      : expected_index,
            "line_of_fault"         : experimental_index + i + 1,
            "xor"                   : "0x" + str(hex(int(line.split("      ")[1].strip("\n"), 16) ^ int(y[experimental_index + i].strip("\n"), 16)))[2:].zfill(64),
        }
        writer.writerow(dictlist)
        flag = 1
    f.close()
if flag == 0:
    print("Success! No Faults Occured")
else:
    print("Oh no! Fault Occured.")