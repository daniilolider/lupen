from os import getenv
from typing import Final


class KEYS:
    mathurai_TOKEN: Final = getenv('lupen_TOKEN', "token isn't in env")
