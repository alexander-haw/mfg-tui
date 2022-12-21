
from picotui.screen import Screen
from picotui.dialogs import Dialog
from picotui.menu import WMenuBar, WMenuBox

from context import TerminalContext as Term, Action
from defs import Color as C

if __name__ == '__main__':
    
    with Term("Example App", C.BLACK, 2) as win:

        win.add_label(12, 1, "Press F9 for menu")
        win.add_label(1, 2,"Label:")
        win.add_list_box(1, 3, 16, [f"choice{i}" for i in range(3)])
        win.add_drop_down(1, 8, 10, ["Red", "Green", "Yellow"])
        win.add_check_box(11, 8, "Red")
        win.add_check_box(11, 9, "Green")
        win.add_check_box(11, 10, "Yellow")
        win.add_radio_button(12, 20, ["Red", "Green", "Yellow"])

        win.add_button(10, 11, 8, Action.OK)
        win.add_button(23, 11, 8, Action.CANCEL)
        
        global res
        res = win.loop()

print("Result:", res)