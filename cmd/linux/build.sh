#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/../../"

cd "$PROJECT_ROOT"

# Подгружаем .env.dev
export $(grep -v '^#' .env.dev | xargs)

source venv/bin/activate

exec gunicorn -w 4 -b $FLASK_RUN_HOST:$FLASK_RUN_PORT ${FLASK_APP%%.py}:app
