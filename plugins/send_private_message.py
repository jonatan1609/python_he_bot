from pyrogram import Client, Filters, Message


@Client.on_message(Filters.text & Filters.private & Filters.create(lambda _, m: m.text == "/start howtosharecode"))
async def how_to_share_code(_client: Client, message: Message):
    await message.reply(
            """
איך לשלוח קוד / שגיאה:
**עדיפות ראשונה:**
לשתף את הקוד באתר כמו nekobin.com,     ולשתף כאן את הקישור. [מומלץ להחליף את סיומת txt לסיומת py].
**עדיפות שניה:**
קיים כלי במחשב  שמאפשר לבצע צילומי מסך על חלק ספציפי במסך,
לוחצים ctrl + shift + s, בוחרים את האזור הרצוי שרוצים לשתף,
לאחר מכן ניגשים לטלגרם ולוחצים ctrl + v.

מומלץ גם לעבור על הקישור הזה:

https://github.com/shlomif/how-to-share-code-online"""
        )
