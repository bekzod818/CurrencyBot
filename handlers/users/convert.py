from keyboards.inline.valyuta import back
from loader import dp
from aiogram import types
from states.currency import Converter
from aiogram.dispatcher import FSMContext
from data.converter import convert_cur


@dp.message_handler(state=Converter.amount)
async def result(message: types.Message, state: FSMContext):
    txt = message.text
    data = await state.get_data()
    from_cur = data.get("from_cur")
    to_cur = data.get('to_cur')
    res = convert_cur(from_cur, to_cur, amount=txt)
    msg = f"♻️Aylantirildi: {txt} {from_cur} ➡️ {res['res']} {to_cur}"
    await message.answer(msg, reply_markup=back)
    await Converter.amount.set()