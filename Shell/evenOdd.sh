#!/bin/bash

read -p "Enter the number you want to Check : " number

rem=`expr $number % 2`

if [[ $rem -eq 0 ]]
then
    echo "${number} is an Even Number"
else
    echo "${number} is an Odd Number"
fi

