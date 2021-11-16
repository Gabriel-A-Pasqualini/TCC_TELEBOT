import psycopg2
import telebot
import json

key = open('key.txt', 'r')
token = key.readline()
bot = telebot.TeleBot(token)

database = psycopg2.connect(
    user="postgres",
    password="pass",
    host="127.0.0.1",
    port="5432",
    database="clinica"
)

cursor = database.cursor()

def cadastro(idTele,lname,fname):
    try:
        sql = f"INSERT INTO paciente(id_telegram, F_Name, L_Name ) VALUES ('{idTele}','{lname}','{fname}')"
    
        cursor.execute(sql)

        database.commit()
        #recset = cursor.fetchall()
    except:
        print("O paciente ja esta cadastrados")

def horariosDisp():
    try:
        sql = "SELECT * FROM consultas WHERE status='disponivel' ORDER BY id"
  
        cursor.execute(sql)

        database.commit()

        return cursor.fetchall()
    
    except:
        print('Invalid value!')

def find_user(id):
    sql = f"SELECT * FROM paciente WHERE id_telegram = '{id}'"
    #sql = "SELECT * FROM paciente WHERE id_telegram != '12'"
    cursor.execute(sql)
    database.commit()
    
    return cursor.fetchall() 

def setHorario(nome,idtele,horario):
   
    sql = f"UPDATE consultas SET paciente ='{nome}',id_telegram ='{idtele}' ,status = 'indisponivel' WHERE date = '{horario}'"
    cursor.execute(sql)
    database.commit()
    
def conferirr(idtele):
    sql = f"SELECT * FROM consultas WHERE id_telegram = '{idtele}'"
    cursor.execute(sql)
    database.commit()
    
    return cursor.fetchall()
    
def desmarcarr(idTele):
    sql = f"UPDATE consultas SET paciente ='',id_telegram ='' ,status = 'disponivel' WHERE id_telegram = '{idTele}'"
    cursor.execute(sql)
    database.commit()
    return 'Feito! Sua consulta foi desmarcada'    