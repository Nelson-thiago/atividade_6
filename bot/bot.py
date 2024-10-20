from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def obter_veiculos():
    def ler_dados():
        with open('veiculos.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        dados = []
        for linha in linhas:
            tipo_veiculo, marca, modelo, ano, diaria, comb, cc = linha.strip().split(',')
            veiculo = {
                'tipo_veiculo': tipo_veiculo,
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'diaria': diaria,
                'combustivel': comb if tipo_veiculo.lower() == 'carro' else None,
                'cilindrada': cc if tipo_veiculo.lower() == 'moto' else None
            }
            dados.append(veiculo)
        return dados

    return ler_dados()

def iniciar_bot():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    return bot

def acessar_pagina(bot, url):
    print("Iniciando a automação do formulário de produto.")
    bot.browse(url)
    bot.wait(1000)

def preencher_formulario(bot, veiculo):
    bot.find_element('//*[@id="tipo_veiculo"]', By.XPATH).send_keys(veiculo['tipo_veiculo'])
    bot.wait(1000)
    bot.find_element('//*[@id="marca"]', By.XPATH).send_keys(veiculo['marca'])
    bot.wait(1000)
    bot.find_element('//*[@id="modelo"]', By.XPATH).send_keys(veiculo['modelo'])
    bot.wait(1000)
    bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(veiculo['ano'])
    bot.wait(1000)
    bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(veiculo['diaria'])

    if veiculo['tipo_veiculo'].lower() == 'carro':
        bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(veiculo['combustivel'])
    elif veiculo['tipo_veiculo'].lower() == 'moto':
        bot.find_element('//*[@id="cc"]', By.XPATH).send_keys(veiculo['cilindrada'])
    bot.wait(1000)

def alugar_veiculo(bot, veiculos):
    for veiculo in veiculos:
        preencher_formulario(bot, veiculo)
        bot.find_element('/html/body/div[1]/form/input[5]', By.XPATH).click()
        bot.wait(5000)

        bot.find_element('/html/body/div[1]/a/button', By.XPATH).click()
        bot.wait(1000)

        bot.find_element('/html/body/ul/li[1]/a/button', By.XPATH).click()
        bot.wait(1000)

def retornar_menu(bot):
    bot.find_element('/html/body/li/a/button', By.XPATH).click()
    bot.wait(1000)

def listar_veiculos(bot):
    bot.find_element('/html/body/ul/li[2]/a/button', By.XPATH).click()
    bot.wait(10000)

def main():
    # Inicialização do Maestro
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Inicializa o bot
    bot = iniciar_bot()

    # Acessa a página
    acessar_pagina(bot, r'http://127.0.0.1:5000')

    # Obtém a lista de veículos
    veiculos = obter_veiculos()

    # Processo de alugar veículos
    bot.find_element('/html/body/ul/li[1]/a/button', By.XPATH).click()
    alugar_veiculo(bot, veiculos)

    # Retorna ao menu
    retornar_menu(bot)

    # Lista os veículos
    listar_veiculos(bot)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
