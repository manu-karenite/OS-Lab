#!/bin/bash

read -p "Enter the number of elements : " n
arr=()
i=1
while [[ $i -le $n ]]
do
    read -p "Enter the number : " x
    arr+=($x)
    i=`expr $i + 1`
done

read -p "Enter the number you want to replace  : " y
read -p "Enter the Replacement  : " z

i=0
while [[ $i -lt $n ]]
do
    curr=${arr[$i]}
    if [[ $curr -eq $y ]]
    then
        #replace now
        arr[$i]=$z
    fi

    i=`expr $i + 1`
done

echo "${arr[*]}"
    
