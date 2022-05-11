#!/bin/bash

read -p "Please Enter the String you want to Check  : " s

read -p "Please Enter the Character you want to Count : " c

l=`expr length $c`
freq=0
if [[ $l != 1 ]]
then
    echo "Please Enter a Single Character.. Try Again"
else
    #means 1 char is there
    i=1
    last=`expr length "$s"`
    
    while [[ $i -le $last ]]
    do
        char=`expr substr "$s" $i 1`
        if [[ $char == $c ]]
        then
            freq=`expr $freq + 1`
        fi
        i=`expr $i + 1`
    done
fi

echo "${s} contains ${c} for ${freq} number of times!"