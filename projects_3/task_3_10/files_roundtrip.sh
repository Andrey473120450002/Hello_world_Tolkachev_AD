#!/bin/bash
for i in {1..10}; do
    touch "test${i}.txt"
    echo "created test${i}.txt"
done
while [ $i -ge 1 ]; do
    rm "test${i}.txt"
    echo "rempved test${i}.txt"
    i=$((i-1))
done
