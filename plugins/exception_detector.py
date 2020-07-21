from pyrogram import Client, Filters, Message
from .utils import detect_exception, groups


@Client.on_message(~Filters.private & Filters.text & Filters.create(lambda _, m: all(x in m.text for x in (
            'Traceback (most recent call last):',
            'File', 'line', 'in', '.py'
    )) and len(m.text) > 250) & Filters.create(lambda _, m: str(m.chat.id) in groups))
async def handle_exception(_client: Client, message: Message):
    text = await detect_exception(message.text)
    await message.reply(
        f"""
        [{message.from_user.first_name}](tg://user?id={message.from_user.id})
        ככל הנראה ההודעה שנשלחה מכילה פירוט אודות שגיאה,
        [תוכן ההודעה הועבר לכאן מפאת אריכות ההודעה!]({text})
        """,
        disable_web_page_preview=True
    )
    await message.delete()
