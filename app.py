from flask import Flask, render_template

app = Flask(__name__)

from classes import Carro, Motocicleta

import os

def obter_veiculos():
    def ler_dados():
        caminho_arquivo = os.path.join(os.path.dirname(__file__), 'veiculos.txt')

        # Verifica se o arquivo existe
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

        # Abre o arquivo e lê as linhas
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        dados = []
        for linha in linhas:
            tipo_veiculo, marca, modelo, ano, diaria, comb, cc = linha.strip().split(',')
            if tipo_veiculo.lower() == 'carro':
                dados.append(Carro(marca, modelo, int(ano), float(diaria), comb))
            elif tipo_veiculo.lower() == 'moto':
                dados.append(Motocicleta(marca, modelo, int(ano), float(diaria), int(cc)))
        
        return dados
    return ler_dados()




@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/adicionar_veiculo')
def alugar_carros():
    return render_template('adicionar_veiculo.html')

@app.route('/alugar_motos')
def alugar_motos():
    return render_template('motocicleta.html')


@app.route('/listar_veiculos')
def listar_veiculos():
    dados = obter_veiculos()  
    print (dados)
    return render_template('veiculos.html', dados=dados)


if __name__ == "__main__":
    app.run(debug=True)
