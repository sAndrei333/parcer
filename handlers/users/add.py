from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from pyexpat.errors import messages

from keys.key import types, kb_start
from loader import router, cursor, con, scheduler, bot
from aiogram import F
from script.parser import parser_update, parse_website
import json
class FormUrl(StatesGroup):
    url = State()

@router.message(F.text == 'Добавить')
async def add(message: Message):
    url = State()
    user_id = message.chat.id

    cursor.execute('INSERT INTO data (url) VALUES (?)', [url])
    con.commit()
    cursor.execute('SELECT url FROM data WHERE id=(?) )', [url])
    con.commit()


    if url in con:
         await message.answer(text='уже добавляли')
    else:
         await State.set_state(url)






