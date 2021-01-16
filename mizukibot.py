''' Mizuki bot '''
from telebot import types
import telebot
import random
''' Token Mizuki's bot '''
bot = telebot.TeleBot("1352350957:AAFLjONVjc2kpvGmEEF1yli7mUw-TUqMADI", parse_mode=None) 

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_sticker(message.chat.id,
		"CAACAgQAAxkBAAEBxHRgAAGsiWdzZb8QYk7tDFKaCH2BgOYAAoQDAAKpxuIN2nvc_4Oj5eweBA")
	markup_w = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Рандомное число")
	item2 = types.KeyboardButton("🧐 Вопрос?")
	item3 = types.KeyboardButton("📚 Уравнение")
	item4 = types.KeyboardButton("🤚🏻 Привет")
	item5 = types.KeyboardButton("👋🏻 Пока")
	markup_w.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> даю тебе выбор из команд,выбирай."
		.format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup_w)

@bot.message_handler(commands=['help', 'info']) #help or info 
def support(message):
	markup_kl = types.ReplyKeyboardMarkup(row_width=3)
	item_kl1 = types.KeyboardButton("/start")
	markup_kl.add(item_kl1)

	bot.send_sticker(message.chat.id,
		"CAACAgIAAxkBAAEBxHJgAAGrtK1H7dYHBfYKpMjSf0Z5MPAAAugAA-JJzSIiENfLTjkjsx4E")
	bot.send_message(message.chat.id,
		"Чтобы использовать меня нужно нажать на /start снизу👇🏻 Или написать вручную.",
		reply_markup = markup_kl)

@bot.message_handler(content_types=['text'])
def answers(message):
	if message.text.lower() == "привет":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxH5gAAG-oleftKHsK9O0yFfQRFRZaNQAAvYAA-JJzSLZcZRTqToIyh4E")
		bot.send_message(message.chat.id,
			"Да-да,привет. ")
	elif message.text.lower() == "пока":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxH5gAAG-oleftKHsK9O0yFfQRFRZaNQAAvYAA-JJzSLZcZRTqToIyh4E")
		bot.send_message(message.chat.id, "До встречи✌🏻")
	elif message.text.lower() == "мне пора":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxH5gAAG-oleftKHsK9O0yFfQRFRZaNQAAvYAA-JJzSLZcZRTqToIyh4E")
		bot.send_message(message.chat.id,
			"Ну да... Пока в реале не проиграл, отмазок можно придумывать сколько угодно.")
	elif message.text == "🎲 Рандомное число":
		bot.send_message(message.chat.id, str(random.randint(0,100))) #function random
	elif message.text == "🧐 Вопрос?":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxHhgAAG6xSFHmekjPiUBiyk5Uj2eMCYAAs8AA-JJzSJxj82JnfAcRB4E")
		markup_ques = types.InlineKeyboardMarkup(row_width=2) 
		item_que1 = types.InlineKeyboardButton("Да,есть такое..", callback_data = 'well')
		item_que2 = types.InlineKeyboardButton("Нет,не считаю", callback_data = 'loser')
		markup_ques.add(item_que1, item_que2)

		bot.send_message(message.chat.id, "Вы считаете себя глупым?",
			reply_markup = markup_ques)
	elif message.text == "📚 Уравнение":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxHJgAAGrtK1H7dYHBfYKpMjSf0Z5MPAAAugAA-JJzSIiENfLTjkjsx4E")	
		markup_answer = types.ReplyKeyboardMarkup(row_width=1)
		item_an1 = types.KeyboardButton("√3^2")
		item_an2 = types.KeyboardButton("3")
		item_an3 = types.KeyboardButton("1√3")
		item_an4 = types.KeyboardButton("2√3")
		markup_answer.add(item_an1, item_an2, item_an3, item_an4)

		bot.send_message(message.chat.id, "Реши хотябы это😏",
			reply_markup = markup_answer)

	elif message.text == "√3^2":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxG5gAAGrjQbTiB1HESCnaJqnUgUY-lMAAgoBAALiSc0iplFtcxpn_hMeBA")
		bot.send_message(message.chat.id, "Нет,глупец!")
	elif message.text == "3":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxG5gAAGrjQbTiB1HESCnaJqnUgUY-lMAAgoBAALiSc0iplFtcxpn_hMeBA")
		bot.send_message(message.chat.id, "Нет,глупец!")
	elif message.text == "1√3":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxG5gAAGrjQbTiB1HESCnaJqnUgUY-lMAAgoBAALiSc0iplFtcxpn_hMeBA")
		bot.send_message(message.chat.id, "Нет,глупец!")
	elif message.text == "2√3":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxKNgAVRxKOY2igJow_vEBpsz59ZUmAACtwAD4knNIkmHaumAq1GYHgQ")
		bot.send_message(message.chat.id, "Это... Верно👌🏻")

	elif message.text == "🤚🏻 Привет":
		bot.send_message(message.chat.id,
			"Мне лень повторять,выбери что-нибудь поинтереснее..")
	elif message.text == "👋🏻 Пока":
		bot.send_sticker(message.chat.id,
			"CAACAgIAAxkBAAEBxKVgAV_url0d2frmY3R4T6XCHucxRQAC1QAD4knNIjM4bbu7SVsPHgQ")
		bot.send_message(message.chat.id, "Прощаай!")
	else:
		bot.send_message(message.chat.id, "Что ты несёшь?.. напиши /help")

@bot.callback_query_handler(func=lambda call: True)
def ending(call):
	try:
		if call.message:
			if call.data == 'well':
				bot.send_sticker(call.message.chat.id,
					"CAACAgIAAxkBAAEBxHBgAAGrnZ4H8rZyRcYFsMCApkOZl_gAAtYAA-JJzSKJGhbNUqmFxx4E")
				bot.send_message(call.message.chat.id, "Это правильный ответ🤭")
			elif call.data == 'loser':
				bot.send_sticker(call.message.chat.id,
					"CAACAgIAAxkBAAEBxGxgAAGrfwU0aNLqTNz2mBK0Aqa28I4AAuQAA-JJzSIUuwhBPyMpDh4E")
				bot.send_message(call.message.chat.id,
					"Перед тем, как соврать, хорошенько подумай о том, кому врёшь!")
			''' Исчезновение (disappear message) '''
			bot.edit_message_text(chat_id=call.message.chat.id,
				message_id=call.message.message_id, text="🧐 Вопрос?",
				reply_markup=None)

			''' Вывод сообщения (show alert) '''
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="Игра не закончена, пока мы умеем дышать.")

	except Exception as e:
    	 print(repr(e))


bot.polling(none_stop = True)
