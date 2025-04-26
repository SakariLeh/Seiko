#!/bin/bash

VENV_DIR="$(dirname "$0")/.venv"
REQUIREMENTS="$(dirname "$0")/requirements.txt"

# Создаем виртуальное окружение, если его нет
if [ ! -d "$VENV_DIR" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    if [ -f "$REQUIREMENTS" ]; then
        echo "Установка зависимостей..."
        pip install -r "$REQUIREMENTS"
    fi
else
    source "$VENV_DIR/bin/activate"
    # Обновляем зависимости при изменении requirements.txt
    if [ -f "$REQUIREMENTS" ]; then
        echo "Проверка зависимостей..."
        pip install -r "$REQUIREMENTS" --upgrade
    fi
fi

# Запускаем Python-скрипт
python3 -u "$(dirname "$0")/run.py"

# Оставляем консоль открытой
read -p "Нажмите Enter для выхода..."