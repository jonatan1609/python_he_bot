from aiohttp import ClientSession
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
channel = config['bot']['channel']
groups = [int(x) for x in config['bot']['allowed_groups'].split(',')]
bot_username = config['bot']['username'].strip('"')
admins = {}


async def set_administrators(app):
    global admins
    admins = {}
    for chat in groups:
        async for admin in app.iter_chat_members(chat, filter="administrators"):
            if admin.get(chat):
                admins[chat].append(admin.user.id)
            else:
                admins[chat] = [admin.user.id]


async def detect_exception(string):
    async with ClientSession() as session:
        async with session.post('https://nekobin.com/api/documents', data={"content": string}) as response:
            return "https://nekobin.com/{}.py".format((await response.json())['result']['key'])
