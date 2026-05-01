class TVState:
    def __init__(self):
        self.power = "OFF"
        self.current_module = "Live TV"
        self.volume = 10


class IPadState:
    def __init__(self):
        self.connected = True
        self.now_playing = "Live TV"
