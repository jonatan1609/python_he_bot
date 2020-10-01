from pyrogram import Client, Filters, Message
from .utils import detect_exception


@Client.on_message(Filters.reply & 'paste', '#'))
async def paste_code(_client: Client, message: Message):
    await message.reply(await detect_exception(message.reply_to_message.text))
   
