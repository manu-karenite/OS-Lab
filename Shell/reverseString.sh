#!/bin/bash

read -p "Enter the String to Reverse : " st

#reverse
out=$(rev<<<"${st}")
echo $out