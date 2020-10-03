from pyrogram import Client, filters, types
from .utils import detect_exception, admins


@Client.on_message(filters.reply & filters.command('paste', '#'))
async def paste_code(_client: Client, message: types.Message):

    await message.delete()
    original_message_sender_id = message.reply_to_message.from_user.id
    sender = message.from_user.id
    is_usable = message.from_user.id in admins.get(message.chat.id) or original_message_sender_id == sender

    if is_usable:

        await message.reply_to_message.delete()
        await (message.reply_to_message.reply(await detect_exception(message.reply_to_message.text)))
