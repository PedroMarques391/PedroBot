import pyautogui as pt
import pyperclip as pc
from Bases import falas_bot
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import pyttsx3
from pytube import YouTube
from colorama import Fore
from Bases.topicos_bot import Conversas, bot_psicologo
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer  

robot = pyttsx3.init()

print(Fore.GREEN + 'Olá estranho, qual é o seu nome? ')
robot.say(falas_bot.fala3)
robot.runAndWait()
nome = input("--> ")


print('====================================================================================================')
time.sleep(1)
print(f"Olá {nome}, eu sou o PedroBot, sou capaz de executar tarefas básicas no seu computador e na internet.")
fala = f"Olá {nome}, eu sou o PedroBot, sou capaz de executar tarefas básicas no seu computador e na internet."
robot.say(fala)
robot.runAndWait()
print("Não se preocupe, vou listar abaixo o que sou capaz de fazer :)⬇️")
robot.say(falas_bot.fala2)
robot.runAndWait()
print('====================================================================================================')
time.sleep(1)
def main():
    menu()

def menu():
    print('[1] - Abrir o seu navegador e digitar uma URL de sua escolha.')
    print("[2] - Abrir aplicações ou arquivos do seu computador.")
    print("[3] - Criar diretórios")
    print("[4] - Excluir diretórios")
    print("[5] - Acessar sua conta do facebook")
    print("[6] - Acessar sua conta do instagram")
    print("[7] - Encerrar Bot")
    print('[8] - Baixa vídeos ou músicas diretamente do YouTube.')
    print('[9] - Acessar plataformas de streaming')
    print("[10] - Conversar Comigo :)")
    print("[11] - Desligar computador")
    escolha = int(input('---> '))


    if escolha == 1:
        browser()
    elif escolha == 2:      
        aplicacao()
    elif escolha == 3:
        criar_diretorios()
        robot.say(falas_bot.fala4)
        robot.runAndWait()
    elif escolha == 4:
        excluir_diretorios()
        robot.say(falas_bot.fala5)
        robot.runAndWait()
    elif escolha == 5:
        robot.say(falas_bot.fala11)
        robot.runAndWait()
        facebook()
    elif escolha == 6:
        robot.say(falas_bot.fala12)
        robot.runAndWait()
        instagram()
    elif escolha == 7:
        print(f"Certo {nome}, encerrando tudo. Adeus..")
        time.sleep(2)
        fala4 = f"Certo {nome}, encerrando tudo. Mas vou fechar a aplicação. Até mais."
        robot.say(fala4)
        robot.runAndWait()
        pt.hotkey('ctrl', "'")
        pt.hotkey('alt', 'f4')

    elif escolha == 8:
        robot.say(falas_bot.fala15)
        robot.runAndWait()
        link = input("Digite o link do vídeo aqui. \nURL: ")
        download(link)

    elif escolha == 9:
        robot.say(falas_bot.fala18)
        robot.runAndWait()
        streaming()

    elif escolha == 10:
        robot.say(falas_bot.fala21)
        robot.runAndWait()
        pedrobot()

    elif escolha == 11:
        robot.say(falas_bot.fala13)
        robot.runAndWait()
        pt.hotkey('ctrl', "'")
        desligar()
    else:
        print(f"{nome}... colega, para eu te ajudar você precisa escolher uma opção válida")
        invalido = f"{nome}... colega, para eu te ajudar você precisa escolher uma opção válida"
        robot.say(invalido)
        robot.runAndWait()
        menu()


pt.PAUSE = 1

def browser():
    navegador = input("Digite o nome do seu navegador: ")
    site = input("Digite o nome do site que você deseja abrir [ex: youtube.com]: ")
    pc.copy(navegador)
    time.sleep(1)
    pt.press('Win')
    pt.hotkey("ctrl", "v")
    pt.press("enter")
    time.sleep(2)
    pc.copy(site)
    pt.hotkey("ctrl", "v")
    robot.say(falas_bot.fala8)
    robot.runAndWait()
    pt.press('enter')

def aplicacao():
    aplicacao = input("Digite a aplicação que você deseja abrir: ")
    pc.copy(aplicacao)
    time.sleep(1)
    pt.press('Win')
    time.sleep(1)
    pt.hotkey("ctrl", "v")
    robot.say(falas_bot.fala9)
    robot.runAndWait() 
    pt.press("enter")


