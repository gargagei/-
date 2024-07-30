import telebot

botTimeWeb = telebot.TeleBot('6721737699:AAGiSXFOx1OVdiZtYQKqPTimWAmIhfXDBH4')

from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, Привет!\nЯ телеграмм - бот для подбора музыкального контента!"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Привет!', callback_data='yes')
  markup.add(button_yes)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call2):
   if function_call2.message:
      if function_call2.data == "yes":
         third_mess = "Каталог альбомов"
         markup = types.InlineKeyboardMarkup()
         button_yes2 = types.InlineKeyboardButton(text='Точки расставлены - Елка', url ="https://www.youtube.com/watch?v=E9pFeMKZR1I")
         markup.add(button_yes2)
         markup.add(types.InlineKeyboardButton(text='мои твои темные желания - ooes', url ="https://www.youtube.com/watch?v=E9pFeMKZR1I"))
         markup.add(types.InlineKeyboardButton(text='Export - Iowa', url="https://www.youtube.com/watch?v=E9pFeMKZR1I"))
         button_sure = types.InlineKeyboardButton(text = 'Это супер, я хочу добавить свои треки!', callback_data='yes2')
         markup.add(button_sure)
         button_no = types.InlineKeyboardButton(text='Это супер, но я не хочу добавлять сво свои альбомы!', callback_data='no')
         markup.add(button_no)
         botTimeWeb.send_message(function_call2.message.chat.id, third_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == "yes2":
        markup_reply == types.ReplyKeyboardMarkup(resize_keyboard= True)
        katalogal_id = types.KeyboardButton("Мой каталог альбомов")
        katalodtrk_id = types.KeyboardButton("Мой каталог треков")
        markup_reply.add(katalogal_id, katalodtrk_id)
        client.send_message(call.message.chat.id, "Нажмите на одну из кнопок")
        reply_markup = markup_reply

botTimeWeb.polling()


#...