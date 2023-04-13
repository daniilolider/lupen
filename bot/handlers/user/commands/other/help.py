from aiogram.types import Message


async def cmd_help(message: Message) -> None:
    """Выводит меню помощи"""
    from bot.keyboards.Inline.help_message import help_message

    help_msg = '<b>🤖Как все уже поняли, я несу радость, <u><i>а ты</i></u>?</b> 🎂\n\n' \
               '🕋Ладно. Я <b>стараюсь</b> помогать своим <b>пользователям</b>\n\n' \
               '🔮<i>Поэтому я умею много всяких</i> <b>штук</b>\n\n' \
               '💡Нажимай на <b>кнопки</b> и <b>узнавай</b>, что да как\n' \
               '(<i>если что, все команды можно вводить через</i> <b>/</b> <i>и</i> <b>!</b> 🙊)\n\n' \
               'Кстати, <b>по вопросам</b> - 👾<b>@olider_db</b>👾'

    await message.answer(help_msg, reply_markup=help_message())
