#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/../../"

cd "$PROJECT_ROOT"

# Подгружаем .env
export $(grep -v '^#' .env | xargs)

source .venv/bin/activate

flask run --reload
