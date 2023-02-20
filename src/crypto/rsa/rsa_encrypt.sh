#!/bin/bash
# Description: Script to run benchmark for RSA algorithim at desired temperature 
# Usage:   ./rsa_encrypt.sh <encrypted_file_name>.txt <temperature>
# Example: ./rsa_encrypt.sh rsa_u0_t60_1.txt 60


echo "Stress Test turned on...."

# Runs stress test until CPU temp is less than or equal to $2
while [ $(($(</sys/class/thermal/thermal_zone0/temp)/1000)) -lt $2 ]
do
    sudo stress --cpu 4 --timeout 2s -q
   # echo "CPU Temperature => $(($(</sys/class/thermal/thermal_zone0/temp)/1000))"
done
echo "Temperature reached $2'C"

python rsa_bench.py $1
echo "CPU Temperature after encryption => $(($(</sys/class/thermal/thermal_zone0/temp)/1000))'C"