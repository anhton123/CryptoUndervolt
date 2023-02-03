#!/bin/bash
# Description: Script to find nominal voltage of cpu based on different cpu temperatures  
# Usage:   ./cpu_volt_temp.sh <temperature>
# Example: ./cpu_volt_temp.sh 65


echo "Stress Test turned on...."

# Runs stress test until CPU temp is less than or equal to $2
while [ $(($(</sys/class/thermal/thermal_zone0/temp)/1000)) -lt $1 ]
do
    sudo stress --cpu 4 --timeout 2s -q
   # echo "CPU Temperature => $(($(</sys/class/thermal/thermal_zone0/temp)/1000))"
done
echo "Temperature reached $1'C"


echo "CPU Voltage => $(vcgencmd measure_volts core)"
echo "CPU Clock => $(vcgencmd measure_clock arm)"
