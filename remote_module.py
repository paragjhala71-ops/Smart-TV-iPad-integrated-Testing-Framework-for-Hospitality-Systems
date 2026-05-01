class RemoteControl:
    def __init__(self, tv):
        self.tv = tv

    def power_on(self):
        self.tv.power = "ON"
        print("TV Powered ON")

    def power_off(self):
        self.tv.power = "OFF"
        print("TV Powered OFF")

    def switch_module(self, module_name):
        if self.tv.power == "ON":
            self.tv.current_module = module_name
            print(f"Switched TV to {module_name}")
        else:
            print("Cannot switch module. TV is OFF")

    def volume_up(self):
        if self.tv.power == "ON":
            self.tv.volume += 1
            print("Volume Increased")
        else:
            print("TV is OFF")
