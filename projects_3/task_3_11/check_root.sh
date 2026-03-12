#!/bin/bash

check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "Ошибка: скрипт должен быть запущен от root (UID=0)." >&2
        exit 1
    fi
}

check_root
