from pyrogram import Client, idle
from plugins.utils import set_administrators


app = Client("PythonHeBot")
app.start()
app.loop.run_until_complete(set_administrators(app))
idle()
app.stop()
