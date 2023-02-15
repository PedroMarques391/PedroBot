from topicos_bot import Conversas, bot_psicologo
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer  

#from spacy.cli import download
#Observação: Essa parte comentada só deve ser usada se houver na instalação do chatterbot.
            #download("en_core_web_sm")

                #class ENGSM:
            #ISO_639_1 = "en_core_web_sm" 


print("Tudo bem, vamos conversar")
print("Como podemos começar?")
print("[1] - Conversa em Geral, nada específico")
print("[2] - Desabafo")
esc = int(input("---> "))

if esc == 1:

    chatbot = ChatBot("PedroBot")
    trainer = ListTrainer(chatbot)
    trainer.train(Conversas)
    fala = "PedroBot: Olá, digíte 'sair' a qualquer momento para encerrar. :)"
    print(fala)
    while fala != "sair":
        fala = input("---> ")
        if fala == "sair":
            print("PedroBot: saindo..")
        else:
            resposta = chatbot.get_response(fala)

            print(f"PedroBot: {resposta}")

elif esc == 2:
    chatbot = ChatBot("PedroBot")
    trainer = ListTrainer(chatbot)
    trainer.train(bot_psicologo)
    fala = "PedroBot: Olá, vamos conversar" 
    print("digíte 'sair' a qualquer momento para encerrar. :)")
    print(fala)
    while fala != "sair":
        fala = input("---> ")
        if fala == "sair":
            print("PedroBot: saindo..")
        else:
            resposta = chatbot.get_response(fala)

            print(f"PedroBot: {resposta}")