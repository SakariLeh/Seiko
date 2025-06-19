@echo off
setlocal enabledelayedexpansion

cd /d %~dp0\..\..

REM Загрузка переменных из .env.dev
for /f "tokens=1,2 delims==" %%a in ('.env.dev') do (
    set "%%a=%%b"
)

call venv\Scripts\activate

gunicorn -w 4 -b %FLASK_RUN_HOST%:%FLASK_RUN_PORT% %FLASK_APP:.py=%:app
