from aiogram.types import Message
from loader import router, cursor, con, scheduler
from aiogram import F

@router.message(F.text=='delete link')
async def delete(message: Message):
    user_id = message.chat.id

    cursor.execute('SELECT url FROM data WHERE url=(?) )', [url])
    con.commit()
    if url not in con:
        await message('no link available')
    else:
        await scheduler.remove_job(task_id)


