'''
Name:
    operand_generate.py

Description:
    This file creates two random 32 bit operands NUM_OF_MULITIPLCATIONS times and writes
    those operands to <x>.txt

Usage:
    python operand_generate.py <x>.txt

Example:
    python operand_generate.py mul_op_u0_t50_1.txt
'''

import random
import sys

NUM_OF_MULTIPLICATIONS = 1000000

f_out = open("../../data/multiplication/{}".format(sys.argv[1]),'a')
for i in range(NUM_OF_MULTIPLICATIONS):
    x = random.randbytes(4)
    y = random.randbytes(4)
    f_out.write(str(x.hex()) + "      " + str(y.hex()) + "\n")
f_out.close()
