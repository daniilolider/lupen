from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def schedule_message() -> InlineKeyboardMarkup:
    """Inline клавиатура сообщения Расписание"""

    builder = InlineKeyboardBuilder()

    week_position = InlineKeyboardButton(text='⬆️Какая сейчас неделя?⬇️', callback_data='week_position')

    monday = InlineKeyboardButton(text='1️⃣Понедельник', callback_data='monday_schedule')
    tuesday = InlineKeyboardButton(text='2️⃣Вторник', callback_data='tuesday_schedule')
    wednesday = InlineKeyboardButton(text='3️⃣Среда', callback_data='wednesday_schedule')
    thursday = InlineKeyboardButton(text='4️⃣Четверг', callback_data='thursday_schedule')
    friday = InlineKeyboardButton(text='5️⃣Пятница', callback_data='friday_schedule')

    week = InlineKeyboardButton(text='⬆️⬇️Вся неделя⬆️⬇️', callback_data='week_schedule')

    down_week = InlineKeyboardButton(text='⬇️Нижняя неделя⬇️', callback_data='down_week_schedule')
    schedule_photo = InlineKeyboardButton(text='📷Фотка расписания📝', callback_data='photo_week_schedule')
    up_week = InlineKeyboardButton(text='⬆️Верхняя неделя⬆️', callback_data='up_week_schedule')

    couple_now = InlineKeyboardButton(text='❓Какая сейчас пара?❔', callback_data='now_couple')

    builder.row(week_position)
    builder.row(monday, tuesday, wednesday)
    builder.row(thursday, friday, week)
    builder.row(down_week, schedule_photo, up_week)
    builder.row(couple_now)

    keyboard = builder.as_markup()

    return keyboard
