from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Categoria, Produto, Movimentacao

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    total_produtos = Produto.query.count()
    total_categorias = Categoria.query.count()
    total_movimentacoes = Movimentacao.query.count()

    produtos_estoque_baixo = Produto.query.filter(
        Produto.quantidade <= Produto.quantidade_minima
    ).order_by(Produto.nome).all()

    ultimas_movimentacoes = Movimentacao.query.order_by(
        Movimentacao.data.desc()
    ).limit(5).all()

    return render_template(
        'index.html',
        total_produtos=total_produtos,
        total_categorias=total_categorias,
        total_movimentacoes=total_movimentacoes,
        produtos_estoque_baixo=produtos_estoque_baixo,
        ultimas_movimentacoes=ultimas_movimentacoes
    )

@bp.route('/categorias')
def listar_categorias():
    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template('categorias/listar.html', categorias=categorias)

@bp.route('/categorias/nova', methods=['GET', 'POST'])
def nova_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        descricao = request.form.get('descricao', '').strip()

        if not nome:
            flash('O nome da categoria é obrigatório.', 'erro')
            return redirect(url_for('main.nova_categoria'))

        if Categoria.query.filter_by(nome=nome).first():
            flash('Já existe uma categoria com esse nome.', 'erro')
            return redirect(url_for('main.nova_categoria'))

        nova = Categoria(nome=nome, descricao=descricao)
        db.session.add(nova)
        db.session.commit()

        flash('Categoria cadastrada com sucesso!', 'sucesso')
        return redirect(url_for('main.listar_categorias'))

    return render_template('categorias/formulario.html', categoria=None)

@bp.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        descricao = request.form.get('descricao', '').strip()

        if not nome:
            flash('O nome da categoria é obrigatório.', 'erro')
            return redirect(url_for('main.editar_categoria', id=id))

        existente = Categoria.query.filter_by(nome=nome).first()
        if existente and existente.id != id:
            flash('Já existe uma categoria com esse nome.', 'erro')
            return redirect(url_for('main.editar_categoria', id=id))

        categoria.nome = nome
        categoria.descricao = descricao
        db.session.commit()

        flash('Categoria atualizada com sucesso!', 'sucesso')
        return redirect(url_for('main.listar_categorias'))

    return render_template('categorias/formulario.html', categoria=categoria)

@bp.route('/categorias/excluir/<int:id>', methods=['POST'])
def excluir_categoria(id):
    categoria = Categoria.query.get_or_404(id)

    if categoria.produtos:
        flash('Não é possível excluir esta categoria porque existem produtos vinculados a ela.', 'erro')
        return redirect(url_for('main.listar_categorias'))

    db.session.delete(categoria)
    db.session.commit()

    flash('Categoria excluída com sucesso!', 'sucesso')
    return redirect(url_for('main.listar_categorias'))

@bp.route('/produtos')
def listar_produtos():
    produtos = Produto.query.order_by(Produto.nome).all()
    return render_template('produtos/listar.html', produtos=produtos)

@bp.route('/produtos/novo', methods=['GET', 'POST'])
def novo_produto():
    categorias = Categoria.query.order_by(Categoria.nome).all()

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        descricao = request.form.get('descricao', '').strip()
        quantidade = request.form.get('quantidade', 0)
        quantidade_minima = request.form.get('quantidade_minima', 5)
        preco = request.form.get('preco', 0)
        categoria_id = request.form.get('categoria_id')

        if not nome:
            flash('O nome do produto é obrigatório.', 'erro')
            return redirect(url_for('main.novo_produto'))

        if not categoria_id:
            flash('Selecione uma categoria.', 'erro')
            return redirect(url_for('main.novo_produto'))

        try:
            quantidade = int(quantidade)
            quantidade_minima = int(quantidade_minima)
            preco = float(preco.replace(',', '.'))
        except ValueError:
            flash('Quantidade, quantidade mínima e preço devem ser números válidos.', 'erro')
            return redirect(url_for('main.novo_produto'))

        novo = Produto(
            nome=nome,
            descricao=descricao,
            quantidade=quantidade,
            quantidade_minima=quantidade_minima,
            preco=preco,
            categoria_id=int(categoria_id)
        )
        db.session.add(novo)
        db.session.commit()

        flash('Produto cadastrado com sucesso!', 'sucesso')
        return redirect(url_for('main.listar_produtos'))

    return render_template('produtos/formulario.html', produto=None, categorias=categorias)

