from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

<<<<<<< HEAD
from classes import Carro, Motocicleta, Veiculo
=======
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

>>>>>>> 8e9c3146724f5203d80f055b027331821e177d31

veiculos = []  # Define a lista de veículos globalmente


@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/adicionar_veiculo', methods=['GET', 'POST'])
def adicionar_veiculo():
    if request.method == 'POST':
        tipo_veiculo = request.form['tipo_veiculo']
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        diaria = float(request.form['diaria'])

        if tipo_veiculo == 'carro':
            combustivel = request.form['combustivel']
            veiculo = Carro(marca, modelo, ano, diaria, combustivel)
            print(f"Carro adicionado: {veiculo.marca} {veiculo.modelo}, {veiculo.ano}, {veiculo.valor_diario}, {veiculo.tipo_combustivel}")
        
        elif tipo_veiculo == 'moto':
            cilindrada = int(request.form['cc'])
            veiculo = Motocicleta(marca, modelo, ano, diaria, cilindrada)
            print(f"Motocicleta adicionada: {veiculo.marca} {veiculo.modelo}, {veiculo.ano}, {veiculo.valor_diario}, {veiculo.cilindrada}cc")


        # Adiciona o novo veículo à lista
        veiculos.append(veiculo)

        return redirect(url_for('listar_veiculos'))
    
    return render_template('adicionar_veiculo.html')

@app.route('/listar_veiculos')
def listar_veiculos():
    return render_template('veiculos.html', dados=Veiculo.lista_veiculos)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/adicionar_veiculo')
def alugar_carros():
    return render_template('adicionar_veiculo.html')

@app.route('/alugar_motos')
def alugar_motos():
    return render_template('motocicleta.html')

if __name__ == "__main__":
    app.run(debug=True)
