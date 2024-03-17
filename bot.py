from aiogram import Bot, Dispatcher, executor, types

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = Bot(token="6391985504:AAG59nToj2HuJsJOSei_AhYErKTgsGq710Y")
dp = Dispatcher(bot)

# Define a function to handle the /start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Welcome to the Votes to text! Send me a vote and I will echo the text back to you. owner @M7MED1573")

# Define a function to handle votes
@dp.message_handler(content_types=types.ContentType.POLL)
async def handle_vote(message: types.Message):
    vote_question = message.poll.question
    options = message.poll.options
    options_text = "\n".join(f"{index + 1}. {option.text}" for index, option in enumerate(options))
    response = f"Your vote: \n{vote_question}\nOptions:\n{options_text}"
    await message.reply(response)

async def main():
    # Start the bot
    await executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
    executor.start_polling(dp, skip_updates=True)