@bp.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)
    categorias = Categoria.query.order_by(Categoria.nome).all()

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        descricao = request.form.get('descricao', '').strip()
        quantidade = request.form.get('quantidade', 0)
        quantidade_minima = request.form.get('quantidade_minima', 5)
        preco = request.form.get('preco', 0)
        categoria_id = request.form.get('categoria_id')

        if not nome:
            flash('O nome do produto é obrigatório.', 'erro')
            return redirect(url_for('main.editar_produto', id=id))

        if not categoria_id:
            flash('Selecione uma categoria.', 'erro')
            return redirect(url_for('main.editar_produto', id=id))

        try:
            quantidade = int(quantidade)
            quantidade_minima = int(quantidade_minima)
            preco = float(preco.replace(',', '.'))
        except ValueError:
            flash('Quantidade, quantidade mínima e preço devem ser números válidos.', 'erro')
            return redirect(url_for('main.editar_produto', id=id))

        produto.nome = nome
        produto.descricao = descricao
        produto.quantidade = quantidade
        produto.quantidade_minima = quantidade_minima
        produto.preco = preco
        produto.categoria_id = int(categoria_id)
        db.session.commit()

        flash('Produto atualizado com sucesso!', 'sucesso')
        return redirect(url_for('main.listar_produtos'))

    return render_template('produtos/formulario.html', produto=produto, categorias=categorias)

@bp.route('/produtos/excluir/<int:id>', methods=['POST'])
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)

    for mov in produto.movimentacoes:
        db.session.delete(mov)

    db.session.delete(produto)
    db.session.commit()

    flash('Produto excluído com sucesso!', 'sucesso')
    return redirect(url_for('main.listar_produtos'))

@bp.route('/movimentacoes')
def listar_movimentacoes():
    movimentacoes = Movimentacao.query.order_by(Movimentacao.data.desc()).all()
    return render_template('movimentacoes/listar.html', movimentacoes=movimentacoes)

@bp.route('/movimentacoes/nova', methods=['GET', 'POST'])
def nova_movimentacao():
    produtos = Produto.query.order_by(Produto.nome).all()

    if request.method == 'POST':
        produto_id = request.form.get('produto_id')
        tipo = request.form.get('tipo')
        quantidade = request.form.get('quantidade')
        observacao = request.form.get('observacao', '').strip()

        if not produto_id or not tipo or not quantidade:
            flash('Preencha todos os campos obrigatórios.', 'erro')
            return redirect(url_for('main.nova_movimentacao'))

        if tipo not in ['entrada', 'saida']:
            flash('Tipo de movimentação inválido.', 'erro')
            return redirect(url_for('main.nova_movimentacao'))

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            flash('A quantidade deve ser um número inteiro positivo.', 'erro')
            return redirect(url_for('main.nova_movimentacao'))

        produto = Produto.query.get_or_404(int(produto_id))

        if tipo == 'saida' and produto.quantidade < quantidade:
            flash(f'Estoque insuficiente. Disponível: {produto.quantidade}', 'erro')
            return redirect(url_for('main.nova_movimentacao'))

        movimentacao = Movimentacao(
            tipo=tipo,
            quantidade=quantidade,
            observacao=observacao,
            produto_id=produto.id
        )
        db.session.add(movimentacao)

        if tipo == 'entrada':
            produto.quantidade += quantidade
        else:
            produto.quantidade -= quantidade

        db.session.commit()

        flash(f'{tipo.capitalize()} de {quantidade} unidade(s) registrada com sucesso!', 'sucesso')
        return redirect(url_for('main.listar_movimentacoes'))

    return render_template('movimentacoes/formulario.html', produtos=produtos)