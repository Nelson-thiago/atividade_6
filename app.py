from flask import Flask, render_template

app = Flask(__name__)

# Renomeando a função que lê o arquivo para evitar conflito de nome
def obter_veiculos():
    def ler_dados():
        with open('veiculos.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        dados = []
        for linha in linhas:
            tipo_veiculo, marca, modelo, ano, diaria, comb, cc = linha.strip().split(',')
            dados.append({
                'tipo': tipo_veiculo,
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'diaria': diaria,
                'combustivel': comb,
                'cilindradas': cc
            })
        return dados

    return ler_dados()


@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/alugar_carros')
def alugar_carros():
    return render_template('carro.html')


@app.route('/alugar_motos')
def alugar_motos():
    return render_template('motocicleta.html')


@app.route('/listar_veiculos')
def listar_veiculos():
    dados = obter_veiculos()  # Chamando a função renomeada
    return render_template('veiculos.html', dados=dados)


if __name__ == "__main__":
    app.run(debug=True)
