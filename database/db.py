import logging
from gino import Gino

from utils.config import POSTGRES_URI

db: Gino = Gino()


async def connect_db() -> None:
    await db.set_bind(POSTGRES_URI)
    await db.gino.create_all()
    logging.info('Connected to DB')
