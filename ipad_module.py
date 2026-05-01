class IPadController:
    def __init__(self, tv, ipad):
        self.tv = tv
        self.ipad = ipad

    def sync_with_tv(self):
        self.ipad.now_playing = self.tv.current_module
        print("iPad Synced With TV")
