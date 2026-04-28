# 🚀 Automation QA Portfolio
![CI](https://github.com/VladimirBerg/AUTO_QA_portfolio/actions/workflows/tests.yml/badge.svg)

## Стек
Python - Pytest - Playwright - Requests - Allure - Docker - GitHub Actions

## Структура проекта

- **api/** — API тесты (JSONPlaceholder)
- **ui/** — UI тесты (Playwright)
- **config/** — Конфиги окружений
- **utils/** — Логгер
- **docker/** — Dockerfile
- **kafka/** — Kafka producer/consumer
- **grpc/** — gRPC сервер и клиент

## Быстрый старт

pip install -r requirements.txt
playwright install chromium
pytest -v

## Запуск групп тестов

pytest -m api -v
pytest -m ui -v

## Allure отчёт

pytest --alluredir=allure-results
allure serve allure-results

## Docker

docker-compose up --build
