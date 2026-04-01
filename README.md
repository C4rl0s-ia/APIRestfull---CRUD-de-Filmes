# API de Cadastro de Filmes

## Visão geral

Este projeto é uma API REST para gerenciar filmes com as operações básicas de CRUD:
- criar filme
- listar filmes
- atualizar filme
- deletar filme

A aplicação foi escrita em Python usando FastAPI e salva os dados em um banco SQLite local.

## Estrutura do projeto

A arquitetura segue a separação em camadas:

- `app/controllers` → define rotas HTTP e trata requisições
- `app/services` → coordena a lógica de negócio
- `app/repositories` → acessa e manipula o banco de dados
- `app/models` → define a estrutura da tabela de filmes
- `app/schemas` → valida dados de entrada com Pydantic
- `app/database` → configura a conexão com SQLite

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Requisitos

- Python 3.8+
- Dependências do projeto:
  - fastapi
  - uvicorn
  - sqlalchemy
  - pydantic

## Como executar

1. Instale as dependências:

```bash
python -m pip install fastapi uvicorn sqlalchemy pydantic
```

2. Rode o servidor:

```bash
python -m uvicorn app.main:app --reload
```

3. Acesse a documentação automática:

```
http://127.0.0.1:8000/docs
```

## Endpoints disponíveis

### Criar filme

- Método: `POST`
- Rota: `/filmes`
- Corpo da requisição (JSON):

```json
{
  "titulo": "Vingadores",
  "genero": "Ação",
  "ano": 2012,
  "nota": 9
}
```

### Listar filmes

- Método: `GET`
- Rota: `/filmes`
- Retorna uma lista de filmes cadastrados.

### Atualizar filme

- Método: `PUT`
- Rota: `/filmes/{filme_id}`
- Substitui os dados do filme existente pelo conteúdo enviado.

### Deletar filme

- Método: `DELETE`
- Rota: `/filmes/{filme_id}`
- Remove o registro do filme com o ID informado.

## Modelagem do dado

O modelo de filme usa os campos:

- `id`: inteiro, chave primária
- `titulo`: string
- `genero`: string
- `ano`: inteiro
- `nota`: inteiro (0 a 10)

A validação do campo `nota` é aplicada no schema do Pydantic em `app/schemas/filme_schema.py`.

## Banco de dados

- Banco: SQLite
- Arquivo gerado: `filmes.db`
- Tabela: `filmes`

O banco é criado automaticamente ao iniciar a aplicação por meio de `Base.metadata.create_all(bind=engine)` em `app/main.py`.

## Tratamento de erros

- `POST /filmes` e `PUT /filmes/{filme_id}` validam os dados de entrada.
- `DELETE /filmes/{filme_id}` retorna `404` quando o filme não é encontrado.
- `PUT /filmes/{filme_id}` retorna `404` quando o filme não é encontrado.

## Imagens e exemplos visuais

A pasta `images/` contém capturas de tela das operações da API e exemplos de respostas:

- `Criando filme(POST).png`
- `Criando-filme-_POST-ERROR_.png`
- `Listando filme(GET).png`
- `Atualizando-filme_PUT_.png`
- `Deletando-filme_DELETE_.png`
- `Deletando-filme_DELETE-ERROR_.png`
- `image.png`

### Galeria de imagens

<img src="images/Criando filme(POST).png" alt="Criando filme POST" width="600">

<img src="images/Listando filme(GET).png" alt="Listando filmes GET" width="600">

<img src="images/Atualizando-filme_PUT_.png" alt="Atualizando filme PUT" width="600">

<img src="images/Deletando-filme_DELETE_.png" alt="Deletando filme DELETE" width="600">

<img src="images/Criando-filme-_POST-ERROR_.png" alt="Erro ao criar filme POST" width="600">

<img src="images/Deletando-filme_DELETE-ERROR_.png" alt="Erro ao deletar filme DELETE" width="600">

## Observações

- A API não possui autenticação.
- O foco é demonstrar o fluxo básico de CRUD com FastAPI e SQLAlchemy.
- Se você quiser, posso também ajudar a melhorar o tratamento de erros e o endpoint de atualização.

## Autores

Projeto desenvolvido por:

- Bruno Ferreira da Costa - 1240114845
- Bruno Lourenço Queiroz da Silva - 1240120417
- Carlos Augusto da Silva Souza - 1240101684
- Eduardo Rodrigues Gomes - 1240208119
- Gabriel Ribeiro - 1240113883
- Gabriel Vasconcelos - 1210102929
- Guilherme Ribeiro Alves - 1240200753
- Jamilly Dias Deodato - 1240205458
- João Vitor Hermes Fonseca Coelho - 1240112457
- João Victor Pereira dos Reis - 1240111812
- Lucas Rodrigues Correia - 1240105219
- Matheus de Souza - 1240100507
- Mauricio Gonçalves Simões Júnior - 1230103599
- Rafael Matias Alonso Carvalhal - 1240107511
- Victor Gusmão Moreira Vieira - 1260114525
