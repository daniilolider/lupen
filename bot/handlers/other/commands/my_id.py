from aiogram.types import Message


async def my_id(message: Message):
    """Выводит id, username, firstname и lastname пользователя"""
    print('#########################################\n' 
           f'{message.chat.id} - chat id\n'
           f'{message.from_user.id} - user id\n'
           f'{message.from_user.first_name} - firstname\n'
           f'{message.from_user.last_name} - lastname\n'
           f'{message.from_user.username} - username\n'
           f'#########################################\n\n')
