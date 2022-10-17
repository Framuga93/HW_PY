from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters,ConversationHandler
import logging
import json
from config import TOKEN

bot = Bot(TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOICE, FIND, SHOW, ADD, DEL, EXPORT_CSV, EXPORT_JSON = range(7)

def start(update, _):
        update.message.reply_text(
        f"Привет! Я бот-справочник\n"
        f"Выберите необходимое действие\n")
        update.message.reply_text(
        "1. Найти сотрудника*в работе*\n" #find
        "2. Показать список сотрудников\n" #show 
        "3. Добавить сотрудника\n" #add
        "4. Удалить сотрудника*в работе*\n" #del
        "5. Экспортировать данные в формате json*в работе*\n" #exportjson
        "6. Экспортировать данные в формате csv\n" #exportcsv
        "Чтобы закончить работу введите команду /cancel")
        return CHOICE

def choice(update,context):
    user=update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '1234567':
        if user_choice == '1':
            update.message.reply_text(
                'Введите фамилию сотрудника')
            return FIND
        if user_choice == '2': return SHOW
        if user_choice == '3':
            update.message.reply_text(
                'Введите данные сотрудника в формате\n'
                'id,фамилия,имя и отчество, должность,телефон,зарплата')
            return ADD
        if user_choice == '4':
            update.message.reply_text(
                'Введите фамилию сотрудника для удаления')
            return DEL
        if user_choice == '5': return EXPORT_JSON
        if user_choice == '6': return EXPORT_CSV
        else: update.message.reply_text('Не валидное значение')

def export_csv(update,_):
    f =open('/Users/alekseydemockin/Desktop/GeekBrains/znakomstvo_python/Home_Work/BOT/database.csv' , 'rb')
    bot.send_document(update.effective_chat.id, f)
    f.close()
    return ConversationHandler.END

def show(update,context):
    with open('/Users/alekseydemockin/Desktop/GeekBrains/znakomstvo_python/Home_Work/BOT/database.csv' , 'r') as fin:
        for row in fin:
            context.bot.send_message(update.effective_chat.id, row)
    return ConversationHandler.END

# def find(update,context):
#     with open('/Users/alekseydemockin/Desktop/GeekBrains/znakomstvo_python/Home_Work/BOT/database.csv','r') as f:
#         reader = csv.reader(f)
#         update.message.reply_text('Insert second name: ')
#         second_name = update.message.text
#         for row in reader:
#             if second_name == row[1]:
#                 context.bot.send_message(update.effective_chat.id, row)

def add(update,_):
    with open('/Users/alekseydemockin/Desktop/GeekBrains/znakomstvo_python/Home_Work/BOT/database.csv','a') as f:

        f.write(update.message.text)
        f.close()
    return ConversationHandler.END


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Досвидания',
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            SHOW: [MessageHandler(Filters.text,show)],
            EXPORT_CSV: [MessageHandler(Filters.text, export_csv)],
            CHOICE: [MessageHandler(Filters.text, choice )],
            ADD: [MessageHandler(Filters.text, add)],
        },
        fallbacks=[CommandHandler('cancel',cancel)]
    )
    dispatcher.add_handler(conversation_handler)
    updater.start_polling()
    updater.idle()