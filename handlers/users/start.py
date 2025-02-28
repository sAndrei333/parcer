from tkinter import Button

from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router

@router.message()
async def start(message: Message):
    builder = ReplyKeyboardBuilder()

