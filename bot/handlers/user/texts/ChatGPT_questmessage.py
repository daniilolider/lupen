from aiogram.types import Message


async def txt_chatgpt_questmessage(message: Message):
    """Выводит подсказку по пользованию ChatGPT при нажатии на кнопку меню"""

    text = '📝Чтобы написать 🤖ChatGPT🤖 введите:\n' \
           '<i><b>/q</b></i> или <i><b>/?</b></i> и свой <b>текст</b> через пробел'

    await message.answer(text)
