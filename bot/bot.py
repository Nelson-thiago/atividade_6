from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

import sys
sys.path.append(r'C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_6\classes\veiculo')
sys.path.append(r'C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_6\classes\motocicleta')
sys.path.append(r'C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_6\classes\Crro')
from classes.carro import Carro
from classes.motocicleta import Motocicleta
from app import obter_veiculos

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    print("Iniciando a automação do formulário de produto.")

    # Obtendo a lista de veículos do arquivo
    veiculos = obter_veiculos()

    # Local Menu - CONFIGURAR CONFORME MÁQUINA
    bot.browse(r'http://127.0.0.1:5000/')

    # ---Processo de alugar veículos
    for veiculo in veiculos:
        bot.find_element('/html/body/ul/li[1]/a/button', By.XPATH).click()
        bot.wait(1000)
        bot.find_element('//*[@id="tipo_veiculo"]', By.XPATH).send_keys(veiculo.tipo_veiculo)
        bot.wait(1000)
        bot.find_element('//*[@id="marca"]', By.XPATH).send_keys(veiculo.marca)
        bot.wait(1000)
        bot.find_element('//*[@id="modelo"]', By.XPATH).send_keys(veiculo.modelo)
        bot.wait(1000)
        bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(veiculo.ano)
        bot.wait(1000)
        bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(veiculo.valor_diario)

        # Verifique o tipo de veículo para preencher os campos apropriados
        if isinstance(veiculo, Carro):
            bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(veiculo.tipo_combustivel)
        elif isinstance(veiculo, Motocicleta):
            bot.find_element('//*[@id="cc"]', By.XPATH).send_keys(veiculo.cilindrada)

        bot.wait(1000)
        bot.find_element('/html/body/form/input[7]', By.XPATH).click()
        bot.wait(1000)

        # Botão de voltar para o menu principal
        bot.find_element('', By.XPATH).click()
        bot.wait(1000)

    # Botão de ir para listar veículos
    bot.find_element('/html/body/ul/li[3]/a/button', By.XPATH).click()
    bot.wait(1000)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
