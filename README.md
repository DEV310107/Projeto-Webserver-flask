# Projeto: Sistema Web de Lista de Tarefas (TODO)

- INSTRUÇÕES
    
    *Objetivo*
    
    Desenvolver um sistema web de lista de tarefas (TODO) utilizando Flask. O sistema deverá armazenar os dados em um arquivo CSV e fornecer uma interface simples para gerenciamento das tarefas.
    
    ### *Requisitos Funcionais*
    
    O sistema deverá permitir :
    
    ✅ *Adicionar tarefas* – O usuário poderá criar novas tarefas com um título e descrição.
    
    ✅ *Remover tarefas* – O usuário poderá excluir tarefas individualmente.
    
    ✅ *Editar tarefas* – O usuário poderá modificar o título e a descrição de uma tarefa existente.
    
    ✅ *Listar tarefas* – Exibir todas as tarefas cadastradas.
    
    ### *Requisitos Técnicos*
    
    - O backend deve ser desenvolvido em *Flask*.
    - O banco de dados será um *arquivo CSV*, armazenando ID, título e descrição da tarefa.
    - A interface pode ser desenvolvida com *HTML + TAILWIND*
    
    ---
    
    ### *Extras para Pontos Adicionais (+)*
    
    ➕ *Incluir imagens*: O sistema deve permitir que o usuário faça o upload de uma imagem associada a cada tarefa. As imagens podem ser armazenadas em uma pasta separada no servidor, e o caminho salvo no CSV.
    
    ➕ *Migração para MySQL*: Criar uma versão alternativa do projeto utilizando um banco de dados MySQL ao invés do arquivo CSV, garantindo persistência mais robusta e escalável.
    
    ---
    
    *Entrega:* O projeto deverá ser entregue como um repositório Git contendo o código-fonte e um README com instruções de instalação e uso.
    

## DOCUMENTAÇÃO

### Introdução:

O objetivo deste projeto é criar um sistema de lista de tarefas (TODO) simples e funcional utilizando o framework *Flask. O sistema permitirá ao usuário gerenciar suas tarefas através de uma interface web, incluindo funcionalidades de adicionar, editar, remover e listar tarefas. As tarefas serão armazenadas em um arquivo **CSV, e a interface será desenvolvida com **HTML* e *Tailwind CSS*.

### Pratica:

Com as instruções e objetivos traçados iniciamos a divisão de tarefa no grupo, para um aproveitamento melhor de nosso tempo e ter um desempenho mais focado em cada termo técnico.

### *Requisitos Técnicos*

- O backend deve ser desenvolvido em *Flask*.
- O banco de dados será um *arquivo CSV*, armazenando ID, título e descrição da tarefa.
- A interface pode ser desenvolvida com *HTML + TAILWIND*

**Incluir imagens*

Backend em Flask

Para começar a programar em Flask temos que preparar o ambiente virtual “venv”, para isso vamos entender oque é primeiramente!

*O que é um ambiente virtual (venv)?*

Um ambiente virtual (venv) é um ambiente isolado que permite instalar pacotes Python sem afetar a instalação global do sistema. Isso é útil para manter dependências organizadas e evitar conflitos entre projetos.

*Criando um ambiente virtual*

Para criar um ambiente virtual em Python, use o seguinte comando:


python -m venv venv


Isso criará uma pasta chamada venv com todos os arquivos necessários.

*▶️ Ativando o ambiente virtual*

*🖥 Windows (PowerShell):*


.\venv\Scripts\Activate.ps1


Se ocorrer um erro, talvez seja necessário modificar a permissão de execução de scripts:


Set-ExecutionPolicy RemoteSigned


*📦 Instalando pacotes dentro do venv*

Após ativar o ambiente virtual, você pode instalar pacotes normalmente com pip:


pip install flask


*🚀 Executando um script Python*

Se quiser rodar um arquivo Python dentro do ambiente virtual:


python nome_do_arquivo.py


Se rodar esse comando sem ativar o venv, o script será executado com a versão global do Python, podendo gerar erros caso os pacotes necessários não estejam instalados.

*📌 Conclusão*

Ambientes virtuais são essenciais para organizar dependências em projetos Python. Criar, ativar e instalar pacotes no venv é simples e evita problemas de compatibilidade entre projetos diferentes.

### CÓDIGO:

Depois de entender como configurar o ambiente virtual do “venv”, vamos para a codificação
