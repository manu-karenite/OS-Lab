#read n numbers and display its square as 'i square = j'
#!/bin/sh

echo "Enter the number of terms : "
read n
#create an array of numbers
arr=()

i=0
while [ $i -lt $n ]
do
    read x
    arr+=($x)
    i=`expr $i + 1`
done

square=()

i=0
while [ $i -lt $n ]
do
    sq=`expr ${arr[$i]} \* ${arr[$i]}`
    square+=($sq)
    i=`expr $i + 1`
done
echo "The Numbers Entered Were : " ${arr[*]}
echo "The Squares Calculated Are : " ${square[*]}

