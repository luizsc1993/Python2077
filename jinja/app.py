import os
import webbrowser
from jinja2 import Environment, FileSystemLoader

ambiente = Environment(loader=FileSystemLoader('.'))
template = ambiente.get_template('index.html')

dados_da_atividade = {
    "nome": "Ana",
    "idade": 25,
    "usuario": {"nome": "Ana", "email": "ana@email.com"},
    "alunos": ["Maria", "João", "Pedro", "Lucas"],
    "nota": 8.5
}

html_pronto = template.render(dados_da_atividade)

nome_arquivo = 'resultado_final.html'
with open(nome_arquivo, 'w', encoding='utf-8') as ficheiro:
    ficheiro.write(html_pronto)

print("Arquivo gerado! Abrindo no navegador...")

caminho_absoluto = os.path.abspath(nome_arquivo)
webbrowser.open(f"file:///{caminho_absoluto}")