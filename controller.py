import keyboard


class FishingController:

    def __init__(self):
        self.isRunning = False

        keyboard.add_hotkey("f8", self.toggle)
    def start(self):
        if self.isRunning:
            return

        self.isRunning = True
        print("[INFO] Fishing started")

    def stop(self):
        if not self.isRunning:
            return

        self.isRunning = False
        print("[INFO] Fishing stopped")

    def toggle(self):
        if self.isRunning:
            self.stop()
        else:
            self.start()

    def cleanup(self):
        keyboard.unhook_all()
