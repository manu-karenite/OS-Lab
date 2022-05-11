#!/bin/bash

read -p "Enter the limit of numbers : " n

arr=()

i=2
while [[ $i -le $n ]]
do

    flag=0 #0 means prime...
    j=2
    while [[ $j -lt `expr $i - 1` ]]
    do
        rem=`expr $i % $j`
        if [[ $rem -eq 0 ]]
        then
            #we can declare as a composite number...
            arr+=($i)
            j=`expr $i + 1`

        else
            j=`expr $j + 1`
        fi
    done
    
    i=`expr $i + 1`
done

echo ${arr[@]}
    

    

        

