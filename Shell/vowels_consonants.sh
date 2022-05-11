#!/bin/bash

echo "Enter the String you want to inspect : "
vowels=[aeiouAEIOU]
number=[0123456789]
read s 
echo "$s"
v=0
n=0
ws=0
c=0

i=1

while [[ $i -le `expr length "$s"` ]]
do
    char=`expr substr "$s" $i 1`
    if [[ $char =~ $vowels ]]
    then
        v=`expr $v + 1`
    elif [[ $char =~ $number ]]
    then
        n=`expr $n + 1`
    elif [[ $char == " " ]]
    then
        ws=`expr $vs + 1`
    else
        c=`expr $c + 1`
    fi
    i=`expr $i + 1`
done

echo "${s} has ${v} Vowels, ${n} Numbers, ${c} Consonants and ${ws} Whitespaces"


