#!/bin/bash

arr=()
read -p "Enter the number of terms  : " n

i=1
while [[ $i -le $n ]]
do
    read -p "Enter the term number ${i} : " x
    arr+=($x)
    i=`expr $i + 1`
done


echo ${arr[*]}
sum=0

i=0
while [[ $i -lt $n ]]
do
    curr=${arr[$i]}
    sum=`expr $sum + $curr`
    i=`expr $i + 1`
done

echo "${arr[*]} sum is :  ${sum}"
