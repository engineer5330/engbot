import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, File, InputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import hashlib
import shutil, os

token = open("TOKEN.txt").read()
bot = Bot(token=token)
dp = Dispatcher()
