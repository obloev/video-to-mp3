from aiogram import types

from database.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.BigInteger())
    language = db.Column(db.String())
    conversions = db.Column(db.Integer(), default=0)

    def __str__(self):
        return f'<User {self.id}>'

    @staticmethod
    async def create_user():
        user = types.User.get_current()
        new_user = User()
        new_user.user_id = user.id
        await new_user.create()
        return new_user

    @staticmethod
    async def get_user(user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    @staticmethod
    async def user_exist() -> bool:
        current_user = types.User.get_current()
        user = await User.get_user(current_user.id)
        return bool(user)

    @staticmethod
    async def users_count() -> int:
        count = await db.func.count(User.id).gino.scalar()
        return count

    @staticmethod
    async def set_language(language: str):
        user_id = types.User.get_current().id
        user = await User.get_user(user_id)
        return await user.update(language=language).apply()

    @staticmethod
    async def get_lang(user_id: int) -> str:
        user = await User.get_user(user_id)
        return user.language

    @staticmethod
    async def add_conversion():
        user_id = types.User.get_current().id
        user = await User.get_user(user_id)
        conversions = user.conversions + 1
        return await user.update(conversions=conversions).apply()

    @staticmethod
    async def get_conversions() -> int:
        user_id = types.User.get_current().id
        user = await User.get_user(user_id)
        return user.conversions
