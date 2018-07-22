#Eventex

Sistema de Eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python3.5
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure as instancias do .env
6. Execute os testes.

'''console
git clone git@github.com:henriquebastos/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate   
pip instal -r requirements.txt
cp contrib/env-semple .env
python manage.py test
'''

## Como fazer o deploy

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instancia.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

'''console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configura o email
git push heroku master --force
'''

