from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.carro import Carro
from classes.motocicleta import Motocicleta
from app import obter_veiculos

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def iniciar_bot():
    """Inicializa o WebBot e retorna a instância."""
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    return bot

def acessar_pagina(bot, url):
    """Acessa a página inicial da aplicação."""
    print("Iniciando a automação do formulário de produto.")
    bot.browse(url)
    bot.wait(1000)

def preencher_formulario(bot, veiculo):
    """Preenche o formulário com os dados do veículo."""
    bot.find_element('//*[@id="tipo_veiculo"]', By.XPATH).send_keys(veiculo.tipo_veiculo)
    bot.wait(1000)
    bot.find_element('//*[@id="marca"]', By.XPATH).send_keys(veiculo.marca)
    bot.wait(1000)
    bot.find_element('//*[@id="modelo"]', By.XPATH).send_keys(veiculo.modelo)
    bot.wait(1000)
    bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(veiculo.ano)
    bot.wait(1000)
    bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(str(veiculo.valor_diario))

    if isinstance(veiculo, Carro):
        bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(veiculo.tipo_combustivel)
    elif isinstance(veiculo, Motocicleta):
        bot.find_element('//*[@id="cc"]', By.XPATH).send_keys(veiculo.cilindrada)
    bot.wait(1000)

def alugar_veiculo(bot, veiculos):
    """Processa a ação de alugar veículos da lista."""
    for veiculo in veiculos:
        preencher_formulario(bot, veiculo)
        bot.find_element('/html/body/form/input[5]', By.XPATH).click()
        bot.wait(1000)

def retornar_menu(bot):
    """Retorna ao menu principal."""
    bot.find_element('/html/body/li/a/button', By.XPATH).click()
    bot.wait(1000)

def listar_veiculos(bot):
    """Navega até a lista de veículos."""
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