def criar_diretorios():
    dir = input("Digite o nome do Dirétorio: ")
    os.makedirs(rf'C:\{dir}')
    caminho = f'C:\{dir}'
    print(f"Diretório criado em {caminho}")
    abrir_local_arquico = input('Deseja abrir o local do arquivo? [sim] | [nao] ')
    if abrir_local_arquico == 'sim':
        pc.copy(caminho)
        time.sleep(1)
        pt.press('Win')
        time.sleep(2)
        pt.hotkey('ctrl', 'v')
        pt.press('enter')
    else:
        print('Ok, encerrando por aqui!!')
        exit


def excluir_diretorios():
    rmdir = input("Digite o caminho do diretório que deseja excluir: ")
    print("ATENÇÃO!!! Os ditetórios removidos não podem ser recuperados!!")
    robot.say(falas_bot.fala6)
    robot.runAndWait()
    confirmar = input("Deseja continuar? [sim] [nao]: " )
    robot.say(falas_bot.fala7)
    robot.runAndWait()
    

    if confirmar == 'sim':
        try:
            os.rmdir(rmdir)
            print(f"O diretório {rmdir} foi removido")
        except OSError as e:
            print("O diretório deve está vazio!!")
    elif confirmar == 'nao':
        print("Certo, procedimento cancelado!")
        exit

    else:
        print("Comando inválido ou palavras digitadas de maneira incorreta..")
        time.sleep(2)
        print("..................")
        time.sleep(2)
        print("Procedimento cancelado.")


def facebook():
    print("Olá, para acessar sua rede social vou precisar do seu email e senha, certo? ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    time.sleep(1)
    print("Não se preocupe, nada aqui ficará salvo :)")
    robot.say(falas_bot.fala14)
    robot.runAndWait()

    time.sleep(2)


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)


    navegador.get("https://www.facebook.com/")

    navegador.find_element('xpath', '//*[@id="email"]').send_keys(email)
    time.sleep(2)
    navegador.find_element('xpath', '//*[@id="pass"]').send_keys(senha)
    time.sleep(2)
    pt.press('enter')


def instagram():
    print("Olá, para acessar sua rede social vou precisar do seu email e senha, certo? ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    time.sleep(1)
    print("Não se preocupe, nada aqui ficará salvo :)")
    robot.say(falas_bot.fala14)
    robot.runAndWait()
    time.sleep(2)


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)


    navegador.get("https://www.instagram.com/")
    time.sleep(4)
    navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
    time.sleep(2)
    navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
    time.sleep(2)
    pt.press('enter')



def desligar():
    print('Vou desligar pelo prompt, acho mais fácil :)')
    time.sleep(2)
    print("tchau tchau")
    print(".................................")
    prompt = "prompt de comando"
    pt.press('win')
    pt.write(prompt)
    pt.press('enter')
    pt.write('shutdown -s -t 00')
    pt.press('enter')


def download(link):
    tempo_inicial = time.time()
    print("Qual o formato desejado? ")
    print("[1] - Vídeo")
    print('[2] - Música')
    formato = int(input("-> "))

    if formato == 1:
        youtubeobject = YouTube(link)
        youtubeobject = youtubeobject.streams.get_highest_resolution()
        existe = os.path.exists(r'C:\YouTube\Youtube\Videos')
        local_arquivo = r'C:\YouTube\Youtube\Videos'
        if existe == True:
            print("Fazendo download do arquivo...")
            youtubeobject.download(local_arquivo)
            robot.say(falas_bot.fala16)
            robot.runAndWait()
        else:
            print("Fazendo download do arquivo...")
            os.makedirs(r'C:\YouTube\Youtube\Videos')
            youtubeobject.download(local_arquivo)
            robot.say(falas_bot.fala16)
            robot.runAndWait()
    else:
        youtubeobject = YouTube(link)
        youtubeobject = youtubeobject.streams.get_audio_only()
        existe = os.path.exists(r'C:\YouTube\Youtube\Músicas')
        local_arquivo = r'C:\YouTube\Youtube\Músicas'
        if existe == True:
            print("Fazendo download do arquivo...")
            youtubeobject.download(local_arquivo)
            robot.say(falas_bot.fala17)
            robot.runAndWait()
        else:
            print("Fazendo download do arquivo...")
            os.makedirs(r'C:\YouTube\Youtube\Músicas')
            youtubeobject.download(local_arquivo)
            robot.say(falas_bot.fala17)
            robot.runAndWait()

    tempo_final = time.time()
    print(f"O Download foi concluido em {tempo_final - tempo_inicial:.2f} segundos! \nO arquivo foi salvo na pasta {local_arquivo}")
    abrir_local_arquivo = input("Deseja abrir o local do aquivo? [s] [n]\n-> ")
    if abrir_local_arquivo == 's':
        pt.press('Win')
        pc.copy(local_arquivo)
        pt.hotkey('ctrl', 'v')
        pt.press('Enter')
    else:
        print("Ok, depois você olha!")
        time.sleep(2)

