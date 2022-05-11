#!/bin/bash

echo "Enter the number to check : "
read number

flag=false
i=2
while [[ $i -lt $number ]]
do
    rem=`expr $number % $i`
    #$echo $rem
    if [[ $rem -eq 0 ]]
    then
        flag=true
        i=`expr $i + $number`
    fi

    i=`expr $i + 1`
done

#echo $flag
if [[ $flag == "false" ]]
then
    echo "${number} is a Prime Number"
else
    echo "${number} is not a Prime Number"
fi
