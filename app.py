from flask import Flask, render_template, request
import sqlite3

# Inicializa a aplicação Flask
app = Flask(__name__)

# ==========================================
# CONFIGURAÇÃO DO BANCO DE DADOS (SQLite)
# ==========================================
def iniciar_banco():
    """
    Função para criar o banco de dados e a tabela caso não existam.
    """
    # Conecta ao arquivo do banco (se não existir, o Python cria automaticamente)
    conexao = sqlite3.connect('curriculos.db')
    cursor = conexao.cursor()

    # Criação da tabela de Dados Pessoais usando instrução SQL.
    # Em uma modelagem completa de banco relacional, criaríamos tabelas separadas 
    # para 'Experiencias' e 'Formacoes' (Relacionamento 1 para N). 
    # Para começarmos, vamos salvar os dados principais.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            linkedin TEXT,
            portfolio TEXT
        )
    ''')
    
    conexao.commit()
    conexao.close()

# Executa a função para garantir que o banco está pronto ao iniciar o app
iniciar_banco()

# ==========================================
# ROTAS DA APLICAÇÃO (A ponte Front/Back)
# ==========================================

# 1. Rota principal: Quando o usuário acessa o site (GET)
@app.route('/')
def index():
    # O Flask procura automaticamente na pasta /templates
    return render_template('index.html')

# 2. Rota de processamento: Quando o formulário é enviado (POST)
@app.route('/gerar-curriculo', methods=['POST'])
def gerar_curriculo():
    # Coletando os dados simples que vieram do atributo 'name' do HTML
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    linkedin = request.form.get('linkedin')
    portfolio = request.form.get('portfolio')
    
    # Coletando os campos dinâmicos (listas criadas pelo seu botão clonar no JS)
    # request.form.getlist() pega todos os inputs que têm o mesmo name (ex: name="empresa[]")
    empresas = request.form.getlist('empresa[]')
    cargos = request.form.getlist('cargo[]')
    
    # ==========================================
    # PERSISTÊNCIA E SEGURANÇA NO BANCO DE DADOS
    # ==========================================
    conexao = sqlite3.connect('curriculos.db')
    cursor = conexao.cursor()

    # Inserção de dados utilizando "Parameterized Queries" (os sinais de interrogação ?).
    # Esta é uma prática fundamental de defesa (Blue Team/Sec) para evitar ataques de SQL Injection.
    # Nunca concatene strings diretamente na instrução SQL.
    cursor.execute('''
        INSERT INTO candidatos (nome, email, telefone, linkedin, portfolio)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, email, telefone, linkedin, portfolio))
    
    conexao.commit()
    conexao.close()

    # Log no terminal apenas para visualização de que o back-end recebeu as listas de experiência
    print(f"\n--- Novo Currículo Recebido ---")
    print(f"Nome: {nome} | E-mail: {email}")
    print(f"Empresas cadastradas: {empresas}")
    print(f"Cargos cadastrados: {cargos}")
    print("-------------------------------\n")

    # Retorno temporário para o usuário (aqui no futuro entrará a lógica de gerar o PDF/Word)
    return f"<h1>Sucesso!</h1><p>Os dados de {nome} foram salvos com segurança no banco de dados SQLite!</p>"

# ==========================================
# INICIALIZAÇÃO DO SERVIDOR
# ==========================================
if __name__ == '__main__':
    # O modo debug=True recarrega o servidor sozinho se você alterar o código
    app.run(debug=True)