def streaming():
    print("Certo, consigo Acessar apenas as 6 plataformas mais usadas no momento. :)")
    print("Veja a lista e selecione: ")
    robot.say(falas_bot.fala19)
    robot.runAndWait()
    print('[1] - Netflix')
    print('[2] - Amazon Prime')
    print('[3] - HBO Max')
    print('[4] - GloboPLay')
    print('[5] - Disney+')
    print('[6] - Paramount+')
    stream = int(input('--> '))

    if stream == 1:
        stream = 'https://www.netflix.com/br/login'
    elif stream == 2:
        stream = 'https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fna.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3DsgzAXcp8YtrbDRghN_kvKyanXWRwYdmTUcGlKXnYe2OUZAAAAAQAAAABj6nIJcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2F%3Fgclid%253DEAIaIQobChMIo47wtIGT_QIVROZcCh0RmACuEAAYASAAEgLye_D_BwE%2526ref_%253Datv_auth_pre%2526mrntrk%253Dslid__pgrid_62046161446_pgeo_1031424_x__adext__ptid_kwd-297838409645&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_br&openid.mode=checkid_setup&siteState=131-3573104-4461732&language=pt_BR&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'

    elif stream == 3:
        stream = 'https://play.hbomax.com/signIn'

    elif stream == 4:
        stream = 'https://login.globo.com/login/6999/connect-confirm?url=https%3A%2F%2Fid.globo.com%2Fauth%2Frealms%2Fglobo.com%2Flogin-actions%2Fauthenticate%3Fsession_code%3D-68g_v0WLv0urlf7JiCNaiHt_nCe3m360aq8h8zmjCY%26execution%3Db5dd88dc-447e-468f-945e-e7c7de4883b7%26client_id%3Dvitrine-globo%2540apps.globoid%26tab_id%3DdqtNh3rFITU%26request-context%3DZgw8Vs&error=&request-context=Zgw8Vs'

    elif stream == 5:
        stream = 'https://www.disneyplus.com/pt-br/login'

    elif stream == 6:
        stream = 'https://www.paramountplus.com/br/account/signin/?redirectUrl=%2Faccount%2Fflow%2Ff-upsell%2Faction%2Flogin%2F'

    else:
        print("opção inválida, encerrando o código.")
        exit

    print("Muito bem, agora me diga qual navegador você usa: ")
    robot.say(falas_bot.fala20)
    robot.runAndWait()
    print('[1] - Google Chrome')
    print('[2] - Microsoft Edge')
    print('[3] - Firefox')
    nav = int(input('--> '))

    if nav == 1:
        nav = "Chrome"
    elif nav == 2:
        nav = "Microsoft edge"
    elif nav == 3:
        nav = "Firefox"
    else:
        print("Opção inválida, encerrando o código.")
        exit


    time.sleep(2)
    pt.press('win')
    time.sleep(1)
    pt.write(nav)
    pt.press('enter')
    time.sleep(1)
    pc.copy(stream)
    pt.hotkey('ctrl', 'v')
    pt.press('enter')


def pedrobot():
    print("Tudo bem, vamos conversar")
    print("Como podemos começar?")
    print("[1] - Conversa em Geral, nada específico")
    print("[2] - Desabafo")
    esc = int(input("---> "))

    if esc == 1:
        robot.say(falas_bot.fala23)
        robot.runAndWait()
        chatbot = ChatBot("PedroBot")
        trainer = ListTrainer(chatbot)
        trainer.train(Conversas)
        fala = "PedroBot: Olá, digíte 'sair' a qualquer momento para encerrar. :)"
        print(fala)
        while fala != "sair":
            fala = input("---> ")
            if fala == "sair":
                robot.say(falas_bot.fala24)
                robot.runAndWait()
                print("PedroBot: saindo..")
            else:
                resposta = chatbot.get_response(fala)

                print(f"PedroBot: {resposta}")

    elif esc == 2:
        robot.say(falas_bot.fala22)
        robot.runAndWait()
        chatbot = ChatBot("PedroBot")
        trainer = ListTrainer(chatbot)
        trainer.train(bot_psicologo)
        fala = "PedroBot: Olá, vamos conversar" 
        print("digíte 'sair' a qualquer momento para encerrar. :)")
        print(fala)
        while fala != "sair":
            fala = input("---> ")
            if fala == "sair":
                robot.say(falas_bot.fala24)
                robot.runAndWait()
                print("PedroBot: saindo..")
            else:
                resposta = chatbot.get_response(fala)

                print(f"PedroBot: {resposta}")



if __name__ == "__main__":
    main()