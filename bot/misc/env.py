from os import getenv
from typing import Final


class TOKENS:
    mathurai_TOKEN: Final = getenv('mathurai_TOKEN', "token isn't in env")
