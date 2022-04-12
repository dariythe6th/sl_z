from typing import ClassVar

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from sqlalchemy import Float
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship
import time

print("Бот запущен.")
Base = declarative_base()
engine = create_engine('sqlite:///relation.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session=Session()

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text="Привет, я твой помощник для сна. \nЧтобы я смогу помочь тебе со сном утром под #утро пиши когда ты проснулся, во сколько лёг, ну и опиши свое состояние по шкале от 1 до 10")


def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    newansw = ['', '', '']
    try:
        s = text
        if s[0] == '#':
            if s[1:5] == 'утро':

                answ = s.split('\n')
                for i in range(int(len(answ))):
                    answ[i] = answ[i].strip()
                    for j in range(int(len(answ[i]))):
                        if answ[i][j].isdigit() or answ[i][j] == ':' or answ[i][j] == '.':
                            newansw[i-1] += answ[i][j]
                            #print(answ[i][j])
                    # if (answ[i][j].isalpha()):
                    # pass
                    # elif(answ[i][j]=='🌃' or answ[i][j]=='🌄' or answ[i][j]=='⌚' or answ[i][j]==' '):
                    # pass
                    # else:
                    # newansw +=answ[i][j]
        # if answer[0] == '#':
        # if answer[1:5] == 'утро':
        # i=6
        # while answer[i]!='\n':
        # time1 = answer[i]
        # i=
        # while answer[i] != '\n':
        #  time2 = answer[16:22]
        # rate = answer[29:31]
        # newansw = time1 + " - " + time2 + " Ты оценил сон на: " + rate
        #u1 = Users(name = '', name_id = 12)
        #b1 = Sleep(time_start = newansw[0], time_end =newansw[1] ,date = '2.03',rate =newansw[2] )
        #session.add(b1)
        #session.commit()
        context.bot.send_message(chat_id=chat.id, text='ты лег в '+ newansw[0]+", проснулся в " +newansw[1]+", а оценил на "+newansw[2])
    except:
        context.bot.send_message(chat_id=chat.id, text="Напишите сколько вы спали")


token = "5003896889:AAFlIPPPr7_-YFsN9_QO9nnO8W2e_L4ZSew"
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()



#class Users(Base):
 #   __tablename__ = 'users'
  #  id = Column(Integer, primary_key=True)
   # name = Column(String)
    #name_id = Column(String)
    #users_shares = relationship("Sleep")


class Sleep(Base):
    __tablename__ = "sleep"
    id = Column(Integer, primary_key=True)
    time_start = Column(String)
    time_end = Column(String)
    date = Column(String)
    rate = Column(String)
    #user_id = Column(Integer, ForeignKey("users.id"))



