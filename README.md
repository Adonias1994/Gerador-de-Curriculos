# 📄 Gerador de Currículos

Projeto focado na coleta, estruturação, persistência e processamento de dados para a geração automatizada de documentos. A aplicação utiliza uma interface web para coletar informações, armazená-las com segurança em um banco de dados e alimentar um script de processamento em Python no back-end.

### 🛠️ Tecnologias Utilizadas
* **Back-End & Lógica:** Python (Processamento de dados e regras de negócio).
* **Banco de Dados:** SQLite via Python (Persistência de dados, modelagem de tabelas e consultas SQL).
* **Front-End (Interface de Coleta):** HTML5, CSS3, JavaScript (Manipulação do DOM e formulários dinâmicos).

### ⚙️ Status do Projeto
Em desenvolvimento contínuo.

- [x] Estrutura semântica e formulários de coleta de dados (HTML5).
- [x] Estilização e responsividade (CSS3).
- [x] Lógica para clonagem de múltiplos campos e validação (JavaScript).
- [x] Modelagem do banco de dados e persistência de dados (SQLite).
- [x] Processamento de dados e exportação (Python).

### 🎯 Foco em Engenharia & Segurança
Este repositório demonstra a capacidade de projetar uma aplicação ponta a ponta:

1. Recebimento de dados dinâmicos a partir do Front-End.
2. Sanitização e armazenamento de informações no Banco de Dados (prevenção contra SQL Injection).
3. Processamento de dados no lado do servidor (Python) para a geração automatizada do documento final.

### -> Para executar em Windows

Abra o terminal (ou prompt de comando) na pasta raiz do seu projeto.

1. Instale o Flask digitando o comando: pip install flask
2. Inicie o seu servidor Python: python app.py
3. O terminal mostrará um endereço, [http://xxx.x.x.x:xxxx/](http://xxx.x.x.x:xxxx/). Clique nele ou copie e cole no navegador.

### -> Para executar em Kali Linux

1. Crie o ambiente virtual. Isso cria uma pasta oculta isolada para as dependências deste projeto de currículo, sem afetar o resto do seu sistema: python3 -m venv venv
2. Ative o ambiente virtual. O seu terminal exibirá um prefixo (venv) na frente do seu nome de usuário: source venv/bin/activate
3. Instale o Flask. Agora, dentro do ambiente protegido, o comando funcionará perfeitamente: pip install flask
4. Inicie o servidor: python3 app.py
