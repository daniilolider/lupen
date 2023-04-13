from aiogram import Router
from aiogram.filters import Text

from .vuz2_exams import send_vuz2_exams
from .vuz2_offsets import send_vuz2_offsets
from .vuz2_first_module import send_vuz2_first_module
from .vuz2_second_module import send_vuz2_second_module
from .vuz2_final_module import send_vuz2_final_module


def reg_vuz2_rating_message_callbacks(router: Router):
    router.callback_query.register(send_vuz2_exams, Text('vuz2_exams'))
    router.callback_query.register(send_vuz2_offsets, Text('vuz2_offsets'))
    router.callback_query.register(send_vuz2_first_module, Text('vuz2_first_module'))
    router.callback_query.register(send_vuz2_second_module, Text('vuz2_second_module'))
    router.callback_query.register(send_vuz2_final_module, Text('vuz2_finale_module'))
