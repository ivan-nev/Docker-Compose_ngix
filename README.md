# Домашнее задание к лекции «Docker Compose»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория. 

## Задание* (необязательное)

Cделать конфигурацию docker-compose любого Вашего проекта из курса по Django, который использует БД (например, [CRUD: Склады и запасы](https://github.com/netology-code/dj-homeworks/tree/drf/3.2-crud/stocks_products)).

Результатом является `docker-compose.yml` файл с описанием конфигурации для развертывания приложения (и не забудьте про `Dockerfile`).

P.S. для создания конфигурации необходим образ своего проекта, а значит предварительно необходимо описать `Dockerfile`, сделать образ и потом уже писать `docker-compose.yml` (это типичный сценарий при работе с Docker и Docker Compose).

Созданные файлы отправьте в личном кабинете на сайте [netology.ru](https://netology.ru)

### Подсказка:

Конфигурация должна состоять из 3-х контейнеров: backend, postgres, nginx. 

Контейнеры объединяются в сеть, которые работают в связке:

- Nginx работает в качестве proxy-http для пересылки динамических запросов к Django или возвращая статические html файлы.
- PostgreSQL запускается до Django.
- Django запускается через Gunicorn.

после скачивания репозитория необходимо обновить права для файлов
- $ chmod +x app/entrypoint.prod.sh
- $ chmod +x app/entrypoint.sh

Остановка контейнера
- $ docker-compose down -v

Запуск контейнерa продакшн
- $ docker-compose -f docker-compose.prod.yml up -d --build
- $ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
- $ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
- http://<host>/admin/
- http://<host>/api/v1/

Запуск контейнера разработки без ngix (все изменения в папке app передаются сразу в контейнер)
- $ docker-compose -f docker-compose.yml up -d --build
- http://localhost:8000/admin/
- http://localhost:8000/api/v1/