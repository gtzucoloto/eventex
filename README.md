# Eventex

Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.com/gtzucoloto/eventex.svg?branch=master)](https://travis-ci.com/gtzucoloto/eventex)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com o Python 3.9.
3. Ative o seu virtualenv.
4. Instale as suas dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:gtzucoloto/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minha_instancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```
