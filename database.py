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
        sql = "SELECT * FROM consultas WHERE status='disponivel'"
  
        cursor.execute(sql)

        database.commit()

        return cursor.fetchall()
    
    except:
        print('Invalid value!')

'''def find_user(id):
    sql = f"SELECT * FROM paciente WHERE id_telegram='{id}'"
    cursor.execute(sql)

    database.commit()

    return cursor.fetchall()
'''
