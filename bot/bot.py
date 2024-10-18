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
    

    # print("Iniciando a automação do formulário de produto.")
    # formulario = FormLogin(
    #     nome='Lucas Andrade', idade=31, sexo='Masculino', email='Lrandrade20@gmail.com', telefone='929981458913', 
    #     assunto='Teste', mensagem='Busquem conhecimento', senha='senha123'
    # )

    # # Automação Form Base
    # bot.browse(r'C:\Users\lrand\OneDrive\Área de Trabalho\Nova pasta\poo-python-ifam\Atividades\Atividade 04\bot-formulario\html\form_base.html')
    # bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(formulario.nome)
    # bot.wait(1000)
    # bot.find_element('//*[@id="idade"]', By.XPATH).send_keys(formulario.idade)
    # bot.wait(1000)
    # bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario.email)
    # bot.wait(1000)
    # bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(formulario.telefone)
    # bot.wait(1000)
    # bot.enter()
    # bot.wait(3000)

    # # Automação Form Login
    # bot.browse(r'C:\Users\lrand\OneDrive\Área de Trabalho\Nova pasta\poo-python-ifam\Atividades\Atividade 04\bot-formulario\html\form_login.html')
    # bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario.email)
    # bot.wait(1000)
    # bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(formulario.senha)
    # bot.wait(1000)
    # bot.enter()
    # bot.wait(3000)

    # # Automação Form Contato
    # bot.browse(r'C:\Users\lrand\OneDrive\Área de Trabalho\Nova pasta\poo-python-ifam\Atividades\Atividade 04\bot-formulario\html\form_contato.html')
    # bot.find_element('//*[@id="assunto"]', By.XPATH).send_keys(formulario.assunto)
    # bot.wait(1000)
    # bot.find_element('//*[@id="mensagem"]', By.XPATH).send_keys(formulario.mensagem)
    # bot.wait(1000)
    # bot.enter()
    # bot.wait(3000)
    # print(formulario.informacao())


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()