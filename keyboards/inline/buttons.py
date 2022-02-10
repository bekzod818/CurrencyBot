from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

convert = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Ayirboshlash", callback_data='convert')]
    ]
)