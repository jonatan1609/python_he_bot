from pyrogram import Client, Filters
from .utils import groups


@Client.on_message(Filters.new_chat_members)
async def cant_being_here(_client, message):
    if str(message.chat.id) not in groups:
        await message.reply("I'm sorry, i Can't being here")
        await message.chat.leave()
