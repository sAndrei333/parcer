
from aiogram.types import Message
from loader import router, cursor, con, scheduler
from aiogram import F

@router.message(F.text=='delete link')
async def delete(message: Message, state):
    user_id = message.chat.id
    task_id = state
    cursor.execute('SELECT * FROM data WHERE id=(?) )', [user_id])
    con.commit()
    if  not cursor.fetchall():
        await message.answer('no link available')
    else:
        await scheduler.remove_job(task_id)
        cursor.execute('DELETE id FROM data WHERE id=(?) )', [user_id])

