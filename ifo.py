import telebot
from telebot import types



bot = telebot.TeleBot('6151130386:AAHtmB_V_ptLB8RCqamIoETEweTUMrDvPAs')



@bot.message_handler(commands=['start', 'psinfo', 'skacat', '/ok'])
def reply(message):
    if message.text == '/start':
        bot.reply_to(message, 'hi i have this command(/psinfo,/skacat,/ok)')
    if message.text == '/psinfo':
        bot.reply_to(message, 'Adobe Photoshop ([əˈdəʊbɪ ˈfəʊtəʃɒp], Эдо́уби Фотошо́п, интернет-сленг Адо́б Фотошо́п) — многофункциональный графический редактор, разрабатываемый и распространяемый компанией Adobe Systems. В основном работает с растровыми изображениями, однако имеет некоторые векторные инструменты. Продукт является лидером рынка в области коммерческих средств редактирования растровых изображений и наиболее известной программой разработчика.В настоящее время Photoshop доступен на платформах macOS, Windows и iPadOS. Для Windows Phone и Android доступна упрощённая версия приложения под названием Adobe Photoshop Touch[8]. Также существует версия Photoshop Express для Windows Phone 8 и 8.1[9][10]. В 2014 году в США проходило бета-тестирование потоковой версии продукта для Chrome OS[11][12]. Ранние версии редактора были портированы под SGI IRIX[13], но официальная поддержка прекращена начиная с третьей версии продукта. Для версий 8.0 и CS6 возможен запуск под Linux с помощью альтернативы Windows API — Wine[14].')
    if message.text == '/skacat':
        bot.reply_to(message, 'tyt /ok')
    keyboard = types.InlineKeyboardMarkup()
    if message.text == '/ok':
        btn1 = types.InlineKeyboardButton('photos', url='https://softcatalog.io/ru/programmy/adobe-photoshop')
        keyboard.add(btn1)
        bot.send_message(message.from_user.id, 'skacat tyt', reply_markup=keyboard)





bot.infinity_polling()
