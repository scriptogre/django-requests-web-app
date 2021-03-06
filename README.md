# Purchase Requisitions

Web application for automating Purchase Requisitions by sending mails for requisitioning approval.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Screenshots
[![Dashboard.png](https://i.postimg.cc/rF49GLT3/Dashboard.png)](https://postimg.cc/1f96P2fr)
[![Update-modal.png](https://i.postimg.cc/yxmkdnqQ/Update-modal.png)](https://postimg.cc/Wq42YG1g)
[![Requisitions-list.png](https://i.postimg.cc/CK91s9Sr/Requests-list.png)](https://postimg.cc/qtX4kbt2)
[![admin-login.png](https://i.postimg.cc/xTVm2Nrp/admin-login.png)](https://postimg.cc/dDn3R1VG)

## Features
1. **Modern Material Design** (including Django admin panel)
2. **Dashboard** (purchasing requisitions statistics, latest requisitions, users)
3. **Modal Popups** (create, edit, delete requisition dialog)
4. **DataTables integrated**

## TODO
1. Modal Popups (sign in, sign out)
2. Asynchronous CRUD requests
3. Finite State Machine App Design
4. Implement Celery


## Getting up and running locally

### Requirements
- [Docker](https://www.docker.com/products/docker-desktop/)

### Starting project
1. Clone repository & cd to project
```
git clone https://github.com/scriptogre/django-requisitions-web-app.git
cd ./django-requests-web-app/
```
2. docker-compose build & up
```
docker-compose -f local.yml build
docker-compose -f local.yml up
```
3. In your browser, go to "localhost:8000" or "127.0.0.1:8000" (0.0.0.0:8000 does not work)

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use these commands inside a terminal:
```
docker-compose -f local.yml run --rm django python manage.py migrate
```
```
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy purchase_requisitions

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd purchase_requisitions
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
