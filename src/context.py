from typing import ForwardRef, List

from picotui.context import Context
from picotui.screen import Screen
from picotui.dialogs import Dialog
from loguru import logger

from defs import Color as C, Action
from picotui import widgets

from widgets import WCheckbox, WButton, WDropDown, WRadioButton, WListBox

class TerminalDialog(Dialog):

    def add(self, x: int, y: int, widget: widgets.Widget) -> widgets.Widget:
        super().add(x, y, W := widget)
        return W

    def add_button(self, x: int, y: int, w: int, text: str | Action) \
    -> WButton:
        finish_dialog = None
        if isinstance(text, Action):
            finish_dialog = text
            text = text._name_
        W: widgets.WButton = self.add(x, y, WButton(w, text))
        if finish_dialog:
            W.finish_dialog = finish_dialog
        return W
    def add_check_box(self,    x: int, y: int, title: str, choice: bool = False)\
    -> WCheckbox:    return self.add(       x,      y, WCheckbox(title, choice))
    def add_frame(self,        x: int, y: int, w: int, h: int, title: str)\
    -> widgets.WFrame:       return self.add(       x,      y, widgets.WFrame(w, h, title))
    def add_multi_entry(self,  x: int, y: int, w: int, h: int, text: str)\
    -> widgets.WMultiEntry:  return self.add(       x,      y, widgets.WMultiEntry(w, h, text))
    def add_label(self,        x: int, y: int, text: str)\
    -> widgets.WLabel:       return self.add(       x,      y, widgets.WLabel(text, len(text)))
    def add_text_entry(self,   x: int, y: int, w: int, text: str)\
    -> widgets.WTextEntry:   return self.add(       x,      y, widgets.WTextEntry(w, text))
    def add_combo_box(self,    x: int, y: int, w: int, text: str, items: List[str])\
    -> widgets.WComboBox:    return self.add(       x,      y, widgets.WComboBox(w, text, items))
    def add_drop_down(self,    x: int, y: int, w: int, items: List[str])\
    -> WDropDown:    return self.add(       x,      y, WDropDown(w, items))
    def add_list_box(self,     x: int, y: int, w: int, items: List[str])\
    -> WListBox:     return self.add(       x,      y, WListBox(w, len(items), items))
    def add_radio_button(self, x: int, y: int, items: List[str])\
    -> WRadioButton: return self.add(       x,      y, WRadioButton(items))

class TerminalContext(Context):

    def __init__(self, title: str, color: C, margin: int):
        
        super().__init__(True, True)
        self.title, self.color, self.margin = title, color, margin
        
        logger.remove()

    __exit__ = ForwardRef('__exit__')

    @logger.catch(onerror=__exit__, default=Action.NONE)
    def __enter__(self)\
        -> TerminalDialog:

        logger.add(f"{{time:DD.MM.YYYY}}.txt", mode='a')

        super().__enter__()
        Screen.attr_color(C.WHITE, self.color)
        Screen.cls()
        Screen.attr_reset()
        
        self.dialog = TerminalDialog(
            self.margin, self.margin,
            self.width, self.height,
            self.title
        )
        self.dialog.redraw()

        return self.dialog
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        Screen.cls()
        Screen.attr_reset()
        self.dialog.deinit_tty()
        
        return super().__exit__(exc_type, exc_val, exc_tb)

    width:  int = property(lambda self:
        Screen.screen_size()[0] - self.margin*2)
    height: int = property(lambda self:
        Screen.screen_size()[1] - self.margin*2)
    