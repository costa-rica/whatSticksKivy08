from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
import os
import parentscreen1.ps1
import parentscreen2.ps2

Builder.load_file('base.kv')

class BaseScreenManager(ScreenManager):
  controller = ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('BaseScreenManager __init__')
