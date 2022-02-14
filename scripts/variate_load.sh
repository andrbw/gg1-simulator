#!/bin/bash

file="result.dat"
rm -rf $file

echo "Lambda ServiceTimeMean ServiceTimeConfInterval" >> $file

parallel ./execute.py {1} 1 100000 --runMode static --beta 0.1 >> $file ::: 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
