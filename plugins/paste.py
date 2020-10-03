from pyrogram import Client, filters, types
from .utils import detect_exception, admins


@Client.on_message(filters.reply & filters.command('paste', '#'))
async def paste_code(_client: Client, message: types.Message):

    await message.delete()
    original_message_sender = message.reply_to_message.from_user
    sender = message.from_user.id
    is_usable = message.from_user.id in admins.get(message.chat.id) or original_message_sender.id == sender

    if is_usable:

        await message.reply_to_message.delete()
        await (message.reply_to_message.reply(
            f"[{original_message_sender.first_name}](tg://user?id={original_message_sender.id})"
            f"'s Message has been pasted -> {await detect_exception(message.reply_to_message.text)}"
        ))

