from pathlib import Path
import os


class GUIFiles:
    def __init__(self, logger):
        self.logger = logger

        self.GUI_PATH = str(Path.cwd() / 'ui')

        self.KV_DES_FILE = os.path.join(self.GUI_PATH, r'design\horizon_music_des.kv')
        self.CLICK_SOUND = os.path.join(self.GUI_PATH, r'sounds\click.mp3')
        self.ERROR_SOUND = os.path.join(self.GUI_PATH, r'sounds\error.mp3')
        self.BACKGROUND = os.path.join(self.GUI_PATH, r'images\screens\BackG.png')
        self.INFO_SCREEN = os.path.join(self.GUI_PATH, r'images\screens\info.png')
        self.BACKWARD_WINDOW_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\Backw.png')
        self.CONTINUE_WINDOW_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\cont.png')
        self.BACK_TO_MENU_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\BtoM.png')
        self.INFO_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\Info.png')
        self.ALL_MUSIC_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\Music.png')
        self.FOLDER_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\Folder.png')
        self.PLAYLIST_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\Playlist.png')
        self.QUIT_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\Quit.png')
        self.SEARCH_BAR_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\SearchBar.png')
        self.SEARCH_WIDGET = os.path.join(self.GUI_PATH, r'images\widgets\SearchIcon.png')
        self.SONG_BACK = os.path.join(self.GUI_PATH, r'images\screens\SongBack.png')
        self.MEDIA_PLAYER_PLAY_PAUSE = os.path.join(self.GUI_PATH, r'images\widgets\PlayPause.png')
        self.MEDIA_PLAYER_PREV = os.path.join(self.GUI_PATH, r'images\widgets\prev.png')
        self.MEDIA_PLAYER_NEXT = os.path.join(self.GUI_PATH, r'images\widgets\next.png')
        self.MEDIA_PLAYER_BACK = os.path.join(self.GUI_PATH, r'images\screens\MediaPlayerBack.png')

        self.INTRO = os.path.join(self.GUI_PATH, r'videos\Intro.avi')

        self.files = [self.KV_DES_FILE, self.CLICK_SOUND, self.BACKGROUND, self.INFO_SCREEN,
                      self.BACKWARD_WINDOW_WIDGET, self.BACKWARD_WINDOW_WIDGET, self.BACK_TO_MENU_WIDGET,
                      self.INFO_WIDGET, self.ALL_MUSIC_WIDGET, self.FOLDER_WIDGET, self.PLAYLIST_WIDGET,
                      self.QUIT_WIDGET, self.SEARCH_BAR_WIDGET, self.SEARCH_WIDGET, self.INTRO, self.MEDIA_PLAYER_BACK,
                      self.SONG_BACK, self.MEDIA_PLAYER_NEXT, self.MEDIA_PLAYER_PLAY_PAUSE, self.MEDIA_PLAYER_PREV]

        self.is_load = True
        for file in self.files:
            f = None
            try:
                f = open(file)

            except FileNotFoundError:
                self.is_load = False
                self.logger.write("ERROR! Can't load file or file is corrupted: {}".format(file))

            f.close()

        if self.is_load:
            self.logger.write("Loaded all GUI files successfully!")


class Network:
    PORT = 1690
    SERVER_IP = '127.0.0.1'  # '192.168.1.16' -> not local
