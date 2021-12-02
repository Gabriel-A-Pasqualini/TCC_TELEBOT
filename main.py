import json
from os import times
from types import ModuleType
import time
from banco import cadastro, conferirr, convenios, desmarcarr, find_user, horariosDisp, setHorario
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
    # constants from telegram
    fname = msg.from_user.first_name
    lname = msg.from_user.last_name
    idTele = msg.from_user.id
    try:
        user = find_user(idTele)
        if len(user) <= 0:
        
            cadastro(idTele, lname, fname)

        t = horariosDisp()
        if len(t)<= 0:
            bot.send_message(msg.chat.id, f'Desculpe, estamos sem horários disponíveis.')
        
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
        bot.send_message(msg.chat.id, f'Você não tem consulta agendada, para agendar clique aqui -> /agendar')
   
    for i in range(len(t)):
        data = str(t[i][4])
        dia = data[8]+data[9]
        mes =data[5]+data[6]
        hora = data[11]+data[12]
        minuto = data[14]+data[15]
        bot.send_message(msg.chat.id, f'Você tem consulta para o dia {dia} do mês {mes} às {hora}:{minuto}')

@bot.message_handler(commands=["desmarcar"])
def desmarcar(msg):
    idTele = msg.from_user.id
    num = conferirr(idTele)
    if len(num) >= 1:
        idTele = msg.from_user.id
        var = desmarcarr(idTele)
        bot.send_message(msg.chat.id, var)
    else:
        bot.send_message(msg.chat.id, "Você não tem consulta para desmarcar")

@bot.message_handler(commands=["duvidas"])
def duvidas(msg):
    bot.send_message(msg.chat.id, "/D1 -> Como saber se o meu convênio é aceito pela Clínica Médica?")
    bot.send_message(msg.chat.id, "/D2 -> Existem estacionamentos próximos à Clínica Médica?")
    bot.send_message(msg.chat.id, "/D3 -> Como chegar as unidades da Clínica Médica")
    
@bot.message_handler(commands=["lista"])
def lista(msg):
    conv = convenios()  
    bot.send_message(msg.chat.id,"Segue a nossa lista de convênios:")
    for i in range(len(conv)):  
        bot.send_message(msg.chat.id,conv[i])

def verify(msg):
    return True

@bot.message_handler(func=verify)
def default(msg):
    name = msg.from_user.first_name
    idTele = msg.from_user.id
    texto = str(msg.text)
    textoL = texto.lower()
    opcoes = f'''
/agendar => Agendo sua consulta nos dias disponíveis. 
/conferir => Te mostro a data e horário de sua consulta agendada.
/desmarcar => Desmarco sua consulta. 
/duvidas => Dúvidas frequentes.
        '''

    if texto.startswith('/Dia'):
        num = conferirr(idTele)
        if len(num) == 0:
            print(texto)
            dia = texto[5]+texto[6]
            ano = texto[25]+texto[26]+texto[27]+texto[28]
            mes = texto[15]+texto[16]
            hora = texto[38]+texto[39]+':'+texto[43]+texto[44]+':00'
            print(dia+'-'+mes+'-'+ano+' '+hora)
            marcar = (ano+'-'+mes+'-'+dia+' '+hora)
       
            hora2 = texto[38]+texto[39]+':'+texto[43]+texto[44]
            setHorario(name,idTele,marcar) #ENVIO AO BANCO DE DADOS
            bot.send_message(msg.chat.id, 'Vou marcar para o dia em questão')
            time.sleep(1)
            return bot.send_message(msg.chat.id, f'Feito, está marcado para o dia {dia} do mes {mes} as {hora2}')
        
        return bot.send_message(msg.chat.id, 'Voce ja tem consulta marcada')    
    
    if textoL.startswith('oi') or textoL.startswith('ola') or textoL.startswith('bom dia') or textoL.startswith('boa tarde') or textoL.startswith('boa noite'):        
        
        bot.send_message(msg.chat.id, f"Olá {name}, em que posso ser útil?")
        return bot.send_message(msg.chat.id, opcoes)

    if texto.startswith('/D'):
        op = texto.split('D')[1]
        if op == '1':
            return bot.send_message(msg.chat.id, "Verifique nossa /lista de convênios médicos.")

        if op == '2':
            return bot.send_message(msg.chat.id, "Sim, a clínica possui estacionamento próprio.")

        if op == '3':
            return bot.send_message(msg.chat.id, "O endereço da unidade é a Rua das Amoras, 1456 Jardim das flores")    

        return bot.send_message(msg.chat.id, "Dúvida não disponível") 
   
    bot.send_message(msg.chat.id, "Desculpe, não entendi o que disse...")
    return bot.send_message(msg.chat.id, opcoes)

bot.polling()