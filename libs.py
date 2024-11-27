import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import sqlite3

connection = sqlite3.connect('engineeriys.db')
cursor = connection.cursor()

token = open("TOKEN.txt").read()
bot = Bot(token=token)
dp = Dispatcher()