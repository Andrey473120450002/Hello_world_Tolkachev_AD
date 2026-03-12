#!/bin/bash
read -p "Введите массу (г):" WEIGHT
read -p "Введите рост (cм):" HEIGHT
BMI=$(( (WEIGHT * 10) / (HEIGHT * HEIGHT) ))
echo "Метаболического индекса: $BMI"

