from aiogram.types import Message


async def text_help(message: Message) -> None:
    """Выводит меню помощи"""
    from bot.keyboards.Inline.help_message import help_message

    help_msg = 'Как уже все поняли, я несу радость, <u><i>а ты</i></u>?🎂\n\n' \
               'Ладно. Я стараюсь помогать своим пользователям👨‍👩‍👦\n\n' \
               'Поэтому я умею много всяких штук 😉\n\n' \
               'Нажимай на кнопки и узнавай, что да как 🤩\n' \
               '(если что, все команды можно вводить через / и ! 🙊)\n\n' \
               'Кстати, по вопросам - 👾@olider_db👾'

    await message.answer(help_msg, reply_markup=help_message())
