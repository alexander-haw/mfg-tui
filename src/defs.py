
from enum import Enum, IntEnum, auto

from picotui.basewidget import ACTION_OK
from picotui.defs import C_BLACK, C_GRAY, ATTR_INTENSITY
    
class Action(IntEnum):

    """https://help.sap.com/saphelp_ewm70/helpdata/en/7d/355fa04c3f11d4b5cd0004ac160649/content.htm?no_cache=true"""
    
    OK     = ACTION_OK
    CANCEL = auto()
    NEXT   = auto()
    PREV   = auto()

    ACTIVITY_STATUS_DEFAULT  = auto()
    ACTIVITY_STATUS_FIN_CONF = auto()
    ACTIVITY_STATUS_FIXED    = auto()
    ACTIVITY_STATUS_FXD_REL  = auto()
    ACTIVITY_STATUS_PARTCONF = auto()
    ACTIVITY_STATUS_RELEASED = auto()
    ACTIVITY_STATUS_STARTED  = auto()
    ALTERNATIVE_LINE_SWITCH  = auto()
    ASSIGN_ACTIONNET         = auto()
    COFFEE_REQUEST           = auto()
    CONFIGURATION_4_TRACKING = auto()
    NOTIFICATION_SEND        = auto()
    ORDER_CHECK_ATP          = auto()
    ORDER_DEALLOCATE         = auto()
    ORDER_DELETE             = auto()
    ORDER_INITIALIZE         = auto()
    ORDER_MODIFY_GENERIC     = auto()
    PROCESS_ACTIONS_4_POINT  = auto()
    PRODUCTION_BACKFLUSH     = auto()
    PRODUCTION_TRACKING      = auto()
    FOT_ORDER_MERGE          = auto()
    FOT_ORDER_PRODCH         = auto()
    FOT_ORDER_SPLIT          = auto()

    NONE   = 3095
    
class Key(bytes, Enum):
    
    TAB       = b'\t'
    ENTER     = b'\r'
    BACKSPACE = b'\x7f'
    QUIT      = b'\x03'
    ESC       = b'\x1b'

    UP        = b'\x1b[A'
    DOWN      = b'\x1b[B'
    LEFT      = b'\x1b[D'
    RIGHT     = b'\x1b[C'
    END       = b'\x1b[F'
    HOME      = b'\x1b[H'
    SHIFT_TAB = b'\x1b[Z'

    DELETE = b'\x1b[3~'
    PGUP   = b'\x1b[5~'
    PGDN   = b'\x1b[6~'
    
    F1  = b'\x1bOP'
    F2  = b'\x1bOQ'
    F3  = b'\x1bOR'
    F4  = b'\x1bOS'
    F5  = b'\x1b[15~'
    F6  = b'\x1b[17~'
    F7  = b'\x1b[18~'
    F8  = b'\x1b[19~'
    F9  = b'\x1b[20~'
    F10 = b'\x1b[21~'

class Color(IntEnum):

    B = property(lambda self:
        self.value | ATTR_INTENSITY
    )

    BLACK     = C_BLACK
    RED       = auto()
    GREEN     = auto()
    YELLOW    = auto()
    BLUE      = auto()
    MAGENTA   = auto()
    CYAN      = auto()
    WHITE     = auto()
    GRAY      = C_GRAY; GREY = GRAY