from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
import os
import parentscreen1.ps1
import parentscreen2.ps2

Builder.load_file('base.kv')

class BaseScreenManager(ScreenManager):
  controller = ObjectProperty()
  # email=StringProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('BaseScreenManager __init__')
    # self.ps1_base_width=1
    # self.ps1_base_height=1
  #   self.bind(size=self.on_size)
  #
  # def on_size(self, *args):
  #   self.controller.base_scrn_manager_size(self)
