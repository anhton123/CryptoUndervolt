'''
Name:
    mul_bench.py

Description:
    This file reads in 32 bit operands from <x>.txt times and writes the multiplication
    of those operands to <y>.txt.

Usage:
    python mul_bench.py <x>.txt <y>.txt

Example:
    python mul_bench.py mul_op_u0_t50_1.txt mul_bench_u0_t50_1.txt
'''

import sys

# reads in the operands from <x>.txt
f_in = open("../../data/multiplication/{}".format(sys.argv[1]),'r')
lines = f_in.readlines()
f_in.close()

# writes multiplication of the operands to <y>.txt
f_out = open("../../data/multiplication/{}".format(sys.argv[2]), 'a')
for line in lines:
    operand1 = int(line.strip("\n").split("      ")[0],16)
    operand2 = int(line.strip("\n").split("      ")[1],16)
    f_out.write(str(operand1 * operand2) + "\n")
f_out.close()
