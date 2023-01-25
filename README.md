# CNAB-Parser

CNAB-Parser é uma aplicação web desenvolvida em Python, utilizando o framework Django, que permite fazer upload e processar arquivos CNAB. Ele normaliza e armazena os dados em um banco de dados relacional e exibe operações importadas por loja com totalizador do saldo. 

## Características
- Fácil de configurar e executar
- Utiliza Docker para garantir compatibilidade com ambientes Unix
- Ferramenta útil para organizações financeiras e outras empresas que lidam com muitos dados CNAB, permitindo automatizar processos de negócios.

## Requisitos
- Docker
- Docker Compose

## Instalação
1. Clone este repositório: `git clone https://github.com/VictrCruz312/CNAB-Parser.git`
2. Entre no diretório do projeto: `cd CNAB-Parser`
3. Crie um arquivo `.env` com as configurações de sua aplicação (veja o arquivo `.env.example` como referência)
4. Execute o comando `docker-compose up -d` para iniciar os containers
5. Acesse a aplicação em `http://localhost:8000`

## Como usar
1. Faça upload de um arquivo CNAB
2. Visualize a lista de operações importadas por loja e seus respectivos totais de saldo
3. Utilize o filtro de seleção de loja para visualizar apenas as operações de uma determinada loja

## Créditos
CNAB-Parser foi desenvolvido por [VictrCruz312](https://github.com/VictrCruz312) com o objetivo de facilitar o processamento de arquivos CNAB.
