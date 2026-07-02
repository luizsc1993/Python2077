from flask import Blueprint, redirect, render_template, request, url_for
from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

# Apelido "figurinhas" -> use url_for('figurinhas.index') nos templates
figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    # Busca a lista de ofertas no banco usando o método do modelo
    ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()

    if request.method == "POST":
        # Captura as strings enviadas pelo formulário HTML através do atributo 'name'
        colecionador_id = request.form.get("colecionador_id")
        observacao = request.form.get("observacao")
        figurinha_oferece_id = request.form.get("figurinha_oferece_id")
        figurinha_deseja_id = request.form.get("figurinha_deseja_id")

        # 1. Instancia e adiciona a nova Oferta de Troca principal
        nova_oferta = OfertaTroca(colecionador_id=colecionador_id, observacao=observacao)
        db.session.add(nova_oferta)

        # 2. Instancia e adiciona os itens vinculados à oferta (o que ele oferece e o que deseja)
        item_oferece = ItemOferta(oferta=nova_oferta, figurinha_id=figurinha_oferece_id, tipo="oferece", quantidade=1)
        item_deseja = ItemOferta(oferta=nova_oferta, figurinha_id=figurinha_deseja_id, tipo="deseja", quantidade=1)
        
        db.session.add(item_oferece)
        db.session.add(item_deseja)

        # 3. Commita a transação para salvar de fato todas as linhas nas tabelas correspondentes
        db.session.commit()

        # Redireciona o usuário para a página de listagem
        return redirect(url_for('figurinhas.index'))

    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )