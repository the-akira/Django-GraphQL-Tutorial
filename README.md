# Django GraphQLAPI Tutorial

Neste guia vamos desenvolver uma GraphQLAPI com o framework Django através do auxílio da biblioteca Graphene.

**[Leia o Tutorial](https://akiradev.netlify.app/posts/django-graphql-api/)**

---

## Instalação

### Clone o Repositório

```
git clone https://github.com/the-akira/Django-GraphQL-Tutorial.git
```

### Dentro do Diretório Principal

Crie um Ambiente Virtual

```
python -m venv myvenv
```

Ative o Ambiente Virtual

```
source myvenv/bin/activate
```

Instale os Requeriments

```
pip install -r requirements.txt
```

Sincronize o banco de dados

```
python manage.py migrate
```

Execute a aplicação

```
python manage.py runserver
```

Navegue até `http://127.0.0.1:8000/graphql/` para executar as Queries.