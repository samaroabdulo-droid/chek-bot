import telebot

TOKEN = "9139836464:AAE58bU-JQ3Cvz-bePeyFEemKAr_-vebtA8"
ADMIN_ID = 6776153004 # ВСТАВЬ СЮДА СВОЙ ID - как узнать смотри ниже
bot = telebot.TeleBot(TOKEN)

NOMER_DS = "+992933328746"
last_user = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Салом, бародар! 👋\n\nЯ - CHOKADI BOT.RU\n\n💰 Цена: 5 сомони\n\n1. Отправь 5 сомони на ДС:\n" + NOMER_DS + "\n2. Отправь мне скрин чека оплаты 5 сомони\n3. Отправь мне чек, который надо проверить")

@bot.message_handler(content_types=['photo'])
def photo(message):
    # Клиенту - только это и ничего больше!
    bot.send_message(message.chat.id, "Подождите, идёт проверка...")
    # Тебе пересылаем чек для проверки
    last_user['id'] = message.chat.id
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(ADMIN_ID, "Проверь чек ☝️\nЕсли фальшивый - напиши /fake\nЕсли настоящий - напиши /real")

@bot.message_handler(commands=['fake'])
def fake(message):
    if message.chat.id != ADMIN_ID:
        return
    if 'id' in last_user:
        bot.send_message(last_user['id'], "❌ Чек фальшивый!")
    bot.send_message(ADMIN_ID, "Отправил клиенту: Чек фальшивый")

@bot.message_handler(commands=['real'])
def real(message):
    if message.chat.id != ADMIN_ID:
        return
    if 'id' in last_user:
        bot.send_message(last_user['id'], "✅ Чек настоящий! Начинаем работу!")
    bot.send_message(ADMIN_ID, "Отправил клиенту: Чек настоящий")

bot.polling(none_stop=True)