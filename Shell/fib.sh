#!/bin/bash

read -p "Enter the number of terms : " t

a=0
b=1

if [[ $t -eq 1 ]]
then
    echo $a
elif [[ $t -eq 2 ]]
then
    echo $a $b
else
    #when we have more than two terms, we need to calculate.
    echo $a
    echo $b

    start=3
    while [[ $start -le $t ]]
    do
        c=`expr $a + $b`
        echo $c
        start=`expr $start + 1`
        a=$b
        b=$c
    done
fi



