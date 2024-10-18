from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Importação da classe formulario
# from formulario import FormLogin


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    from classes import Veiculo
    from classes import Carro
    from classes import Motocicleta

    print("Iniciando a automação do formulário de produto.")

    # Instânciando objetos
    carro = Carro("Ford", "Fiesta", 2020, 100, "Gasolina")
    moto = Motocicleta("Honda", "CB500", 2021, 80, 250)

    # Local Menu - CONFIGURAR CONFORME MÁQUINA
    bot.browse(r'C:\Users\matutino\Desktop\desafio\atividade_6\templates\menu.html')

    # ---Processo de alugar carro
    bot.find_element('/html/body/ul/li[1]/a/button', By.XPATH).click()
    bot.wait(1000)
    bot.find_element('//*[@id="tipo_veiculo"]', By.XPATH).send_keys(carro.tipo_veiculo)
    bot.wait(1000)
    bot.find_element('//*[@id="marca"]', By.XPATH).send_keys(carro.tipo_veiculo)
    bot.wait(1000)
    bot.find_element('//*[@id="modelo"]', By.XPATH).send_keys(carro.modelo)
    bot.wait(1000)
    bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(carro.ano)
    bot.wait(1000)
    bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(carro.valor_diario)
    bot.wait(1000)
    bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(carro.tipo_combustivel)
    bot.wait(1000)
    bot.find_element('/html/body/form/input[7]', By.XPATH).click()
    bot.wait(1000)

    # Botão de voltar para o menu principal !!!!!
    bot.find_element('', By.XPATH).click()
    bot.wait(1000)

    # Botão de ir para o processo de alugar moto
    bot.find_element('/html/body/ul/li[2]/a/button', By.XPATH).click()
    bot.wait(1000)

    # ---- Processo de alugar moto
    bot.find_element('//*[@id="tipo_veiculo"]', By.XPATH).send_keys(moto.tipo_veiculo)
    bot.wait(1000)
    bot.find_element('//*[@id="marca"]', By.XPATH).send_keys(moto.marca)
    bot.wait(1000)
    bot.find_element('//*[@id="modelo"]', By.XPATH).send_keys(moto.modelo)
    bot.wait(1000)
    bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(moto.ano)
    bot.wait(1000)
    bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(moto.valor_diario)
    bot.wait(1000)
    bot.find_element('//*[@id="cc"]', By.XPATH).send_keys(moto.cilindrada)
    bot.wait(1000)
    bot.find_element('/html/body/form/input[7]', By.XPATH).click()
    bot.wait(1000)

    # Botão de voltar para o menu principal !!!!!
    bot.find_element('', By.XPATH).click()
    bot.wait(1000)

    # Botão de ir para listar veiculos
    bot.find_element('/html/body/ul/li[3]/a/button', By.XPATH).click()
    bot.wait(1000)


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()