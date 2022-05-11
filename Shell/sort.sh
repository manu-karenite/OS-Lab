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

i=0
k=0

while [[ $i -lt $n ]]
do
   j=$i
   
   while [[ $j -le $n ]]
   do
    curr=${arr[$j]}
    if [[ $curr -le ${arr[$i]} ]]
    then
        #swap here
        temp=${arr[$i]}
        arr[$i]=${arr[j]}
        arr[$j]=$temp
    fi
    j=`expr $j + 1`
    done
i=`expr $i + 1`
done

echo "The sorted Array is  : " ${arr[*]}

echo "The Smallest Number in Array is  : " ${arr[1]}
last=`expr $n - 1`
echo "The Largest Number in Array is  : " ${arr[$n]}

