import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.audio import SoundLoader, Sound


'''
    Screen
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
        self.bind(on_press=self.clickSound)

    def clickSound(self, *args):
        clickAudio = SoundLoader.load('sounds\click.mp3')
        if clickAudio.state == 'play':
            print("blah")
            clickAudio.stop()
        clickAudio.play()
        clickAudio.seek(0.3538)
        clickAudio.volume = 0.5


kv_des = Builder.load_file('design\horizon_music_des.kv')


class HorizonMusicApp(App):
    def build(self):
        self.title = "Horizon Music" + chr(169)

        Window.size = (1920, 1080)
        Window.fullscreen = True

        return kv_des


if __name__ == "__main__":
    HorizonMusicApp().run()
