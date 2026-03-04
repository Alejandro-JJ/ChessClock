"""
Logic of the clock engine
"""
from TimeControls import TIME_CONTROLS
from time import monotonic as tm
from time import sleep


def format_time(t):
    # Put time in MM:SS format
    M = int(t//60)
    S = int(t%60)
    t_fmt = f"{str(M).zfill(2)}:{str(S).zfill(2)}"
    return t_fmt

class Clock:
    def __init__(self, timecontrol):
        # Take properties from timecontrol to initialize
        self.base_sec = timecontrol.base_sec
        self.increment = timecontrol.increment
        self.time_P1 = self.base_sec
        self.time_P2 = self.base_sec
        self.playing = "P1" # can only take values (P1, P2)
        self.last_switch = tm()

    def telltime(self):
        # Read-only function, does not alter internal state
        # It only gives display times, always from the start time
        # Returns a tuple (P1, P2) in a MM:SS format
        elapsed_time = tm() - self.last_switch
         # Compute temporary display values
        if self.playing == "P1":
            display_P1 = self.time_P1 - elapsed_time
            display_P2 = self.time_P2
        elif self.playing == "P2":
            display_P1 = self.time_P1
            display_P2 = self.time_P2 - elapsed_time
        else:
            display_P1 = self.time_P1
            display_P2 = self.time_P2

        # Prevent negative display
        display_P1 = max(0, display_P1)
        display_P2 = max(0, display_P2)

        return (format_time(display_P1), format_time(display_P2))

    def switch(self):
        # Changes internal status
        elapsed_time = tm() - self.last_switch

        # P1 was playing, and button switches to P2
        if self.playing == "P1":
            self.time_P1 = self.time_P1 - elapsed_time + self.increment
            self.playing = "P2"
        # P2 was playing, and button switches to P1
        elif self.playing == "P2":
            self.time_P2 = self.time_P2 - elapsed_time + self.increment
            self.playing = "P1"
        else:
            pass
        # The critical line! This wasa lot of stupid debugging
        self.last_switch = tm()




