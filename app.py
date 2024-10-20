from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from classes import Carro, Motocicleta, Veiculo

'''def obter_veiculos():
    def ler_dados():
        with open('veiculos.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        dados = []
        for linha in linhas:
            tipo_veiculo, marca, modelo, ano, diaria, comb, cc = linha.strip().split(',')
            if tipo_veiculo.lower() == 'carro':
                dados.append(Carro(marca, modelo, int(ano), diaria, comb))
            elif tipo_veiculo.lower() == 'moto':
                dados.append(Motocicleta(marca, modelo, int(ano), float(diaria), int(cc)))
        return dados

    return ler_dados()'''



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


"""@app.route('/listar_veiculos')
def listar_veiculos():
    dados = obter_veiculos()  
    print (dados)
    return render_template('veiculos.html', dados=dados)"""


if __name__ == "__main__":
    app.run(debug=True)
