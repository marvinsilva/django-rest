# Django Rest Framework
Criando Uma API Rest Utilizando Django Rest Framework
___

[![Build Status](https://travis-ci.org/marvinsilva/django-rest.svg?branch=master)](https://travis-ci.org/marvinsilva/django-rest)
[![codecov](https://codecov.io/gh/marvinsilva/django-rest/branch/master/graph/badge.svg)](https://codecov.io/gh/marvinsilva/django-rest)
[![Updates](https://pyup.io/repos/github/marvinsilva/django-rest/shield.svg)](https://pyup.io/repos/github/marvinsilva/django-rest/)
[![Python 3](https://pyup.io/repos/github/marvinsilva/django-rest/python-3-shield.svg)](https://pyup.io/repos/github/marvinsilva/django-rest/)

Aplicação disponível em: https://djangorestmyapi.herokuapp.com/
___

Para instalar:

```console
env:
  global:
    - PIPENV_VENV_IN_PROJECT=1
    - PIPENV_IGNORE_VIRTUALENVS=1

install:
  - pip install pipenv
```
No repositório do projeto:
```console
  - pipenv sync -d
  - cp contrib/env-sample .env
```

Para conferir a qualidade de código:
```console
  - pipenv run flake8
  - pipenv run pytest --cov=myapi
```

Django app:
```console
  - pipenv run python manage.py makemigrations
  - pipenv run python manage.py migrate
  - pipenv run python manage.py collectstatic
  - pipenv run python manage.py createsuperuser
  - pipenv run python manage.py runserver
```

Referências:
- https://www.django-rest-framework.org/
- https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa

 [ ~ Dependencies scanned by PyUp.io ~ ]
