import os
import random
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import requests
from uuid import uuid4

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from PythonPSI.api import PSI

ADMIN_SDK_JSON = 'webscraper.json'
STORAGE_URL = 'https://firebasestorage.googleapis.com/v0/b/webscraper-425e3.appspot.com/o/'
SPEED_API_KEY = 'AIzaSyAqQW3GLZ0jGmj7B94dn4o0faFn1qB9LAc'

# 1668898496:AAES8vdQNeIxBT-6MJW88Ul9HJYsBu-kuss
# page speed api AIzaSyAqQW3GLZ0jGmj7B94dn4o0faFn1qB9LAc
# t.me/screnshoto_bot

cred = credentials.Certificate('webscraper.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'webscraper-425e3.appspot.com'
})
bucket = storage.bucket()

def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

def makeScreenShotByUrl(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(formaturl(url))

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    fileName = f'{random.getrandbits(64)}.png'
    driver.find_element_by_tag_name('body').screenshot(f'{fileName}')
    driver.quit()
    return fileName

def uploadToFirebase(file):
    newFileName = f'{random.getrandbits(64)}.png'
    blob = bucket.blob(newFileName)
    new_token = uuid4()
    metadata  = {"firebaseStorageDownloadTokens": new_token}
    blob.metadata = metadata
    blob.upload_from_filename(
        filename=file,
        content_type='image/png'    
        )
    os.remove(file)    
    print(f'{STORAGE_URL}{newFileName}?alt=media&token={new_token}')
    return f'{STORAGE_URL}{newFileName}?alt=media&token={new_token}'

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Приветствую тебя о мудрый {update.effective_user.first_name}')

def screenshot(update: Update, context: CallbackContext) -> None:
    screen_name = makeScreenShotByUrl(context.args[0])
    fileToMessage = uploadToFirebase(screen_name)
    print(fileToMessage)
    print(context.args[0])

    x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={formaturl(context.args[0])}&strategy=desktop&key={SPEED_API_KEY}'
    context.bot.send_document(chat_id=update.effective_chat.id, document=f'{fileToMessage}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{x}')

    # print(f'Requesting {x}...')
    # r = requests.get(x)
    # print(f'{r.json()}')

def anyperson(update: Update, context: CallbackContext) -> None:
    hash = random.getrandbits(16)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=f'https://thispersondoesnotexist.com/image?image={hash}')

updater = Updater('1668898496:AAES8vdQNeIxBT-6MJW88Ul9HJYsBu-kuss')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('screenshot', screenshot))
updater.dispatcher.add_handler(CommandHandler('anyperson', anyperson))

updater.start_polling()
updater.idle()