import requests
import telebot
from telebot import types

a = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]=rtx3050&desktop_gpu[operation]=union&order=price:asc'
b = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]=rx6650xt&desktop_gpu[operation]=union&order=price:asc'
c = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]=rtx3060&desktop_gpu[operation]=union&order=price:asc'
d = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]=rtx3060ti&desktop_gpu[operation]=union&order=price:asc'
e = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]=rtx3070&desktop_gpu[operation]=union&order=price:asc'
f = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?desktop_gpu[0]=rx6750xt&desktop_gpu[operation]=union&order=price:asc'


urls_list = ','.join([a,b,c,d,e,f])
urls_list = urls_list.split(',')

token_orig = '5182672884:AAFthdowZppUFxeU45qG_LcdM4wTZqLhBgI'
bot = telebot.TeleBot(token_orig)


@bot.message_handler(commands=['start','help'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Get Prices', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    bot.send_message(message.from_user.id,text='Прайсы', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        try:
            for link in urls_list:
                r = requests.get(link)
                alllist = r.json()['products']
                bot.send_message(call.from_user.id,f"{alllist[0]['name']}',{alllist[0]['html_url']},\n{(alllist[0]['prices']['price_min']['amount'])}")
        except Exception as e:
            print(e)
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Get Prices', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    bot.send_message(call.from_user.id, text='Прайсы', reply_markup=keyboard)


bot.polling(none_stop=True)