from libs import *

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Личный кабинет')],
    # [KeyboardButton(text='Настройки'), KeyboardButton(text='Выход')]
], 
                           resize_keyboard=True,
                           input_field_placeholder="Выберите пункт")


reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрироваться')],
], 
                           resize_keyboard=True)


lk = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Изменить имя", callback_data="change_name"), InlineKeyboardButton(text="Изменить пароль", callback_data="chanche_pass")],
    # [InlineKeyboardButton(text="Скин", callback_data="skin")]
    #[InlineKeyboardButton(text="Плащ", callback_data="cloak")]
])
