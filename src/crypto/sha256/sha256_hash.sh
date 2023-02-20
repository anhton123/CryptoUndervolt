#!/bin/bash
# Description: Script to run benchmark for SHA256 algorithim at desired temperature 
# Usage:   ./sha256_hash.sh <encrypted_file_name>.txt <temperature>
# Example: ./sha256_hash.sh sha256_u0_t65_1.txt 65


echo "Stress Test turned on...."

# Runs stress test until CPU temp is less than or equal to $2
while [ $(($(</sys/class/thermal/thermal_zone0/temp)/1000)) -lt $2 ]
do
    sudo stress --cpu 4 --timeout 2s -q
   # echo "CPU Temperature => $(($(</sys/class/thermal/thermal_zone0/temp)/1000))"
done
echo "Temperature reached $2'C"

python sha256_bench.py $1
echo "CPU Temperature after encryption => $(($(</sys/class/thermal/thermal_zone0/temp)/1000))'C"
