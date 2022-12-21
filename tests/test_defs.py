from src.defs import Action, Color

assert hex(Action.OK ^ Action.OK) == '0x0'
assert hex(Action.OK ^ Action.NONE) == '0xfff'