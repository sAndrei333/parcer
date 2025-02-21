from sched import scheduler

from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import sqlite3
from apscheduler.schedulers.asyncio import AsyncIOScheduler
con = sqlite3.connect('data/data.db')
cursor = con.cursor()

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot= Bot(TOKEN)
scheduler= AsyncIOScheduler(timezone = 'Europe/Moscow')