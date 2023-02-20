'''
Name:
    mul_verify.py

Description:
    This file reads in 32 bit operands from operand.txt, finds the multiplication of 
    those operands, and then compares that value with the experimental multiplcations
    of those operands to <y>.txt.

Usage:
    python mul_verify.py <y>.txt

Example:
    python mul_verify.py mul_bench_u0_t50_1.txt
'''

import sys
import csv

NUM_OF_MULTIPLICATIONS = 1000000

parse = sys.argv[1].split("_")
undervolt_level = parse[2][1:]
temperature = parse[3][1:]

# reads in the 32 bit random operands
f_in1 = open("operand.txt",'r')
data = f_in1.readlines()
f_in1.close()

# reads in the experimental multiplication values
f_in2 = open("../../data/multiplication/{}".format(sys.argv[1]), 'r')
exper = f_in2.readlines()
f_in2.close()

def log():
    global flag
    with open("mul_faults.csv", 'a', newline='') as f:
        fieldnames = [ "operand_file.txt", "experimental_file.txt", "undervolt_level",
                        "temperature", "operand1", "operand2", "expected", "experimental",
                        "line_of_fault", "xor"]
        writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
        dictlist = {
            "operand_file.txt"     : sys.argv[1],
            "experimental_file.txt": sys.argv[2], 
            "undervolt_level"      : undervolt_level,           
            "temperature"          : temperature, 
            "operand1"             : "0x" + str(data[i].strip("\n").split("      ")[0]), 
            "operand2"             : "0x" + str(data[i].strip("\n").split("      ")[1]), 
            "expected"             : str(hex(expected)), 
            "experimental"         : str(hex(experimental)),
            "line_of_fault"        : i + 1, 
            "xor"                  : str(hex(expected ^ experimental)),
        }
        writer.writerow(dictlist)
        flag = 1
    f.close()

flag = 0

for i in range(NUM_OF_MULTIPLICATIONS):
    expected = int(data[i].strip("\n").split("      ")[0],16) * int(data[i].strip("\n").split("      ")[1],16)
    experimental = int((exper[i].strip("\n")))
    if ((expected ^ experimental) != 0):    # fault occured
        log()                           

if flag == 0:
    print("Success! No faults detected.")
else:
    print("Oh no! Fault occured.")
