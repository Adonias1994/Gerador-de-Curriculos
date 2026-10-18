# 📄 Gerador de Currículos

Inicialmente tentei desenvolver o projeto acelerando os códigos com Inteligência Artificial, o que foi bom até certo ponto. Porém o retorno do arquivo em PDF não foi satisfatório, pois apresentava um erro que não vinha com todas as informações no currículo.

Tentei corrigir, mas o código se tornou confuso e de difícil manutenção. Por esse motivo, decidi recomeçar o projeto do zero com o código sendo feito 100% por mim.

A ideia é ter uma página onde é preenchida as informações e obter o currículo em PDF.

### 🛠️ Tecnologias Utilizadas
* **Back-End & Lógica:** Python (Processamento de dados e regras de negócio).
* **Banco de Dados:** SQLite via Python (Persistência de dados, modelagem de tabelas e consultas SQL).
* **Front-End (Interface de Coleta):** HTML5, CSS3, JavaScript (Manipulação do DOM e formulários dinâmicos).

### ⚙️ Status do Projeto
Em desenvolvimento contínuo.

- [...] Estrutura semântica e formulários de coleta de dados (HTML5).
- [] Estilização e responsividade (CSS3).
- [] Lógica para clonagem de múltiplos campos e validação (JavaScript).
- [] Modelagem do banco de dados e persistência de dados (SQLite).
- [] Processamento de dados e exportação (Python).

### -> Para executar em Windows (quando pronto)

Abra o terminal (ou prompt de comando) na pasta raiz do seu projeto.

1. Instale o Flask digitando o comando: pip install flask
2. Inicie o seu servidor Python: python app.py
3. O terminal mostrará um endereço, [http://xxx.x.x.x:xxxx/](http://xxx.x.x.x:xxxx/). Clique nele ou copie e cole no navegador.

### -> Para executar em Kali Linux

1. Crie o ambiente virtual. Isso cria uma pasta oculta isolada para as dependências deste projeto de currículo, sem afetar o resto do seu sistema: python3 -m venv venv
2. Ative o ambiente virtual. O seu terminal exibirá um prefixo (venv) na frente do seu nome de usuário: source venv/bin/activate
3. Instale o Flask. Agora, dentro do ambiente protegido, o comando funcionará perfeitamente: pip install flask
4. Inicie o servidor: python3 app.py
