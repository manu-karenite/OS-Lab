#!/bin/bash

read -p "Enter the String you want to Verify  : " st

i=1
j=`expr length $st`

flag=0
while [[ $i -le $j ]]
do
    left=`expr substr $st $i 1`
    right=`expr substr $st $j 1`
    if [[ $left != $right ]]
    then
        flag=1
        i=`expr $j + 1`
    else
        i=`expr $i + 1`
        j=`expr $j - 1`
    fi

done

if [[ $flag == 0 ]]
then
    echo "${st} is a Palindrome!"
else
    echo "${st} is not a Palindrome!"
fi




