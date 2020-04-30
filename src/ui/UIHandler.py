import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput

from src.utils.StableBoolean import StableBoolean


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

        self.py_size = (0,0)
        self.py_pos = (0,0)

        self.r = 0

        self.is_mouse_over = StableBoolean(false_threshold=3)
        Window.bind(mouse_pos=self.mouse_over_ani)

    def mouse_over_ani(self, src, mouse_pos):
        self.r = self.py_size[0] / 2

        x, y = self.py_pos
        x = x + self.r
        y = y + self.r

        m_x, m_y = mouse_pos

        y_ready = abs(m_y - y) <= self.r
        x_ready = abs(m_x - x) <= self.r

        self.is_mouse_over.update(x_ready and y_ready)

        if self.state == 'down':
            self.opacity = 0.1114

        elif self.is_mouse_over.out_val and self.state == 'normal':
            self.opacity = 0.5554

        else:
            self.opacity = 1


class TransTextInput(TextInput):
    def __init__(self, **kwargs):
        super(TransTextInput, self).__init__(**kwargs)
    pass


'''
    GUI Design
'''
kv_des = Builder.load_file('design\horizon_music_des.kv')


class HorizonMusicApp(App):
    def __init__(self, **kwargs):
        super(HorizonMusicApp, self).__init__(**kwargs)
        self.click_audio = SoundLoader.load('sounds\click.mp3')

    def click_sound(self, *args):
        if self.click_audio.state == 'play':
            self.click_audio.stop()

        self.click_audio.play()
        self.click_audio.volume = 0.3
        self.click_audio.seek(0.3133)

    def build(self):
        self.title = "Horizon Music" + chr(169)

        Window.size = (1920, 1080)
        Window.fullscreen = False

        return kv_des


if __name__ == "__main__":
    HorizonMusicApp().run()
