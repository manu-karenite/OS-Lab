#!/bin/bash
echo "Enter the Number of elements in the array  : "
read n

arr=()
i=0

while [ $i -lt $n ]
do
    read x
    arr+=($x)
    i=`expr $i + 1`
done

echo "Enter the Number you want to Check : "
read x

index=0
i=0
while [ $i -lt $n ]
do
    curr=${arr[$i]}

    if [[ $curr -eq $x ]]
    then
        index=`expr $index + 1`
        i=`expr $i + 1`
    else
        i=`expr $i + 1`
    fi
done

echo "${x} has appeared ${index} times in ${arr[*]}"
