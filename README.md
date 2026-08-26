Sistema de Estoque

Sistema web de controle de estoque desenvolvido em Python utilizando Flask e SQLAlchemy.

O projeto utiliza Python 3, Flask, Flask-SQLAlchemy, SQLite, HTML5, CSS3, JavaScript, JSON, Git e GitHub. O sistema permite cadastrar categorias, cadastrar produtos, registrar entradas e saídas de estoque, visualizar o histórico de movimentações, receber alertas de estoque baixo e filtrar produtos por nome e categoria. Também disponibiliza endpoints de API que retornam dados em formato JSON.

A estrutura do projeto é composta pela pasta app, que contém os arquivos __init__.py, models.py e routes.py, além das pastas templates e static. A pasta instance armazena o banco de dados estoque.db. Também fazem parte do projeto os arquivos requirements.txt, .gitignore, run.py e README.md. A pasta venv é utilizada para o ambiente virtual.

Para executar o projeto, primeiro clone o repositório com o comando git clone https://github.com/vinnyzz07/sistema-de-estoque.git e acesse a pasta com o comando cd sistema-de-estoque. Em seguida, crie o ambiente virtual com o comando python -m venv venv e ative-o. No Windows, utilize o comando venv\Scripts\activate, enquanto no Linux ou macOS utilize o comando source venv/bin/activate. Depois, instale as dependências com o comando pip install -r requirements.txt e execute a aplicação com o comando python run.py.

Após iniciar a aplicação, o sistema estará disponível em http://127.0.0.1:5000. Através da interface web é possível gerenciar categorias, produtos e movimentações de estoque, além de visualizar uma visão geral do estoque. As rotas de API estão disponíveis em /api/produtos e /api/produtos/estoque-baixo.

O projeto utiliza SQLite como banco de dados, e o arquivo estoque.db é criado automaticamente na pasta instance durante a execução da aplicação.

Todas as mensagens de sucesso e erro do sistema estão em português, assim como os nomes de variáveis, funções, classes e rotas, facilitando a leitura e compreensão do código.

Este projeto foi desenvolvido com o objetivo de colocar em prática e aprimorar conhecimentos em desenvolvimento web com Python, Flask, SQLAlchemy, operações CRUD, JavaScript e APIs REST.

Desenvolvido por Vinicius Atanásio.