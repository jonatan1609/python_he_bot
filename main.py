from pyrogram import Client, idle, handlers, filters
from plugins.utils import set_administrators


app = Client("PythonHeBot")
app.add_handler(handlers.MessageHandler(set_administrators, filters.command('refresh', '#')))
app.start()
app.loop.run_until_complete(set_administrators(app))
idle()
app.stop()
