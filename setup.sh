#!/bin/bash

echo 'Установка HDI'

# Поиск HDI
HDI_PATH=$(find . -name "HDI.py" -type f | head -n 1)


if [ -z "$HDI_PATH" ]; then
    echo "Ошибка: файл HDI.py не найден!"
    exit 1
fi

# Удаляем имя файла, оставляем только директорию
HDI_DIR="${HDI_PATH%/*}"

# Создание конечной директории
TARGET_DIR="$HOME/.hdi"
mkdir -p "$TARGET_DIR" || {
    echo "Ошибка: не удалось создать директорию $TARGET_DIR"
    exit 1
}

# Копирование файлов 
cp "$HDI_PATH" "$TARGET_DIR/hdi.py" || {
    echo "Ошибка: не удалось скопировать HDI.py"
    exit 1
}

# Шаг 4: Создание пустых конфигурационных и загрузочных файлов файлов
touch "$TARGET_DIR/config.conf"
touch "$TARGET_DIR/boot.fms"

echo "Созданы файлы:"
echo "  $TARGET_DIR/config.conf"
echo "  $TARGET_DIR/boot.fms"

# Добавление алиаса в .bashrc
ALIAS_LINE="alias hdi='cd \"$TARGET_DIR\" && python hdi.py && cd -'"


# Проверяем, есть ли уже такой алиас
if ! grep -q "alias hdi" "$HOME/.bashrc"; then
    echo "$ALIAS_LINE" >> "$HOME/.bashrc"
    echo "Алиас 'hdi' добавлен в .bashrc"
else
    echo "Алиас 'hdi' уже существует в .bashrc"
fi

# Уведомление пользователя
echo ""
echo "Настройка завершена!"
echo ""
echo "Теперь можно запускать файловый менеджер командой:"
echo "  hdi"
echo ""
echo "Конфигурационные файлы:"
echo "  $TARGET_DIR/config.conf  # для настроек"
echo "  $TARGET_DIR/boot.fms     # для загрузочных параметров"
source $HOME/.bashrc
