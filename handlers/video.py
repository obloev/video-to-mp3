import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.filename import filename_keyboard, filename_cd
from keyboards.subscribe import subscribe_keyboard
from loader import dp, bot
from utils.check_membership import check_membership
from utils.to_mp3 import to_mp3


class Audio(StatesGroup):
    get_name = State()


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_video(message: types.Message):
    if not await check_membership(message.from_user.id):
        await message.answer('please subscribe', reply_markup=subscribe_keyboard())
        return
    video = message.video
    mes = await message.answer('Downloading ...')
    await video.download(destination_file='video_0.mp4')
    await mes.edit_text('Converting ...')
    to_mp3(message.from_user.id, 'video_0.mp4')
    await mes.delete()
    await message.answer('Name?', reply_markup=filename_keyboard())


@dp.callback_query_handler(filename_cd.filter(bool=True))
async def get_filename_callback(query: types.CallbackQuery):
    await query.answer()
    await query.answer('Type Name?')
    await query.message.delete()
    await Audio.get_name.set()


@dp.message_handler(state=Audio.get_name)
async def get_filename(message: types.Message, state: FSMContext):
    filename: str = f'media/{message.from_user.id}/audios/file_0.mp3'
    new_filename = f'media/{message.from_user.id}/audios/{message.text}.mp3'
    os.rename(filename, new_filename)
    await bot.send_audio(message.from_user.id, new_filename)
    await state.finish()


@dp.callback_query_handler(filename_cd.filter(bool=False))
async def send_mp3(query: types.CallbackQuery):
    await query.answer()
    await query.message.delete()
    filename: str = f'media/{query.from_user.id}/audios/file_0.mp3'
    mes: types.Message = await query.answer('sending ...')
    await bot.send_chat_action(query.from_user.id, 'upload_voice')
    await bot.send_audio(query.from_user.id, filename)
    await mes.delete()
