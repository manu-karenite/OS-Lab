#!/bin/bash

read -p "Enter the String  : " s

read -p "Enter the character you want to replace : " t

read -p "Enter the replacement character : " c

s=${s//[$t]/$c}
echo $s
