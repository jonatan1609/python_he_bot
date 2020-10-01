from pyrogram import Client, Filters, Message
from .utils import detect_exception


@Client.on_message(Filters.reply & Filters.command('paste', '#'))
async def paste_code(_client: Client, message: Message):
    await message.delete()
    await message.reply_to_message.reply(await detect_exception(message.reply_to_message.text))
   
