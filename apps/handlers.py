from libs import *
import apps.keyboards as kb


class Reg(StatesGroup):
    name = State()
    passwrord = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.chat.type !='private':
        await message.answer(f"Привет, передите в личные сообщения, чтобы пользоваться ботом")
    else:
        await message.answer(f"Привет!", reply_markup=kb.main)


@dp.message(F.text == "Личный кабинет")
async def lk(message: types.Message):
    await message.answer("Ваш профиль:\nИмя:engineer5330\nРоль:admin", reply_markup=kb.lk)
    
@dp.callback_query(F.data == "test")
async def catalog(callback: CallbackQuery):
    await callback.answer("test")
    await callback.message.answer("test")
    

@dp.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите ваше имя")


@dp.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.passwrord)
    await message.answer("Введите ваш пароль")
    

@dp.message(Reg.passwrord)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(Reg.passwrord)
    data = await state.get_data()
    await message.answer("res complete")
    await message.answer(f"Name:{data["name"]}\nPass:{data["password"]}")
    await state.clear()