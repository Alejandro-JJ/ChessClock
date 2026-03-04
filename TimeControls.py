class TimeControl:
    """
    Creates each of the game modes with its attributes.
    Can be modified later.
    """
    def __init__(self, label: str, base_min: int, increment: int):
        self.label = label
        self.base_min = base_min
        self.base_sec = self.base_min*60
        self.increment = increment

TIME_CONTROLS = [
    TimeControl(label="1 + 1", base_min=1, increment=1), # for debugging
    TimeControl(label="5 + 0", base_min=5, increment=0),
    TimeControl(label="5 + 1", base_min=5, increment=1),
    TimeControl(label="10 + 0", base_min=10, increment=0),
    TimeControl(label="10 + 3", base_min=10, increment=3),
    ]

