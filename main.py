import asyncio
import logging
import sys
from os import getenv
import requests

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.methods.send_chat_action import SendChatAction

TOKEN = '6423408643:AAEnM4RNUCt03vxnRxbYtOwdl1fVchUBsko'

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("""Приветствую вас!
Я рад приветствовать вас здесь! Я ваш персональный помощник, готовый помочь с вашими запросами. Чем я могу помочь вам сегодня?""")


@dp.message(Command('end'))
async def end_session(message: Message):
    res = requests.post('https://jasik.alwaysdata.net/clear-ig-session',
                        json={'contactId': f'{message.from_user.id}JASIK'})
    await message.answer('До свидания!')


@dp.message()
async def answer(message: Message):
    data = {
        'message': message.text,
        'contactId': f'{message.from_user.id}JASIK',
    }
    res = requests.post('https://jasik.alwaysdata.net/jasikai', json=data)
    await message.answer(res.json()['message'])


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.MARKDOWN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
