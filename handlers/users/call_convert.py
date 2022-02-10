import logging
from loader import dp
from aiogram import types
from states.currency import Converter
from keyboards.inline.valyuta import valyuta, back
from keyboards.inline.buttons import convert
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text_contains="convert")
async def converter_cur(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text("🔄Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=valyuta)
    # await call.message.delete()
    await Converter.from_cur.set()


@dp.callback_query_handler(text_contains="UZS", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="RUB", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="USD", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="EUR", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="GBP", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="CNY", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="KRW", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="TRY", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="KT", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"from_cur": callback_data},
    )
    await call.message.edit_text("🔄Tanlagan valyutangizni qaysi valyuta bilan ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.next()


@dp.callback_query_handler(text_contains="UZS", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="USD", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()
    

@dp.callback_query_handler(text_contains="RUB", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="EUR", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="GBP", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="CNY", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="KRW", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="TRY", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()


@dp.callback_query_handler(text_contains="KZT", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await state.update_data(
        {"to_cur": callback_data},
    )
    await call.message.edit_text("🔄Ayirboshlash uchun son kiriting:\nMasalan: 1 yoki 1.1", reply_markup=back)
    await Converter.next()

@dp.callback_query_handler(text_contains="back", state=Converter.amount)
async def from_to(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_text("🔄Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.from_cur.set()


@dp.callback_query_handler(text_contains="back", state=Converter.to_cur)
async def from_to(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_text("🔄Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=valyuta)
    await Converter.from_cur.set()


@dp.callback_query_handler(text_contains="back", state=Converter.from_cur)
async def from_to(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.edit_text(f"Xush kelibsiz!", reply_markup=convert)
    await state.finish()