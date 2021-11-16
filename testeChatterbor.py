from chatterbot import ChatBot
import chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer, Trainer
from spacy.cli import download

chatbot = ChatBot('PizzaBot')
trainer = ListTrainer(chatbot)

chatTast = [
    "Ola tudo bem?",
    "Sim, e com voce?",
    "Tambem estou",
    "Fazendo o que de bom?",
    "Te treinando kkk",
    "A é kkkkk",
]
trainer = ListTrainer(chatbot)
trainer.train(chatTast)

while True:
    mensagem = input('Voce: ')
    resposta = chatbot.get_response(mensagem)
    print(resposta)