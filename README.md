Задача
· 	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
· 	Django Модель Item с полями (name, description, price)
· 	API с двумя методами:
· 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
· 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
· 	Запуск используя Docker
· 	Использование environment variables
· 	Просмотр Django Моделей в Django Admin панели
· 	Запуск приложения на удаленном сервере, доступном для тестирования
· 	Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
· 	Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
· 	Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
· 	Реализовать не Stripe Session, а Stripe Payment Intent.


## **Запуск**

Склонируйте репозиторий:

```https://github.com/Konstantin-Lanin-it/OOO_PR_RE_PYTHON_DJANGO.git```

Перейдите в папку Django-Stripe-Test-Task:

```cd OOO_PR_RE_PYTHON_DJANGO```

Создайте новое виртуальное окружение:

```python -m venv venv```

Установите зависимости:

```pip install -r requirements.txt```

Выполните миграции:

```python manage.py migrate```

Создайте суперпользователя для доступа к панели администратора:

```python manage.py createsuperuser```

Создайте файл `.env` в котором должны быть указаны следующие переменные окружения:

```SECRET_KEY = секретный ключ Django```

```DEBUG = True/False```

```STRIPE_PUBLISHABLE_KEY = Публичный ключ Stripe```

```STRIPE_SECRET_KEY = Секретный ключ Stripe```

Запустите сервер:

```python manage.py runserver```

Откройте браузер и перейдите по адресу:

```http://127.0.0.1:8000```

Для добавления товаров перейдите в панель администратора и добавьте новые записи во вкладке "Товары":

```http://127.0.0.1:8000/admin```

### **Запуск в Docker**

В папке Django-Stripe-Test-Task выполните следующую команду:

```docker-compose up --build```

Откройте браузер и перейдите по адресу:

```http://127.0.0.1:8000```


