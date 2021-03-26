from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import requests

BOTNAME = "Adilson"

chatbot = ChatBot(BOTNAME)

conversation = [
    "Olá",
    "Oi!",
    "Como vai?",
    "Estou bem.",
    "É bom saber.",
    "Obrigado.",
    "Por nada."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

while True:
    try:
        print("User: ")
        text_input = input()

        if 'citação' in text_input:
            response = requests.get('https://api.quotable.io/random')
            
            if response.status_code == 200:
                data = response.json()
                quote = f'{data["content"]} ({data["author"]})'
            else:
                quote = 'Não consegui recuperar uma citação neste momento, desculpe.'
            
            rest = quote

        else:
            rest = chatbot.get_response(text_input)

        print(BOTNAME+": ", rest)

    except(KeyboardInterrupt, EOFError, SystemExit):
        print(" Deu pau :(")
        break