# API de Cadastro de Filmes

## Descrição

Este projeto foi desenvolvido com o objetivo de criar uma API REST para gerenciamento de filmes, utilizando Python e FastAPI.

A aplicação permite realizar operações de cadastro, listagem, atualização e exclusão de filmes, seguindo uma arquitetura em camadas e boas práticas de desenvolvimento.

---

## Tecnologias Utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## Arquitetura do Projeto

O projeto foi estruturado em camadas:

* **Controller** → recebe requisições HTTP
* **Service** → lógica de negócio
* **Repository** → acesso ao banco de dados
* **Model** → estrutura da tabela
* **Schema** → validação de dados

---

## Como Executar o Projeto

### 1. Instalar dependências

```bash
python -m pip install fastapi uvicorn sqlalchemy pydantic
```

### 2. Executar o servidor

```bash
python -m uvicorn app.main:app --reload
```

### 3. Acessar a API

Abra no navegador:

```
http://127.0.0.1:8000/docs
```

---

## Funcionalidades (CRUD)

### Criar Filme

* **POST /filmes**

### Listar Filmes

* **GET /filmes**

### Atualizar Filme

* **PUT /filmes/{filme_id}**

### Deletar Filme

* **DELETE /filmes/{filme_id}**

---

## Exemplo de Requisição

```json
{
  "titulo": "Vingadores",
  "genero": "Ação",
  "ano": 2012,
  "nota": 9
}
```

## Testes da API


### Criando um filme (POST)


### Listando filmes (GET)


### Atualizando filme (PUT)


### Deletando filme (DELETE)


### Erro 404


---

## Validações

* A nota do filme deve estar entre **0 e 10**
* Retorna erro **404** caso o filme não seja encontrado

---

## Objetivo do Projeto

Este projeto foi desenvolvido como atividade da disciplina de Laboratório de Desenvolvimento de Software, com o objetivo de aplicar conceitos como:

* Desenvolvimento de APIs REST
* Arquitetura em camadas
* Integração com banco de dados
* Boas práticas de programação

---

## Autores

Projeto desenvolvido por:

* Bruno Ferreira da Costa - 1240114845
* Bruno Lourenço Queiroz da Silva - 1240120417
* Carlos Augusto da Silva Souza - 1240101684
* Eduardo Rodrigues Gomes - 1240208119
* Gabriel Ribeiro - 1240113883
* Gabriel Vasconcelos - 1210102929
* Guilherme Ribeiro Alves - 1240200753
* Jamilly Dias Deodato - 1240205458
* João Vitor Hermes Fonseca Coelho - 1240112457
* João Victor Pereira dos Reis - 1240111812
* Lucas Rodrigues Correia - 1240105219
* Matheus de Souza - 1240100507
* Mauricio Gonçalves Simões Júnior - 1230103599
* Rafael Matias Alonso Carvalhal - 1240107511
* Victor Gusmão Moreira Vieira - 1260114525  