import json
from os import times
from types import ModuleType
import time
from banco import cadastro, conferirr, desmarcarr, find_user, horariosDisp, setHorario
#from database import *
from chatterbot import ChatBot
import telebot

key = open('key.txt', 'r')
token = key.readline()
bot = telebot.TeleBot(token)
'''chatbot = ChatBot('PizzaBot')'''
print('')
print('|================================|Bot on|================================|')


@bot.message_handler(commands=["agendar"])
def agendar(msg):
    bot.send_message(msg.chat.id, 'Estes são os horarios disponiveis:')
    # constants from telegram
    fname = msg.from_user.first_name
    lname = msg.from_user.last_name
    idTele = msg.from_user.id
    try:
        
        user = find_user(idTele)
        if len(user) <= 0:
        
            cadastro(idTele, lname, fname)

        t = horariosDisp()
        
        for i in range(len(t)):
            
            data = t[i][4]
            
            strdata = str(data)
            data = strdata.split(' ')[0]
            
            dia = data[8]+data[9]
            mes = data[5]+data[6]
            ano = data[0]+data[1]+data[2]+data[3]
            
            time = strdata.split(' ')[1]
            hora = time[0]+time[1]
            minuto = time[3]+time[4]
           
            bot.send_message(
                msg.chat.id, f'/Dia {dia} do mes {mes} no ano {ano} Horario {hora} e {minuto}'.replace("-", "_").replace(" ", "_"))
    except Exception as err:
        print(err)

@bot.message_handler(commands=["conferir"])
def conferir(msg):
    idTele = msg.from_user.id
    t = conferirr(idTele)
    
    if len(t) <=0:
        bot.send_message(msg.chat.id, f'Voce não tem consulta agendada, para agendar clique aqui -> /agendar')
   
    for i in range(len(t)):
        data = str(t[i][4])
        dia = data[8]+data[9]
        mes =data[5]+data[6]
        hora = data[11]+data[12]
        minuto = data[14]+data[15]
        bot.send_message(msg.chat.id, f'Voce tem consulta para o dia {dia} do mes {mes} as {hora}:{minuto}')


@bot.message_handler(commands=["desmarcar"])
def desmarcar(msg):
    idTele = msg.from_user.id
    var = desmarcarr(idTele)
    bot.send_message(msg.chat.id, var)

def verify(msg):
    return True

@bot.message_handler(func=verify)
def default(msg):
    name = msg.from_user.first_name
    idTele = msg.from_user.id
    texto = str(msg.text)

    if texto.startswith('/Dia'):
        print(texto)
        dia = texto[5]+texto[6]
        ano = texto[25]+texto[26]+texto[27]+texto[28]
        mes = texto[15]+texto[16]
        hora = texto[38]+texto[39]+':'+texto[43]+texto[44]+':00'
        print(dia+'-'+mes+'-'+ano+' '+hora)
        marcar = (ano+'-'+mes+'-'+dia+' '+hora)
       
        setHorario(name,idTele,marcar)

        bot.send_message(msg.chat.id, 'Vou marcar para o dia em questão')

    else:
        opcoes = f'''
        Ola {name}, o que deseja? 
/agendar => Aqui é onde agenda a consulta. 
/conferir => Aqui é onde voce revisa as sua consulta.
/desmarcar => Aqui é onde voce desmarcar a consulta. 
        '''

        bot.send_message(msg.chat.id, opcoes)


bot.polling()
