
from typing import NamedTuple
from defs import Color

class Pallete(NamedTuple):
    tr: Color
    fg: Color
    bg: Color
    
class Margin(NamedTuple):
    h: int
    v: int