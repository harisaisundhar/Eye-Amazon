import track
import logging
import os
import random
import sys
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def start_handler(bot, update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("Hello from Eye-Amazon!\nType /track <URL> to start tracking")


def tracker_handler(bot, update):
    # Creating a handler-function for /track command
    string=update["message"]["text"].replace("/track ", "")
    dta=track.tracker(string)
    logger.info("{}".format(dta["Result"]))
    update.message.reply_text("Output: {}".format(dta["Result"]))
    update.message.reply_text("Title: {}\nCost: {} {}".format(dta["Title"],dta["Curr"],dta["Cost"]))

def limit_handler(bot, update):
    # Creating a handler-function for /track command
    string=update["message"]["text"].replace("/limit ", "")
    track.setEscape(int(string))
    logger.info("Limit channged")
    update.message.reply_text("Limit changed to: {}".format(string))

def mail_handler(bot, update):
    # Creating a handler-function for /track command
    string=update["message"]["text"].replace("/mail ", "")
    track.setEscape(string)
    logger.info("Mail channged")
    update.message.reply_text("Limit changed to: {}".format(string))

def graph_handler(bot, update):
    # Creating a handler-function for /track command
    string=update["message"]["text"].replace("/graph ", "")
    track.graphh(string)
    datum="done"
    logger.info("Graph Analysis done")
    update.message.reply_text("Graph Analysis: {}".format(datum))

if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("track", tracker_handler))
    updater.dispatcher.add_handler(CommandHandler("Track", tracker_handler))
    updater.dispatcher.add_handler(CommandHandler("graph", graph_handler))
    updater.dispatcher.add_handler(CommandHandler("limit", limit_handler))
    updater.dispatcher.add_handler(CommandHandler("mail", mail_handler))
    run(updater)
