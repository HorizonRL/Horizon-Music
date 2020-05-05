import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput

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
            self.opacity = 0.75

    def on_press(self, *args):
        self.opacity = 1


class TransTextInput(TextInput):
    def __init__(self, **kwargs):
        super(TransTextInput, self).__init__(**kwargs)
    pass


class HorizonMusicApp(App):
    def __init__(self, **kwargs):
        super(HorizonMusicApp, self).__init__(**kwargs)
        self.gui_files = GUIFiles()  # load the gui files
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
        Window.fullscreen = True

        return self.kv_des
