from aiogram.types import Message


async def cmd_my_id(message: Message):
    """Выводит id, username, firstname и lastname пользователя"""
    print('#########################################\n' 
           f'{message.chat.id} - chat id\n'
           f'{message.from_user.id} - user id\n'
           f'{message.from_user.first_name} - first name\n'
           f'{message.from_user.last_name} - last name\n'
           f'{message.from_user.username} - user name\n'
           f'#########################################\n\n')
