import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from database.models import User
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
        await message.answer_chat_action('typing')
        await message.answer('please subscribe', reply_markup=subscribe_keyboard())
        return
    video: types.Video = message.video
    await message.answer_chat_action('typing')
    mes: types.Message = await message.answer('Downloading ...')
    await video.download(destination_dir=f'media/{message.from_user.id}')
    await mes.edit_text('Converting ...')
    to_mp3(message.from_user.id)
    await mes.delete()
    await message.answer_chat_action('typing')
    await message.answer('Name?', reply_markup=filename_keyboard())


@dp.callback_query_handler(filename_cd.filter(action='yes'))
async def get_filename_callback(query: types.CallbackQuery):
    await query.message.answer_chat_action('typing')
    await query.message.answer('Type Name?')
    await query.message.delete()
    await Audio.get_name.set()


@dp.message_handler(state=Audio.get_name)
async def get_filename(message: types.Message, state: FSMContext):
    direct: str = f'media/{message.from_user.id}/audios'
    file: str = f'{direct}/{os.listdir(direct)[0]}'
    new_file: str = f'{direct}/{message.text}.mp3'
    os.rename(file, new_file)
    await User.add_conversion()
    await message.answer_chat_action('upload_voice')
    await bot.send_audio(message.from_user.id, new_file)
    await state.finish()
    os.rmdir(f'media/{message.from_user.id}')


@dp.callback_query_handler(filename_cd.filter(action='no'))
async def send_mp3(query: types.CallbackQuery):
    await query.message.delete()
    await User.add_conversion()
    direct: str = f'media/{query.from_user.id}/audios'
    file: str = f'{direct}/{os.listdir(direct)[0]}'
    await query.message.answer_chat_action('typing')
    mes: types.Message = await query.message.answer('sending ...')
    await query.message.answer_chat_action('upload_voice')
    await bot.send_audio(query.from_user.id, file)
    await mes.delete()
    os.rmdir(f'media/{query.from_user.id}')
