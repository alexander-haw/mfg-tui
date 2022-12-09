from picotui.widgets import *
from picotui.defs import *
from picotui.dialogs import *

from tui_context import Wcontext

with Wcontext("Gauge Calibration") as term:
    term.get_assembly_info()

with Wcontext("Gauge Calibration") as term:
    term.form_label("Enter the gauge readings shown on the unit's insturment panel.")
    term.form_newline()

    term.form_input("Altimeter     ", r"\d{1,4}.\d{2}")
    term.form_input("Heading       ", r"\d{1,3}\w")
    term.form_input("Airspeed      ", r"\d{1,4}.\d{2}")
    term.form_input("Attitude      ", r"\d+")
    term.form_input("Vertical Speed", r"\d+\w{3}")

    term.form_newline()
    term.form_label("Press 'OK' when all readings have been entered.")
    term.form_label("End the program at any time by pressing 'CANCEL'.")
    
    term.form_ok_cancel()
    term.dialog.loop()

with Wcontext("Gauge Calibration: Altimiter [1/5]") as term:
    term.form_label("Use the arrows to adjust the panel reading until it matches the value shown.")
    term.form_newline()
    term.form_newline()
    term.form_inc_dec("0.00")

    term.form_newline()
    term.form_ok_cancel()
    term.dialog.loop()
with Wcontext("Gauge Calibration: Heading [2/5]") as term:
    term.form_label("Use the arrows to adjust the panel reading until it matches the value shown.")
    term.form_newline()
    term.form_newline()
    term.form_inc_dec("270")

    term.form_newline()
    term.form_ok_cancel()
    term.dialog.loop()
with Wcontext("Gauge Calibration: Airspeed [3/5]") as term:
    term.form_label("Use the arrows to adjust the panel reading until it matches the value shown.")
    term.form_newline()
    term.form_newline()
    term.form_inc_dec("0.00")

    term.form_newline()
    term.form_ok_cancel()
    term.dialog.loop()
with Wcontext("Gauge Calibration: Attitude [4/5]") as term:
    term.form_label("Use the arrows to adjust the panel reading until it matches the value shown.")
    term.form_newline()
    term.form_newline()
    term.form_inc_dec("0")

    term.form_newline()
    term.form_ok_cancel()
    term.dialog.loop()
with Wcontext("Gauge Calibration: Vertical Speed [5/5]") as term:
    term.form_label("Use the arrows to adjust the panel reading until it matches the value shown.")
    term.form_newline()
    term.form_newline()
    term.form_inc_dec("00.00")

    term.form_newline()
    term.form_ok_cancel()
    term.dialog.loop()

with Wcontext("Gauge Calibration") as term:
    term.form_label("Calibration complete.")
    term.form_ok()
    term.dialog.loop()