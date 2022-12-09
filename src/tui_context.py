
import operator

from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from picotui.dialogs import *

from loguru import logger

logger.remove()

class Wcontext(Context):
    _align = (1, 1)
    
    def __init__(self, title: str, mouse=True):
        super().__init__(True, mouse)
        self.title = title
    
    def form_label(self, __txt: str) -> WLabel:
        self._align = tuple(map(operator.add, self._align, (0, 1)))
        self.dialog.add(*self._align, l := WLabel(__txt))
        return l
                
    def form_newline(self):
        self.form_label("")
                     
    def form_input(self, __txt: str, __pattern: str) -> WTextEntry:
        self.form_label(__txt)
        __pattern = "".join(filter(lambda c: c not in "\\{}-", iter(__pattern)))
        self.dialog.add(self._align[0] + len(__txt), self._align[1], (t:=WTextEntry(len(__pattern)+1, "") ))
        return t
        
    def form_ok_cancel(self):
        self.dialog.add(int(self.width/2-16), self.height-8, (ok := WButton(8, "OK")))
        self.dialog.add(int(self.width/2), self.height-8, (cancel := WButton(8, "CANCEL")))
        ok.finish_dialog = ACTION_OK
        cancel.finish_dialog = ACTION_CANCEL

    def form_ok(self):
        self.dialog.add(int(self.width/2-8), self.height-8, (ok := WButton(8, "OK")))
        ok.finish_dialog = ACTION_OK

    def form_inc_dec(self, __val):
        self.dialog.add(int(self.width/2-20), self._align[1], (inc := WButton(5, "▲")))
        self.dialog.add(int(self.width/2)+5, self._align[1], (dec := WButton(5, "▼")))
        # self.dialog.add(int(self.width/2), self._align[1], (dec := WButton(5, "▼")))
        self.dialog.add(int(self.width/2)-6, self._align[1], WLabel(__val))
        # inc.finish_dialog = ACTION_NEXT
        # dec.finish_dialog = ACTION_PREV

    def popup_input(self, __txt: str, __pattern: str) -> str:
        i = DTextEntry(int(len(__pattern)), "", title=__txt).clear_to_eol()
        self.dialog.redraw()
        return i
    
    def __enter__(self):
        super().__enter__()
        Screen.attr_color(C_WHITE, C_CYAN)
        Screen.cls()
        Screen.attr_reset()
        self.dialog = Dialog(3, 3, self.width - 6, self.height - 6, self.title)
        self.dialog.redraw()

        return self

    width  = property(lambda self: Screen.screen_size()[0])
    height = property(lambda self: Screen.screen_size()[1])

    def get_assembly_info(self):
        c = DTextEntry(int(self.width/2), "", title="Serial Number (SN)")
        sn = c.result()
        c = DTextEntry(int(self.width/2), "", title="Product ID (SKU/PN)")
        sku = c.result()

        # logger.add(f'{sn}_{sku}_{{time:DD.MM.YYYY}}.txt')
        logger.add(f'{{time:DD.MM.YYYY}}.txt', mode='a')