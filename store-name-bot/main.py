from telebot import TeleBot
from telebot.types import Message
from TOKEN import TOKEN
import os

DIR_TO_FILE = 'content/'
FILE_NAME = 'names_and_surnames.txt'

bot = TeleBot(TOKEN)

# TODO: add logging to the function
def send_message(chat_id, text, **args):
    bot.send_message(chat_id, text, **args)

def append_to_file(dir_name, file_name, text):
    # if there is no such dir, create dir
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    full_path = os.path.join(dir_name, file_name)
    
    # write to the file
    with open(full_path, 'a') as _file:
        _file.write(text)

@bot.message_handler(commands=['start'])
def start_message(message: Message):
    """
    Start message.
    """
    send_message(message.chat.id, "Send me your name in the following format:\nName surname")

# TODO: figure out how to deal with spam
 
@bot.message_handler(content_types=['text'], regexp=r'^\w+ \w+$')
def proccess_name(message):
    """
    function for messages consisting of exactly 2 words
    """
    append_to_file(DIR_TO_FILE, FILE_NAME, message.text + '\n')
    send_message(message.chat.id, "Acknowledged!")


if __name__ == "__main__":
    bot_info = bot.get_me()
    print(f"BOT STARTED: {bot_info.first_name} @{bot_info.username}")

    bot.infinity_polling()