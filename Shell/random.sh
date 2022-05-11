#!/bin/bash

echo "Enter the Number of Random Numbers : "
read Numbers

arr=()

i=0
while [[ $i -lt $Numbers ]]
do
    arr+=($RANDOM)
    i=`expr $i + 1`
done

echo "The Random Numbers are : ${arr[*]}"