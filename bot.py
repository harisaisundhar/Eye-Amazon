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
    update.message.reply_text("Hello from Eye-Amazon!\nType /help to get commands")


def tracker_handler(bot, update):
    # Creating a handler-function for /track command
    if update["message"]["text"] != "/track":
        string=update["message"]["text"].replace("/track ", "")
        dta=track.tracker(string)
        logger.info("Result: {} For :{}".format(dta["Result"],update['message']['chat']['first_name']))
        update.message.reply_text("Output: {}".format(dta["Result"]))
        update.message.reply_text("Title: {}\nCost: {} {}".format(dta["Title"],dta["Curr"],dta["Cost"]))
    else:
        logger.info("Track error for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Proper input expected")

def limit_handler(bot, update):
    # Creating a handler-function for /track command
    if update["message"]["text"] != "/limit":
        string=update["message"]["text"].replace("/limit ", "")
        track.setEscape(int(string))
        logger.info("Limit channged for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Limit changed to: {}".format(string))
    else:
        logger.info("Limit error for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Proper input expected")

def mail_handler(bot, update):
    # Creating a handler-function for /track command
    if update["message"]["text"] != "/mail":
        string=update["message"]["text"].replace("/mail ", "")
        track.setEscape(string)
        logger.info("Mail channged for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Limit changed to: {}".format(string))
    else:
        logger.info("Mail error for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Proper input expected")

def graph_handler(bot, update):
    # Creating a handler-function for /track command
    if update["message"]["text"] != "/graph":
        string=update["message"]["text"].replace("/graph ", "")
        track.graphh(string)
        datum="done"
        logger.info("Graph Analysis done for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Graph Analysis: {}".format(datum))
    else:
        logger.info("Graph Analysis error for: {}".format(update['message']['chat']['first_name']))
        update.message.reply_text("Proper input expected")

def help_handler(bot, update):
    # Creating a handler-function for /track command
    logger.info("Help shown to: {}".format(update['message']['chat']['first_name']))
    update.message.reply_text("/start to start the bot. \n /track <URL> to track the product. \n /graph <URL> to get a detailed report of the product.\n /mail <MAIL_ID>to update your mail_id to get updates.\n /limit <Limit_rate> to change your threshold limit.\n /website to view git repository. \n/help to get help.")

if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("track", tracker_handler))
    updater.dispatcher.add_handler(CommandHandler("Track", tracker_handler))
    updater.dispatcher.add_handler(CommandHandler("graph", graph_handler))
    updater.dispatcher.add_handler(CommandHandler("limit", limit_handler))
    updater.dispatcher.add_handler(CommandHandler("mail", mail_handler))
    updater.dispatcher.add_handler(CommandHandler("help", help_handler))
    run(updater)
