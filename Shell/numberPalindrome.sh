#!/bin/bash

echo "Enter the number : "
read number

backup=$number

rev=0
armstrong=0
while [[ $backup -gt 0 ]]
do
    rem=`expr $backup % 10`
    quot=`expr $backup / 10`
    rev=`expr $rev \* 10 + $rem`
    armstrong=`expr $rem \* $rem \* $rem + $armstrong`
    backup=$quot
done

if [[ $rev -eq $number ]]
then
    echo "${number} is a Palindrome Number"
else
    echo "${number} is not a Palindrome Number"
fi


if [[ $armstrong -eq $number ]]
then
    echo "${number} is a Armstrong Number"
else
    echo "${number} is not a Armstrong Number"
fi



