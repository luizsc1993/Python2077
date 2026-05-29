from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello wolrd'
    
@app.route('/curriculo')
def curriculo():
    return"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo</title>
</head>
<body>
    <header>
        <h1>Luiz Costa de Oliveira</h1>
        <div id = "habilidades">
            <p style="color: blue; font-size: 25px;">HABILIDADES</p>
            <p style="">Rei do html</p>
            <p>Flutter</p>
            <p>Python</p>
            <p>Dart</p>
            <p>IOS</p>
            <p>profissional modderpack de minecraft</p>
        </div>
        <div id = "linguas">
            <p style="color: blue; font-size: 25px;">Línguas</p>
               <p>ingles perfeito</p>
               <p>portugues mais ou menos</portal></p>
               <p>alemao fluente</p>
               <p>espanhol de portugal</p>
        </div>
    </header>
</body>
</html>"""

@app.route('/decorator')
def decorator():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Entendendo Decorators</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; max-width: 800px; }
            h1 { color: #2c3e50; }
            h2 { color: #34495e; border-bottom: 2px solid #eee; padding-bottom: 5px; margin-top: 30px; }
            code { background-color: #f4f4f4; padding: 2px 5px; border-radius: 4px; font-family: monospace; color: #d63384; }
            pre { background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; }
        </style>
    </head>
    <body>
        <h1>Decorators em Python </h1>
        
        <h2>1. O que é um decorator?</h2>
        <p>Em Python, um <strong>decorator</strong> (ou decorador) é essencialmente uma função que recebe outra função como argumento, adiciona algum tipo de comportamento ou funcionalidade a ela e, em seguida, retorna uma nova função. A grande vantagem é que ele faz isso <strong>sem modificar o código-fonte da função original</strong>. Na sintaxe do Python, eles são representados pelo símbolo <code>@</code> colocado acima da definição de uma função.</p>
        
        <h2>2. Para que ele serve?</h2>
        <p>Os decorators são uma ferramenta poderosa de "metaprogramação" e servem principalmente para:</p>
        <ul>
            <li><strong>Reutilização de código:</strong> Evitar a repetição de lógicas que precisam ser aplicadas em vários lugares diferentes.</li>
            <li><strong>Separação de responsabilidades:</strong> Manter a função principal focada exclusivamente em sua regra de negócio, deixando o decorator lidar com tarefas secundárias. Exemplo: registrar logs, verificar se um usuário está autenticado, medir o tempo de execução de uma função ou fazer cache de resultados.</li>
        </ul>

        <h2>3. Como ele é utilizado no Flask?</h2>
        <p>No Flask, o exemplo mais famoso e utilizado de decorator é o <code>@app.route()</code>. Ele é o responsável por fazer o <strong>roteamento</strong> da aplicação web.</p>
        <p>Veja este próprio exemplo:</p>
        <pre><code>@app.route('/decorator')
def explicar_decorator():
    return "Olá, mundo!"</code></pre>
        <p>Neste caso, o decorator <code>@app.route('/decorator')</code> está "envolvendo" a nossa função. Por debaixo dos panos, ele está dizendo ao Flask: <em>"Ei, registre esta URL ('/decorator') no seu mapeamento interno. Toda vez que um usuário acessar esse caminho no navegador, chame a função que está logo abaixo de mim e devolva o resultado dela para o usuário."</em></p>
    </body>
    </html>
    """

if __name__ =='__main__':
     app.run(debug=True)