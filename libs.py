import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

token = open("TOKEN.txt").read()
bot = Bot(token=token)
dp = Dispatcher()