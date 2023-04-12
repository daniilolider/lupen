from aiogram import Router
from aiogram.filters import Text

from .vuz2_exam import vuz2_exam
from .vuz2_offset import vuz2_offset
from .vuz2_first_module import vuz2_first_module
from .vuz2_second_module import vuz2_second_module
from .vuz2_final_module import vuz2_final_module


def reg_vuz2_rating_message_callbacks(router: Router):
    router.callback_query.register(vuz2_exam, Text('exams'))
    router.callback_query.register(vuz2_offset, Text('offsets'))
    router.callback_query.register(vuz2_first_module, Text('first_module'))
    router.callback_query.register(vuz2_second_module, Text('second_module'))
    router.callback_query.register(vuz2_final_module, Text('finale_module'))
