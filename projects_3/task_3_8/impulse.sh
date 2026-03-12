#!/bin/bash
if [ $# -lt 2 ]; then echo "Ошибка! Нужно 2 аргумента"; exit 1; fi
GENE="$1"
LEVEL="$2"
echo "Экспрессия гена $1 составляет $2 единиц"