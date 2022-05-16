#!/bin/bash
# Description: Script to run multiplication benchmark at desired temperature
# Usage: ./mul.sh <operand_file>.txt <experimental_multiplication_file>.txt <temperature>
# Example: ./mul.sh mul_op_u0_t50_1.txt mul_bench_u0_t50_1.txt 50


echo "Stress Test turned on...."

# Runs stress test until CPU temp is less than or equal to $3
while [ $(($(</sys/class/thermal/thermal_zone0/temp)/1000)) -lt $3 ]
do
    sudo stress --cpu 4 --timeout 2s -q
done
echo "Temperature reached $3'C"

python mul_bench.py $1 $2
echo "CPU Temperature after multiplication => $(($(</sys/class/thermal/thermal_zone0/temp)/1000))'C"
echo "CPU Clock => $(vcgencmd measure_clock arm)"