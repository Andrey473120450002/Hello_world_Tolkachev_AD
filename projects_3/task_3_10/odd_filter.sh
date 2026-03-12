#!/bin/bash

for (( i=1; i<=20; i++ )); do
    if [ $((i % 2)) -eq 0 ]; then
        continue  
    fi

    echo "Нечётное число: $i"

    if [ $i -eq 15 ]; then
        echo "15..."
        break     
    fi
done
