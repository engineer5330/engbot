from libs import *

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.chat.type !='private':
        await message.answer(f"Привет, передите в личные сообщения, чтобы пользоваться ботом")
    else:
        await message.answer(f"Привет!")