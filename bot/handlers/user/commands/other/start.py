from aiogram.types import Message


async def cmd_start(message: Message) -> None:
    """Команда /start"""
    from bot.keyboards.Reply.start_bot import start_menu_kb

    start_text = '🆘<b>Помогите!</b> Эти <i>изверги</i> держат меня в заложниках! 😱\n\n' \
                 'Хаха, <u>шучу</u> 🤡 Я - <i><b>бот-помогатор</b></i> студентов группы <b>ПМР</b>❕\n\n' \
                 '👋<b><u>Приветствую!</u></b>\n\n' \
                 '✏️Напишите <b><i><u>/help</u></i></b> или нажмите на соответсвующую <b><i><u>кнопку</u></i></b>,' \
                 ' чтобы узнать, что я умею'

    await message.answer(start_text, reply_markup=start_menu_kb())
