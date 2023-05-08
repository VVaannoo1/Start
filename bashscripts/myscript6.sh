#!/bin/bash

echo -n "Enter first number: "
read n1

if [ -z "${n1// /}" ]
then 
	echo "You didn't enter number"
	exit
fi

if [[ "$n1" =~ [a..z] ]]
then
echo "Number, Bitch!"
exit
fi

echo -n "Enter second numer: "
read n2
if [ -z "${n2// /}" ]
then
	echo "You didn't enter number"
	exit
fi

sum=$(($n1 +$n2))

echo "The sum of two numbers="$sum
