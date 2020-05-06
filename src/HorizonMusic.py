from src.ui.UIHandler import HorizonMusicApp
from src.utils.Logger import Logger


class HorizonMusic:
    def __init__(self):
        self.logger = Logger(log_name="MyLog")
        self.app = HorizonMusicApp(self.logger)


if __name__ == "__main__":
    horizon_music = HorizonMusic()
    horizon_music.app.run()