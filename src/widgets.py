from picotui import widgets

from defs import Color as C, Action, Key

class WButton(widgets.WButton):
    def redraw(self):
        self.goto(self.x, self.y)
        self.attr_color(*(
            (C.WHITE,   C.GRAY) if self.disabled else
            (C.WHITE.B, C.WHITE) if self.focus else
            (C.BLACK,   C.WHITE)))
        self.wr(self.t.center(self.w))
        self.attr_reset()

class WCheckbox(widgets.WCheckbox):
    def redraw(self):
        self.goto(self.x, self.y)
        if self.focus:
            self.attr_color(C.WHITE.B, None)
        self.wr(b"\xe2\x96\xa3" if self.choice else b"\xe2\x96\xa1")
        self.wr(self.t)
        self.attr_reset()

class WRadioButton(widgets.WRadioButton):
    def redraw(self):
        if self.focus:
            self.attr_color(C.WHITE.B, None)
        for i, t in enumerate(self.items):
            self.goto(self.x, self.y + i)
            self.wr(b"\xe2\x97\x89" if self.choice == i else b"\xe2\x97\x8b")
            self.wr(f" {t}")
        self.attr_reset()

class WListBox(widgets.WListBox):
    def show_line(self, l, i):
        hlite = self.cur_line == i
        if hlite:
            self.attr_color(*(
                (C.WHITE.B, C.WHITE) if self.focus else
                (C.BLACK,   C.WHITE)))
        if i != -1:
            l = self.render_line(l)[:self.width]
            self.wr(l)
        self.clear_num_pos(self.width - len(l))
        if hlite:
            self.attr_reset()

class WPopupList(widgets.WPopupList):

    class OneShotList(WListBox):

        def handle_key(self, key):
            if key == Key.ENTER:
                return Action.OK
            if key == Key.ESC:
                return Action.CANCEL
            return super().handle_key(key)

        def handle_mouse(self, x, y):
            if super().handle_mouse(x, y) == True:
                # (Processed) mouse click finishes selection
                return Action.OK

    def __init__(self, x, y, w, h, items, sel_item=0):
        super().__init__(x, y, w, h, items)
        self.list = self.OneShotList(w - 2, h - 2, items)
        self.list.cur_line = sel_item
        self.add(1, 1, self.list)

    def handle_mouse(self, x, y):
        if not self.inside(x, y):
            return Action.CANCEL
        return super().handle_mouse(x, y)

    def get_choice(self):
        return self.list.cur_line

    def get_selected_value(self):
        if not self.list.content:
            return None
        return self.list.content[self.list.cur_line]

class WDropDown(widgets.WDropDown):
    def redraw(self):
        self.goto(self.x, self.y)
        self.attr_color(*(
            (C.WHITE.B, C.WHITE) if self.focus else
            (C.BLACK,   C.WHITE)))
        self.wr_fixedw(self.items[self.choice], self.w - 1)
        self.attr_reset()
        self.wr(b"\xe2\x96\xbc")

    def handle_mouse(self, x, y):
        popup = WPopupList(self.x, self.y + 1, self.w, self.dropdown_h, self.items, self.choice)
        res = popup.loop()
        if res == Action.OK:
            self.choice = popup.get_choice()
            self.signal("changed")
        self.owner.redraw()