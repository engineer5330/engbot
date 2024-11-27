from libs import *


def addusers(name, password, datareg, discord_id, telegramm_id):
    cursor.execute('INSERT INTO users (name, password, datareg, iddis, idteller) VALUES (?, ?, ?, ?, ?)', (name, password, datareg, discord_id, telegramm_id))


def upVar(var, newVar, idteller):
    cursor.execute(f'UPDATE Users SET {var} = ? WHERE name = ?', (newVar, idteller))