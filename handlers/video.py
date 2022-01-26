from aiogram import types
from aiogram.utils.callback_data import CallbackData

from keyboards.filename import filename_keyboard
from keyboards.subscribe import subscribe_keyboard
from loader import dp, bot
from utils.check_membership import check_membership

filename_cd = CallbackData('filename', 'bool', 'name')


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_video(message: types.Message):
    if not await check_membership(message.from_user.id):
        await message.answer('please subscribe', reply_markup=subscribe_keyboard())
        return
    video = message.video
    file_name = video.file_name
    mes: types.Message = await message.answer('Downloading ...')
    await video.download()
    await mes.edit_text('Converting ...')
    # convert
    await mes.delete()
    await message.answer('Name?', reply_markup=filename_keyboard(file_name))


@dp.callback_query_handler(filename_cd.filter(bool=True))
async def get_filename(query: types.CallbackQuery):
    await query.answer()
    await query.answer('Type Name?')
    await query.message.delete()
    # set state


# state
@dp.callback_query_handlers(filename_cd.filter(bool=False))
async def send_mp3(query: types.CallbackQuery, callback_data: dict):
    await query.answer()
    await query.message.delete()
    filename = callback_data['name']
    mes: types.Message = await query.answer('sending ...')
    await bot.send_chat_action(query.from_user.id, 'upload_voice')
    await bot.send_audio(query.from_user.id, filename)
    await mes.delete()
