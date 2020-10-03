from pyrogram import Client
from plugins.utils import set_administrators

app = Client("PythonHeBot")
app.run(set_administrators(app))
