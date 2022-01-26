import logging
from gino import Gino

from utils.config import POSTGRES_URI

db = Gino()


async def connect_db() -> None:
    await db.set_bind(POSTGRES_URI)
    logging.info('Connected DB')
    await db.gino.create_all()
