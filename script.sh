#!/bin/bash

#invoke the code.py file and store its output to an array a
mapfile -t a < <(python /home/sunny/r3m4ind3r/code.py)
#enumerate the array values and assign them to new variables
x=${a[0]}
y=${a[1]}
z=${a[2]}

#use zenity for GUI and place the above obtained data as needed.
zenity --info --text="Date: "$x"\nSubject: "$y"\nTopic: "$z --title="Remainder"
