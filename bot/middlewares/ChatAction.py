from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender
from aiogram.types import Message
from typing import Callable, Any, Dict, Awaitable


class ChatActionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        long_operation_type = get_flag(data, "long_operation")

        # Если такого флага на хэндлере нет
        if not long_operation_type:
            return await handler(event, data)

        # Если флаг есть
        async with ChatActionSender(
                action=long_operation_type,
                chat_id=event.chat.id
        ):
            return await handler(event, data)
