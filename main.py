from kivymd.app import MDApp
from kivy.core.window import Window
from myscreencontroller import MyScreenController
import os;import platform

if platform in ['ios','android']:
  print('kivy.utils.platform:::', platform)
else:
  # Window.size = (640, 1136)#iphone demensions
  Window.size = (960, 1704)#iphone mini

class MainApp(MDApp):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainApp __init__')
    self.mycontroller=MyScreenController()

  def build(self):
    print("MainApp build")
    return self.mycontroller.get_screen()
    # return Builder.load_file('main_design.kv')

if __name__ == '__main__':
  MainApp().run()
