from aiogram.types import Message


async def cmd_start(message: Message) -> None:
    """Команда /start"""
    from bot.keyboards.start_bot import start_menu_kb

    start_text = '<b>Помогите мне 🆘!</b> Эти <i>изверги</i> держат меня в заложниках! 😱\n\n' \
                 'Хаха, <u>шучу</u> 😏 Я бот-помогатор студентов группы ПМР❕\n\n' \
                 '<b>Приветствую</b> 😇!\n\n' \
                 'Напишите <i><u>/help</u></i> или нажмите на соответсвующую <i><u>кнопку</u></i>,' \
                 ' чтобы узнать, что я умею. За одно о себе немножко расскажу 😊'

    await message.answer(start_text, reply_markup=start_menu_kb())
