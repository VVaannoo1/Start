#!/bin/bash
if [ "$1" == "Fedia" ]; then
	echo "Privet $1"
elif [ "$1" == "John" ]; then
	echo "Hello $1"
else echo "Salam $1"
fi

read -p "Enter Something:" x

echo "Starting CASE selection..."
case $x in
	1) echo "This is one";;
	[2-9]) echo "Two-Nine";;
"Petia") echo "Privet $x";;
*) echo "Parameter Unknown, sorry!"
esac
