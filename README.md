# API Flask

Este é um projeto de exemplo utilizando o microframework **Flask** para construção de uma API RESTful em Python. O objetivo é demonstrar como criar endpoints básicos, manipular dados via JSON e estruturar uma API simples, ideal para aprendizado e testes iniciais.

## Descrição

A API implementa uma estrutura básica de CRUD (Create, Read, Update, Delete) para itens armazenados em memória (simulação de banco de dados com uma lista).

## 🛠Tecnologias utilizadas

- Python 3.x
- Flask
- JSON (para comunicação entre cliente e servidor)

## Como executar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/gtins/api-flask.git
   cd api-flask
2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. Instale as dependências
```
pip install flask
```
4. Execute a aplicação
```
python app.py
```
5. Acesse no navegador ou via ferramentas como Postman ou curl:

http://127.0.0.1:5000/
