#!/bin/bash
printf "%-20s %-8s %-8s %-8s %-8s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta; do
    [ -e "$file" ] || continue          # если нет файлов, выйти
    [ ! -s "$file" ] && continue        # пропустить пустые
    seq=$(grep -v "^>" "$file" | tr -d '\n' | tr 'a-z' 'A-Z')
    a=$(echo "$seq" | grep -o "A" | wc -l)
    t=$(echo "$seq" | grep -o "T" | wc -l)
    g=$(echo "$seq" | grep -o "G" | wc -l)
    c=$(echo "$seq" | grep -o "C" | wc -l)
    printf "%-20s %-8s %-8s %-8s %-8s\n" "$file" "$a" "$t" "$g" "$c"
done
