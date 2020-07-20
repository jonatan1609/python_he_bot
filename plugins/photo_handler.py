from pyrogram import Client, Filters, Message, InlineKeyboardMarkup, InlineKeyboardButton
from .utils import channel, groups


@Client.on_message(Filters.photo & Filters.create(lambda _, m: str(m.chat.id) in groups))
async def photo_handler(_client: Client, message: Message):
    chat = str(message.chat.id)
    await _client.send_photo(
        int(channel),
        message.photo.file_id,
        caption="[{}](tg://user?id={}) sent [it](t.me/c/{}/{}), is it ok?".format(
            message.from_user.first_name,
            message.from_user.id,
            chat[4:] if chat.startswith('-100') else chat,
            message.message_id
                                                                    ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('unreadable code.', 'False|{}|{}'.format(message.message_id, message.chat.id))
                ],
                [
                    InlineKeyboardButton("it's ok", 'True|{}|{}'.format(message.message_id, message.chat.id))
                ]
            ]
        )
    )
