from aiohttp import ClientSession
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
channel = config['bot']['channel']
groups = config['bot']['allowed_groups'].split(',')


async def detect_exception(string):
    async with ClientSession() as session:
        async with session.post('https://nekobin.com/api/documents', data={"content": string}) as response:
            return "https://nekobin.com/{}.py".format((await response.json())['result']['key'])
