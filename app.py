from flask import Flask, render_template, redirect, flash, request, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = os.urandom(24).hex()

context = {}
context["logo"] = "static/img/logo.jpg"

produtos = {}
produtos[1] = {
    "nome": "Estudar",
    "descricao": "Estudar para a prova de matemática. revise os exercicios.",
    "imagem": "/static/img/livro.png"
}
produtos[2] = {
    "nome": "Tomar Café",
    "descricao": "Tomar ovos com bacon e café preto. Não esqueça o açúcar.",
    "imagem": "/static/img/cafe.jpg"
}
produtos[3] = {
    "nome": "Arrumar a cama",
    "descricao": "Arrumar a cama e colocar o travesseiro no lugar. ",
    "imagem": "/static/img/cama.jpg"
}

@app.route('/')
def homepage():    
    
    context["img"] = "/static/img/logo.jpg"
    context["Titulo"] = "GERENCIADOR DE TAREFAS: Qualidade ao Seu Alcance"
    context["Texto"] = '''
    Descubra o Gerenciador de Tarefas, sua solução para organizar e otimizar o dia a dia. 
    Aqui, você encontra ferramentas práticas e eficientes para gerenciar suas atividades com qualidade e precisão.
    Aproveite a experiência de um sistema pensado para facilitar sua rotina e alcançar seus objetivos com mais eficiência.'''

    return render_template("homepage.html", **context)

@app.route('/produto')
def produto():
       
    context["produtos"] = produtos

    return render_template("produto.html", **context)

@app.route('/del_produto')
def del_produto():

    context["produtos"] = produtos
    return render_template("del_produto.html", **context)

@app.route('/excluir_produtos', methods=['POST'])
def excluir_produtos():

    produtos_ids = request.form.getlist('produtos_ids')
    
    if not produtos_ids:
        flash('Nenhum produto selecionado para exclusão.', 'warning')
        return redirect(url_for('del_produto'))
    
    try:
        produtos_ids = [int(id) for id in produtos_ids]
        
        count = 0
        
        for id in produtos_ids:
            if id in produtos:
                produtos.pop(id)
                count += 1
        
        if count > 0:
            flash(f'{count} produto(s) excluído(s) com sucesso!', 'success')
        else:
            flash('Nenhum dos produtos selecionados foi encontrado.', 'info')
            
    except Exception as e:
        flash(f'Erro ao excluir produtos: {str(e)}', 'error')
    
    return redirect(url_for('del_produto'))


@app.route('/add_produto_form')
def add_produto_form():
    return render_template('add_produto.html',**context)


@app.route('/add_produto', methods=['POST'])
def add_produto():
    
    next_id = max(produtos.keys()) + 1 if produtos else 1
    
    
    nome = request.form['nome']
    descricao = request.form['descricao']
    
    
    imagem = request.files['imagem']
    if imagem:
        
        filename = secure_filename(imagem.filename)
        save_path = os.path.join('static/img', filename)
        imagem.save(save_path)
        imagem_path = f'img/{filename}'
    else:
        imagem_path = None
    
    
    produtos[next_id] = {
        "nome": nome,
        "descricao": descricao,
        "imagem": imagem_path
    }
    
    return redirect(url_for('produto'))

@app.route('/up_produto', methods=['POST'])
def up_produto():
    produto_id = request.form.get('id')
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    imagem = request.files.get('imagem')

    # Atualizar o dicionário
    produtos[int(produto_id)] = {
        "nome": nome,
        "descricao": descricao,
        "imagem": f"img/{imagem.filename}" if imagem else produtos[int(produto_id)]['imagem']
    }

    # Salvar imagem se houver
    if imagem:
        imagem.save(os.path.join('static/img', imagem.filename))

    return redirect(url_for('produto'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")