from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

valyuta = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="UZS", callback_data='UZS'), InlineKeyboardButton(text="RUB", callback_data='RUB'), InlineKeyboardButton(text="USD", callback_data='USD')],
        [InlineKeyboardButton(text="EUR", callback_data='EUR'), InlineKeyboardButton(text="GBP", callback_data='GBP'), InlineKeyboardButton(text="CNY", callback_data='CNY')],
        [InlineKeyboardButton(text="KRW", callback_data='KRW'), InlineKeyboardButton(text="TRY", callback_data='TRY'), InlineKeyboardButton(text="KZT", callback_data='KZT')],
        [InlineKeyboardButton(text="Ortga", callback_data='back')]
    ]
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ortga", callback_data="back")]
    ]
)