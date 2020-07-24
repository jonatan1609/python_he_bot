from pyrogram import Client, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from .utils import bot_username


@Client.on_callback_query()
async def callback_handler(_client: Client, callback: CallbackQuery):
    ok, message, group = callback.data.split('|')
    if ok == 'False':
        user_message = await _client.get_messages(int(group), int(message))
        try:
            await user_message.reply(
                """
    \u200f[{}](tg://user?id={}), ההודעה נמחקה.
    {}
    """.format(
                    user_message.from_user.first_name,
                    user_message.from_user.id,
                    "לנוחיותך מצורף כאן הכותרת של התמונה: \n ```{}```".format(user_message.caption)
                    if user_message.caption else ''
                ), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                    "איך לשלוח קוד / שגיאה:",
                    url=f"t.me/{bot_username}?start=howtosharecode")]])
            )

            await (await _client.get_messages(group, int(message))).delete()
            await callback.edit_message_text('ההודעה טופלה!')
        except AttributeError:
            pass
    elif ok == 'True':
        await callback.edit_message_text('ההודעה טופלה!')
