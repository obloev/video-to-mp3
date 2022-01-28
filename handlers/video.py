import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from database.models import User
from keyboards.filename import filename_keyboard, filename_cd
from keyboards.subscribe import subscribe_keyboard
from loader import dp, bot
from utils.check_membership import check_membership
from utils.config import CHANNEL, JOINCHAT_URL, MAIN_BOT
from utils.to_mp3 import to_mp3


class Audio(StatesGroup):
    get_name = State()


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_video(message: types.Message):
    if not await check_membership(message.from_user.id):
        await message.answer_chat_action('typing')
        await message.answer(f'**Subscribe to the channel to use the bot [{CHANNEL}]({JOINCHAT_URL})**',
                             reply_markup=subscribe_keyboard())
        return
    video: types.Video = message.video
    if video.file_size <= 50 * 2 ** 20:
        await message.answer_chat_action('typing')
        mes: types.Message = await message.answer('📥 Downloading ...')
        await video.download(destination_dir=f'media/{message.from_user.id}')
        await mes.edit_text('🔄 Converting to 🎵 MP3 ...')
        to_mp3(message.from_user.id)
        direct = f'media/{message.from_user.id}/videos'
        os.remove(f'{direct}/{os.listdir(direct)[0]}')
        await mes.delete()
        await message.answer_chat_action('typing')
        await message.answer('**📝 Do you want to name the 🎵 MP3 file?**', reply_markup=filename_keyboard())
    else:
        await message.reply("**⚠️ Due to Telegram API limit we can't download video larger than 50 MB."
                            f"Use {MAIN_BOT}**")


@dp.callback_query_handler(filename_cd.filter(action='yes'))
async def get_filename_callback(query: types.CallbackQuery):
    await query.message.answer_chat_action('typing')
    await query.message.answer('💬 Type your preferred name for 🎵 the mp3 file')
    await query.message.delete()
    await Audio.get_name.set()


@dp.message_handler(state=Audio.get_name)
async def get_filename(message: types.Message, state: FSMContext):
    direct: str = f'media/{message.from_user.id}/audios'
    file: str = f'{direct}/{os.listdir(direct)[0]}'
    new_file: str = f'{direct}/{message.text}.mp3'
    os.rename(file, new_file)
    await User.add_conversion()
    await message.answer_chat_action('typing')
    mes: types.Message = await message.answer('**📤 Sending ...**')
    await message.answer_chat_action('upload_voice')
    with open(new_file, 'rb') as audio:
        bot_info = await bot.get_me()
        await bot.send_audio(message.from_user.id, audio, performer=bot_info.username,
                             caption=f'🎵 {bot_info.username}')
        audio.close()
    await mes.delete()
    await state.finish()
    os.remove(new_file)


@dp.callback_query_handler(filename_cd.filter(action='no'))
async def send_mp3(query: types.CallbackQuery):
    await query.message.delete()
    await User.add_conversion()
    direct: str = f'media/{query.from_user.id}/audios'
    file: str = f'{direct}/{os.listdir(direct)[0]}'
    await query.message.answer_chat_action('typing')
    mes: types.Message = await query.message.answer('**📤 Sending ...**')
    await query.message.answer_chat_action('upload_voice')
    with open(file, 'rb') as audio:
        bot_info = await bot.get_me()
        await bot.send_audio(query.from_user.id, audio, performer=bot_info.username,
                             caption=f'🎵 {bot_info.username}')
        audio.close()
    await mes.delete()
    os.remove(file)
