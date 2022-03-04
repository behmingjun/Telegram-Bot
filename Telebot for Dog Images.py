import Constants as keys
from telegram.ext import * ## telegram.ext package is for programming backend usage, telegram package for telegram frontend info usage
import Responses as R
import requests


print("Bot started...")

def start_command(update, context):   # update is the update(reply) you want to give to user, context is the input from user (command line argument)
    print(update)
    print('\nThis is the chat id:', update['message']['chat']['id'])
    print(update.message.chat_id)
    print()
    print(context)
    update.message.reply_text("Type something random to get started!")
    context.bot.send_message(update.effective_message.chat_id, text="testtest")
    update.message.reply_photo('https://hips.hearstapps.\
                               com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden\
                               -royalty-free-image-1586966191.jpg?crop=1.00\
                               xw:0.669xh;0,0.190xh&resize=1200:*')
    
def help_command(update, context):
    update.message.reply_text("Just type somethingggg")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def get_url():
    content = requests.get("https://random.dog/woof.json").json()
    url = content['url']
    return url

def image_command(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    update.message.reply_photo(photo = url)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    print(keys.API_KEY)
    
    updater = Updater(keys.API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("sendimage", image_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
