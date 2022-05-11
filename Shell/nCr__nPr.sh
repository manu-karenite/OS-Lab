#!/bin/sh
fact(){
    __arg1=$1
    ans=1
    i=2
    while [ $i -le $__arg1 ]
    do
        ans=`expr $i \* $ans`
        i=`expr $i + 1`
    done
    echo $ans
}

echo "Enter the value of n : "
read n
echo "Enter the value of r : "
read r

#assuming n and r are valid...

a=$(fact $n)
b=$(fact $r)
c=$(fact `expr $n - $r`)

denom=`expr $b \* $c`
ans=`expr $a / $denom`
ans1=`expr $a / $b`

echo "Value of ${n}C${r} is ${ans}"
echo "Value of ${n}P${r} is ${ans1}"




