#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip; pip install poetry;  # 重新安装一下最新的 Poetry，因为默认的 Poetry 的版本比较低。
poetry install

python manage.py collectstatic --no-input
python manage.py migrate