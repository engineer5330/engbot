from libs import *
import apps.keyboards as kb
import apps.db.requests as rq
# from funcs import *

class Reg(StatesGroup):
    name = State()
    passwrord = State()


class changeName(StatesGroup):
    name = State()


class changePass(StatesGroup):
    password = State()
    

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.chat.type !='private':
        await message.answer(f"Привет, передите в личные сообщения, чтобы пользоваться ботом")
    else:  
        if await rq.CheckReg(message.from_user.id):
            await message.answer(f"С возвращением! {message.from_user.first_name}", reply_markup=kb.main)
        else:
            await message.answer(f"Привет {message.from_user.first_name}, чтобы пользовать ботом, нужно сперва зарегестрироваться", reply_markup=kb.reg)


@dp.message(F.text == "Личный кабинет")
async def lk(message: types.Message):
    user = await rq.GetData(message.from_user.id)
    await message.answer(f"Ваш профиль:\nИмя:{user.name}\n", reply_markup=kb.lk)

 
# @dp.callback_query(F.data == "test")
# async def catalog(callback: CallbackQuery):
#     await callback.answer("test")
#     await callback.message.answer("test")
 

@dp.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    if await rq.CheckReg(message.from_user.id):
        await message.answer(f"С возвращением! {message.from_user.first_name}", reply_markup=kb.main)
    else:
        await state.set_state(Reg.name)
        await message.answer("Введите ваше имя")
    

@dp.message(F.text == "Зарегистрироваться")
async def reg(message: Message, state: FSMContext):
    await reg_one(message, state)


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
    await state.clear()
 
    await rq.AddUsers(message.from_user.id, data["name"], hashlib.md5(str(data["password"]).encode()).hexdigest())
    await message.answer(f"Добро пожаловать {message.from_user.first_name}" ,reply_markup=kb.main)


@dp.callback_query(F.data == "change_name")
async def change_name(callback: CallbackQuery, state: FSMContext):
    await state.set_state(changeName.name)
    await callback.message.answer("Введите ваше новое имя")
    


@dp.message(changeName.name)
async def change_name1(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await rq.changeName(message.from_user.id, data["name"])
    user = await rq.GetData(message.from_user.id)
    await message.answer(f"Ваше имя изменено, {user.name}!" ,reply_markup=kb.main)
    await state.clear()


@dp.callback_query(F.data == "chanche_pass")
async def change_Pass(callback: CallbackQuery, state: FSMContext):
    await state.set_state(changePass.password)
    await callback.message.answer("Введите ваш новой пароль")
    


@dp.message(changePass.password)
async def change_Pass1(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    await rq.changePass(message.from_user.id, hashlib.md5(str(data["password"]).encode()).hexdigest())
    await message.answer(f"Ваше пароль изменён!" ,reply_markup=kb.main)
    await state.clear()
