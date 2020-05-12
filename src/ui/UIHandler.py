from kivy.app import App
from kivy.lang import Builder

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from src.music_utils.PlayQueue import PlayQueue
from src.music_utils.PlaylistHandler import PlaylistHandler
from src.music_utils.Song import Song
from src.utils.StableBoolean import StableBoolean
from src.utils.Constants import GUIFiles

'''
    Screens
'''


class WindowManager(ScreenManager):
    pass


class Intro(Screen):
    pass


class MenuScreen(Screen):
    pass


class InfoScreen(Screen):
    pass


class MyLibsScreen(Screen):
    pass


class MySongsScreen(Screen):
    pass


class AllSongsScreen(Screen):
    pass


'''
    Widgets & Utils
'''


class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.r = 0

        self.is_mouse_over = StableBoolean(false_threshold=3)
        Window.bind(mouse_pos=self.mouse_over_ani)
        self.bind(on_press=self.on_press)

    def mouse_over_ani(self, src, mouse_pos):
        self.r = self.size[0] / 2

        x, y = self.pos
        x = x + self.r
        y = y + self.r

        m_x, m_y = mouse_pos

        y_ready = abs(m_y - y) <= self.r
        x_ready = abs(m_x - x) <= self.r

        self.is_mouse_over.update(x_ready and y_ready)

        if self.state == 'down':
            pass

        elif self.is_mouse_over.out_val and self.state == 'normal':
            self.opacity = 0.5

        else:
            self.opacity = 1

    def on_press(self, *args):
        self.opacity = 0.3


class TransTextInput(TextInput):
    def __init__(self, **kwargs):
        super(TransTextInput, self).__init__(**kwargs)


class SearchInput(TransTextInput):
    def __init__(self, **kwargs):
        super(TransTextInput, self).__init__(**kwargs)
        self.coulor = (1, 0, 0, 1)
        self.search = ''
        self.playlist = PlaylistHandler().all_music
        self.easter_time = str(chr(111) + chr(102) + chr(101) + chr(107) + chr(32) + chr(114) + chr(108) +
                               chr(32) + chr(116) + chr(104) + chr(101) + chr(32)
                               + chr(107) + chr(105) + chr(110) + chr(103))
        
    def get_search(self):
        self.search = self.text.replace(' ', '').casefold()

        self.act_on_valid(self.validate())

    def validate(self):
        if self.search == self.easter_time.replace(' ', '').casefold():
            return self.easter_time

        for song in self.playlist.songs:
            song_name = song.song_name.replace(' ', '').casefold()
            if song_name in self.search:
                return "True"

        return "False"

    def act_on_valid(self, is_valid):
        if is_valid == "False":
            self.text = "Can't find this search!"
        elif is_valid == self.easter_time:
            self.text = str(chr(84) + chr(114) + chr(117) + chr(101) + chr(33))


class VolumeUp(ImageButton):
    def __init__(self, **kwargs):
        super(VolumeUp, self).__init__(**kwargs)
        self.bind(on_press=self.act)
        self.session = AudioUtilities.GetAllSessions()
        self.volume = self.session._ctl.QueryInterface(ISimpleAudioVolume)

    def act(self):
        self.volume.SetMasterVolume(self.volume.GetMasterVolume() + 1, None)


class VolumeDown(ImageButton):
    def __init__(self, **kwargs):
        super(VolumeDown, self).__init__(**kwargs)
        self.bind(on_press=self.act)
        self.session = AudioUtilities.GetAllSessions()
        self.volume = self.session._ctl.QueryInterface(ISimpleAudioVolume)

    def act(self):
        self.volume.SetMasterVolume(self.volume.GetMasterVolume() - 1, None)


song_queue = PlayQueue()


class PlayPause(ImageButton):
    def __init__(self, **kwargs):
        super(PlayPause, self).__init__(**kwargs)
        self.bind(on_press=song_queue.current.toggle_state())


class NextSong(ImageButton):
    def __init__(self, **kwargs):
        super(NextSong, self).__init__(**kwargs)
        self.bind(on_press=song_queue.skip())


class PrevSong(ImageButton):
    def __init__(self, **kwargs):
        super(PrevSong, self).__init__(**kwargs)
        self.bind(on_press=song_queue.back())


class SongWidget(Widget):
    def __init__(self, **kwargs):
        super(SongWidget, self).__init__(**kwargs)
        self.song_obj = Song(r'')
        self.widget_title = "{} | {}".format(self.song_obj.artist, self.song_obj.song_name)


'''
    App
'''


class HorizonMusicApp(App):
    def __init__(self, logger, **kwargs):
        super(HorizonMusicApp, self).__init__(**kwargs)
        self.gui_files = GUIFiles(logger)  # load the gui files
        self.kv_des = Builder.load_file(self.gui_files.KV_DES_FILE)
        self.click_audio = SoundLoader.load(self.gui_files.CLICK_SOUND)

    def click_sound(self, *args):
        if self.click_audio.state == 'play':
            self.click_audio.stop()

        self.click_audio.play()
        self.click_audio.volume = 0.2
        self.click_audio.seek(0.3133)

    def build(self):
        self.title = "Horizon Music" + chr(169)

        Window.size = (1920, 1080)
        Window.fullscreen = False

        return self.kv_des
