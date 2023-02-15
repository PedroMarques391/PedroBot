import pyautogui as pt
import pyperclip as pc
import time
import os

"""
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
pt.press('enter')

======================================================================

aplicacao = input("Digite a aplicação que você deseja abrir: ")
pc.copy(aplicacao)
time.sleep(1)
pt.press('Win')
time.sleep(1)
pt.hotkey("ctrl", "v")
pt.press("enter")

=========================================================================

dir = input("Digite o nome do Dirétorio: ")

os.makedirs(rf'C:\{dir}')

caminho = f'C:\{dir}'

print(f"Diretório criado em {caminho}")


rmdir = input("Digite o caminho do diretório que deseja excluir: ")
print("ATENÇÃO!!! Os ditetórios removidos não podem ser recuperados!!")
confirmar = input("Deseja continuar? [sim] [nao]: " )

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





from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

print("Olá, para acessar sua rede social vou precisar do seu email e senha, certo? ")
email = input("Digite seu email: ")
senha = input("Digite sus senha: ")
time.sleep(1)
print("Não se preocupe, nada aqui ficará salvo :)")
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


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


print("Olá, para acessar sua rede social vou precisar do seu email e senha, certo? ")
email = input("Digite seu email: ")
senha = input("Digite sus senha: ")
time.sleep(1)
print("Não se preocupe, nada aqui ficará salvo :)")
time.sleep(2)


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)


navegador.get("https://www.instagram.com/")

navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
time.sleep(1)
pt.press('enter')




import pyttsx3
import falas_bot




robot = pyttsx3.init()

robot.say(falas_bot.fala)

robot.runAndWait()

robot.say(falas_bot.fala2)

robot.runAndWait()



print("Certo, consigo Acessar apenas as 6 plataformas mais usadas no momento. :)")
print("Veja a lista e selecione")
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

print("Muito bem, agora me diga qual navegador você usa.")
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
pt.write(stream)
pt.press('enter')
"""





