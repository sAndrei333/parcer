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
async def add(message: Message, data):
    url = FormUrl()
    user_id = message.chat.id
    cursor.execute('SELECT id FROM data WHERE id=(?) )', [user_id])
    if cursor.fetchall():
         await message.answer(text='уже добавляли')
    else:
         await cursor.execute('INSERT INTO data (id) VALUES (?)', [user_id])
    con.commit()
    class_names = "styles_wrapper__5FoK7"
    inner_class_name = "styles_secondary__MzdEb"
    result = parse_website(data['url'], class_names, inner_class_name)[:5]
    with open(f'data/{user_id}.json', 'w', encoding='utf-8')as file:
        file.write(json.dumps(result))


@router.message(F.text=='xd')
async def FormUrl(message: Message, state: State(), url):
    user_id = message.chat.id
    task_id = state
    await state.update_data(url=message.text)
    data = await state.get_data()
    await state.clear()
    task = scheduler.add_job(parser_update(trigger='interval',
                                           seconds=60,
                                           kwargs={'user_id':user_id, 'bot': bot}))
    cursor.execute('INSERT INTO data (url), (id), (id_task) VALUES (?), (?), (?)', [url],[task.id],[task_id])
    con.commit()
    await kb_start(text='парсер запущен')









