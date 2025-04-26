@echo off

set "VENV_DIR=%~dp0.venv"
set "REQUIREMENTS=%~dp0requirements.txt"

:: Проверяем наличие виртуального окружения
if not exist "%VENV_DIR%" (
    echo Создание виртуального окружения...
    python -m venv "%VENV_DIR%"
    call "%VENV_DIR%\Scripts\activate.bat"
    if exist "%REQUIREMENTS%" (
        echo Установка зависимостей...
        pip install -r "%REQUIREMENTS%"
    )
) else (
    call "%VENV_DIR%\Scripts\activate.bat"
    :: Обновление зависимостей при изменении requirements.txt
    if exist "%REQUIREMENTS%" (
        echo Проверка зависимостей...
        pip install -r "%REQUIREMENTS%" --upgrade
    )
)

:: Запуск Python-скрипта
python -u "%~dp0run.py"

:: Оставить консоль открытой
pause