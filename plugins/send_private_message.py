from pyrogram import Client, filters, types


@Client.on_message(filters.text & filters.private & filters.create(lambda _, __, m: m.text == "/start howtosharecode"))
async def how_to_share_code(_client: Client, message: types.Message):
    await message.reply(
            """
**אפשרות ראשונה**:
    להעתיק את הקוד לאתר כגון del.dog או nekobin.com,
    ולשלוח בקבוצה את הקישור,
    מומלץ להוסיף לסוף הקישור את את הסיומת של הקובץ,
     על מנת לצבוע את הטקסט.
    לדוגמה: `del.dog/mycode.py` 
    
**אפשרות שניה**:
    **במערכות Windows**:
         ניתן ללחוץ `Win+shift+S` ולסמן את הקטע הדרוש,
         או לחלופין `win+PrtSc` בשביל צילום מסך מלא,
         ולאחר מכן `Ctrl+V` בתוך טלגרם כדי לשלוח את התמונה.
    
    **במערכות Linux**:
        לרוב בשביל לבצע צילום מסך לוחצים `Ctrl+Shift+PrtSc`,
        או `Ctrl+PrtSc` בשביל מסך מלא,
        ומדביקים את התצלום בטלגרם על ידי `Ctrl+V`.


מומלץ לעבור על הקישור הזה:
https://github.com/shlomif/how-to-share-code-online

כמו כן מומלץ לבקר באתר הנועד למטרה זו:
screenshot.help
""")
