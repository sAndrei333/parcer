
from loader import cursor, bot, con, scheduler
from script.parser import parser_update

def parcerupdate():
    cursor.execute('SELECT * FROM data)')
    con.commit()
    data = cursor.fetchall()
    for user in data:
        user_id = user[0]
        task = scheduler.add_job(trigger='interval',
                                           seconds=1,
                                           kwargs={'user_id':user_id, 'bot': bot})
        task_id= task.id
        cursor.execute('UPDATE INTO data (task_id) VALUES (?)', [task_id])
        con.commit()

