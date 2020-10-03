from aiohttp import ClientSession
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
channel = config['bot']['channel']
groups = [int(x) for x in config['bot']['allowed_groups'].split(',')]
bot_username = config['bot']['username'].strip('"')
admins = {}


async def set_administrators(app, message=None):
    global admins
    if not message or message.from_user.id in admins.get(message.chat.id):
        for chat in groups:
            admins[chat] = [admin.user.id async for admin in app.iter_chat_members(chat, filter="administrators")]
        return message.reply("Admins list updated successfully.") if message else ...
    return message.reply("You have no permission to update the admins list.")


async def detect_exception(string):
    async with ClientSession() as session:
        async with session.post('https://nekobin.com/api/documents', data={"content": string}) as response:
            return "https://nekobin.com/{}.py".format((await response.json())['result']['key'])
