# Luiza Labs Django Coding Test

[![Build Status](https://travis-ci.org/pigaov10/desafio.svg?branch=master)](https://travis-ci.org/pigaov10/desafio)


### Linguagem / Framework / Banco de dados
* [Python 3.6] - https://www.python.org/
* [Django 1.11.5] - https://www.djangoproject.com/
* [Django REST] - http://www.django-rest-framework.org/
* [SQLite] - https://www.sqlite.org/

### Ferramentas auxiliares
* [conda] - https://anaconda.org/anaconda/python
* [nose] - http://nose.readthedocs.io/en/latest/
* [coverage] - https://coverage.readthedocs.io/en/coverage-4.4.1/
* [pyflakes] - https://pypi.python.org/pypi/pyflakes
* [pylint] - https://www.pylint.org/

### Instalação
* Crie um virtualenv e.g `$ conda create --name myenv python=3.6`
* Ative o virtualenv e.g `$ source activate myenv`
* Clone o repositório  `$ git clone https://github.com/pigaov10/desafio.git luizalabs; cd luizalabs`
* Instale as dependencias `$ pip install -r requirements.txt`

### Migração
```sh
$ cd builder
$ python manage.py makemigrations manager
$ python manage.py migrate
$ python manage.py createsuperuser
```

### Linters
```sh
$ pyflakes .
$ pylint .
$ pep8 .
```

### Testes
```sh
$ python manage.py test manager/tests.py --with-coverage
```

### Inicie o servidor e acesse o Admin Employee
```sh
$ python manage.py runserver
```

> <http://127.0.0.1:8000/admin/>
> Entre com o usuário que foi cadastrado no createsuperuser
> Cadastre um Departamento e um Employee, após isso você poderá acessar a API

### API

> Via Browser, você poderá acessar o Admin do Django REST Framework
> http://127.0.0.1:8000/employees/
> Via Curl adicione o comandos abaixo: (Obs: Autenticacao é feita com usuario do ADMIN)

#### Lista todos os Employee

| RESPONSE | CODE |
| ------ | ------ |
| OK | HTTP_20O_SUCCESS |
| ERRO | HTTP_400_BAD_REQUEST |

```sh
$ curl -X GET \
  http://127.0.0.1:8000/employees/ \
  -u <username>:<password>
```

#### Lista Específico Employee

| RESPONSE | CODE |
| ------ | ------ |
| OK | HTTP_20O_SUCCESS |
| ERRO | HTTP_404_NOT_FOUND |


```sh
$ curl -X GET \
  http://127.0.0.1:8000/employee/<id>/ \
  -u <username>:<password>
```

#### Deletar Específico Employee

| RESPONSE | CODE |
| ------ | ------ |
| OK | HTTP_204_NO_CONTENT |
| ERRO | HTTP_400_BAD_REQUEST |

```sh
$ curl -X DELETE \
  http://127.0.0.1:8000/employee/<id>/ \
  -u <username>:<password>
```

#### Criar Employee

| RESPONSE | CODE |
| ------ | ------ |
| OK | HTTP_201_CREATED  |
| ERRO | HTTP_400_BAD_REQUEST |

```sh
$ curl -X POST http://127.0.0.1:8000/employees/ \
  -u <username>:<password>  \
  -d "name=Albert Einstein&email=einstein1907@relatividade.com&department_id=1"

Resposta:

{
    "name": "Albert Einstein",
    "department": {
        "department_id": 1,
        "name": "RH"
    },
    "email": "einstein1907@relatividade.com",
    "employee_id": 4
}

```

### Acesso Negado
```sh
{"detail":"Authentication credentials were not provided."}
```

### Usuário já cadastrado
```sh
{
    "email": [
        "employee with this email already exists."
    ]
}
```
