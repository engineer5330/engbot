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
    

class setSkin(StatesGroup):
    skin= State()
    

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.chat.type !='private':
        await message.answer(f"Привет, передите в личные сообщения, чтобы пользоваться ботом")
    else:  
        if await rq.CheckReg(message.from_user.id):
            await message.answer(f"С возвращением! {message.from_user.first_name}", reply_markup=kb.main)
        else:
            await message.answer(f"Привет {message.from_user.first_name}, чтобы пользовать ботом, нужно сперва зарегестрироваться", reply_markup=kb.reg)


# @dp.message(F.document)
# async def photo_mes(message: types.Message):
#     photo_id = message.document.file_id
#     photo_name = message.document.file_name
    
#     file = await bot.get_file(photo_id)
#     file_path = file.file_path
    
#     await bot.download_file(file_path, photo_name, chunk_size=99999)
#     await message.answer(f"{message.document}")
    


@dp.message(F.text == "Личный кабинет")
async def lk(message: types.Message):
    user = await rq.GetData(message.from_user.id)
    await message.answer(f"Ваш профиль:\nИмя:{user.name}\n", reply_markup=kb.lk)



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



@dp.callback_query(F.data == "change_Skin")
async def set_skin(callback: CallbackQuery, state: FSMContext):
    await state.set_state(setSkin.skin)
    await callback.message.answer("Отпавьте ваш скин")


@dp.message(setSkin.skin)
async def set_skin1(message: Message, state: FSMContext):
    await state.update_data(skin = message.document)
    skin = await state.get_data()
    skin = skin["skin"]
    photo_id = skin.file_id
    skin_name = skin.file_name
    
    file = await bot.get_file(photo_id)
    file_path = file.file_path
    user = await rq.GetData(message.from_user.id)
    user_name = user.name
    
    await bot.download_file(file_path, f"{user_name}.png", chunk_size=99999)
    
    if (os.path.exists(os.path.join("files", "skins", f"{user_name}.png"))):
        os.remove(os.path.join("files", "skins", f"{user_name}.png"))
    
    
    shutil.move(f"{user_name}.png", os.path.join("files", "skins"))
    
    
    await state.clear()
    await message.answer(f"Вы добавили скин! \n " ,reply_markup=kb.main)


@dp.callback_query(F.data == "skin")
async def skinlk(callback: CallbackQuery):
    user = await rq.GetData(callback.message.from_user.id)
    user_name = user.name
    await callback.message.answer_photo(photo=f'http://http://engineeriys.ru/bot/files/skins/{user.name}.png')
    await callback.message.answer(f"Ваш скин:\n", reply_markup=kb.skin)