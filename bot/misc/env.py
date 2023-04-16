from os import getenv
from typing import Final
from dotenv import load_dotenv, find_dotenv


class KEYS:

    load_dotenv(find_dotenv())

    lupen_TOKEN: Final = getenv('lupen_TOKEN', "token isn't in env")

    creator_USERNAME: Final = getenv('creator_USERNAME', "username isn't in env")

    creator_ID: Final = getenv('creator_ID', "id isn't in env")

    # True - включен, False - whitelist выключен
    WHITELIST_STATUS: Final = bool(eval(getenv('WHITELIST_STATUS', "whitelist status isn't in env")))

    chatgpt_TOKEN: Final = getenv('chatgpt_TOKEN', "token isn't in env")

    ChatGPT_STATUS: Final = bool(eval(getenv('ChatGPT_STATUS', "chatpgt status isn't in env")))
