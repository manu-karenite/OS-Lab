#!/bin/bash

read -p "Enter the number you evaluate : " n

ans=1

i=1

while [[ $i -le $n ]]
do
    ans=`expr $ans \* $i`
    i=`expr $i + 1`
done

echo "Factorial of ${n} is ${ans}"