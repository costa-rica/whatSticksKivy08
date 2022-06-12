from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

import mainbox.mainbox

from utils import current_time_util

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...
class Toolbar(MDToolbar):...


class ParentScreen2(Screen):
  toolbar=ObjectProperty(None)

  def __init__(self,**kwargs):
    super(ParentScreen2,self).__init__(**kwargs)
    print('ParentScreen2 __init__')
    # print('self.parent:', self.parent)#None
    self.bind(size=self.on_size)
    self.on_size_count=0

  def on_size(self,*args):
    print('ParentScreen2 on_size:', self.on_size_count)
    self.size_hint=None,None
    self.size=(self.parent.ps1_base_width,self.parent.ps1_base_height)
    self.on_size_count+=1


  def on_enter(self):
    print('ParentScreen2 on_enter')

  #Assign obj vars
    act_screen = self.children[0].children[1].children[0]
    main_box = act_screen.children[0].children[0].children[1]
    extra_box = act_screen.children[0].children[0].children[0]
    date_time_box = main_box.children[1].children[0]


  #Assign MainBox and ExtraBox dimensions AND pass ps1_base dimensions
    main_box.ps1_base_width=self.parent.ps1_base_width
    main_box.ps1_base_height=self.parent.ps1_base_height-self.toolbar.height
    print('toolbar height:::', self.toolbar.height)
    main_box.toolbar_height=self.toolbar.height
    # main_box.login_token=self.parent.login_token

    extra_box.ps1_base_width=self.parent.ps1_base_width
    extra_box.ps1_base_height=self.parent.ps1_base_height
    extra_box.toolbar_height=self.toolbar.height

  #set MainBox screen name
    main_box.act_screen_screen_name.email=self.parent.email

  #date time box assignments (inside MainBox)
    date_time_box.date_str, date_time_box.time_str=current_time_util(self.parent.user_timezone)


class ExtraBoxLayout(BoxLayout):
  # ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  # toolbar_height=ObjectProperty(0)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainBoxLayout __init__')
