import os

from Adafruit_IO import Client
p1=os.getenv('uname')
p2=os.getenv('feed')
aio = Client(p1,p2)


from telegram.ext import Updater , MessageHandler , Filters

def demo1(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the lights on')
  aio.send('light',1)
  
  
def demo2(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the lights off')
  aio.send('light',0)
  
  
def demo3(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the fan on')
  aio.send('fan',1)
  
  
def demo4(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the fan off')
  aio.send('fan',0)
  
  

def main(bot,update):
  a = bot.message.text
  if a =='Turn on light':
   demo1(bot,update)
   
  elif a =='Turn off light':
   demo2(bot,update)
   
  elif a =='Turn on fan':
   demo3(bot,update)
   
  elif a =='Turn off fan':
   demo4(bot,update)

bot_token = os.getenv('bot_token’)
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
 
  
