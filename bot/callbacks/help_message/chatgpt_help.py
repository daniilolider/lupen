from aiogram.types import CallbackQuery


async def send_ChatGPT_help(callback: CallbackQuery):
    """Отправляет справку по обращению с ChatGPT"""

    schedule_help_text = '💬<b>Вы можете задать любой свой вопрос чат-боту <i>ChatGPT</i>!</b>\n\n' \
                         '✍️Для этого вам нужно ввести <b>/q</b> или <b>/?</b> и ' \
                         '<b>свой вопрос</b> через <b>пробел</b>\n\n' \
                         '✨Вы можете с ним и просто пообщаться, правда, я не знаю, ' \
                         'на какие темы вы будете общаться с роботом 😁'

    await callback.message.answer(schedule_help_text)
