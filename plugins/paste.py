from pyrogram import Client, Filters, Message
from .utils import detect_exception


@Client.on_message(Filters.reply & Filters.command('paste', '#'))
async def paste_code(_client: Client, message: Message):

    await message.delete()

    if commander_status in ('creator', 'administrator') or original_message_sender_id == commander_id:

        original_message_sender_id = message.reply_to_message.from_user.id
        commander_id = message.from_user.id
        commander_status = await (_client.get_chat_member(message.chat.id, commander_id)).status

        await message.reply_to_message.delete()
        await (message.reply_to_message.reply(await detect_exception(message.reply_to_message.text)))
   
