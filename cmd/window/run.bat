@echo off
setlocal enabledelayedexpansion

cd /d %~dp0\..\..

REM Загрузка переменных из .env.dev
for /f "tokens=1,2 delims==" %%a in ('.env.dev') do (
    set "%%a=%%b"
)

call venv\Scripts\activate

flask run
