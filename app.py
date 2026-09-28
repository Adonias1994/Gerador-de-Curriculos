from flask import Flask, render_template, request, send_file
import sqlite3
import io
from weasyprint import HTML

app = Flask(__name__)

# ==========================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ==========================================
def iniciar_banco():
    # Agora o banco será criado no local exato onde o app.py for executado
    conexao = sqlite3.connect('curriculos.db')
    cursor = conexao.cursor()
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

iniciar_banco()

# ==========================================
# ROTAS DA APLICAÇÃO
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-curriculo', methods=['POST'])
def gerar_curriculo():
    # 1. Coletando os dados do formulário Front-End
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    linkedin = request.form.get('linkedin')
    portfolio = request.form.get('portfolio')
    empresas = request.form.getlist('empresa[]')
    cargos = request.form.getlist('cargo[]')
    
    # 2. Salvando no Banco de Dados
    conexao = sqlite3.connect('curriculos.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO candidatos (nome, email, telefone, linkedin, portfolio)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, email, telefone, linkedin, portfolio))
    conexao.commit()
    conexao.close()

    # 3. GERAÇÃO DINÂMICA (Criando o PDF)
    # Utilizamos o zip() para juntar as duas listas (empresas e cargos) formando pares (Ex: [('Contax', 'Atendente')])
    experiencias = zip(empresas, cargos)
    
    # O Flask preenche o HTML modelo com as variáveis do usuário
    html_renderizado = render_template('curriculo_modelo.html',
                                       nome=nome,
                                       email=email,
                                       telefone=telefone,
                                       linkedin=linkedin,
                                       portfolio=portfolio,
                                       experiencias=experiencias)

    # O WeasyPrint lê o HTML preenchido e converte para PDF na memória do servidor (sem salvar arquivo no disco)
    pdf = HTML(string=html_renderizado).write_pdf()

    # Formata o nome do arquivo (ex: curriculo_Adonias_Pessoa.pdf)
    nome_arquivo = f"curriculo_{nome.replace(' ', '_')}.pdf"

    # 4. DOWNLOAD AUTOMÁTICO (Enviando para o navegador)
    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf',
        as_attachment=True,
        download_name=nome_arquivo
    )

if __name__ == '__main__':
    app.run(debug=True)