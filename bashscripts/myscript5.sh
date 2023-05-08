#!/bin/bash

summa=0

myFunction()
{
	echo "This is text from Function!!"
	echo "Num1= $1"
	echo "Num2= $2"
summa=$(($1+$2))
}

myFunction 10 50
echo "Summa = $summa" 
