class Validator:
    def __init__(self, tv, ipad):
        self.tv = tv
        self.ipad = ipad

    def validate_sync(self):
        if self.tv.current_module == self.ipad.now_playing:
            return "PASS"
        return "FAIL"
