import sqlite3
from db.requests import *

connection = sqlite3.connect('engineeriys.db')
cursor = connection.cursor()
    
    
async def funcsqlasync(tellid):
    return cursor.execute(f'SELECT name FROM users WHERE idteller = "{tellid}"').fetchall()

tellid = "engineer5330"
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(funcsqlasync(tellid))
event_loop.close()

# print(funcsqlasync(tellid))

# connection.commit()
# connection.close()