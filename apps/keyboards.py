from libs import *

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Личный кабинет')],
    [KeyboardButton(text='Настройки'), KeyboardButton(text='Выход')]
], 
                           resize_keyboard=True,
                           input_field_placeholder="Выберите пункт")


reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрироваться')],
], 
                           resize_keyboard=True)


lk = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="test", callback_data="test")]
])

