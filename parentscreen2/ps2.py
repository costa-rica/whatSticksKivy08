from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
#custom
# import utils
# from utils import CanvasWidget, current_time_util
#python
# import json
# import requests
# import activityscreen.act_screen
import mainbox.mainbox

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...
class Toolbar(MDToolbar):...

class ParentScreen2(Screen):
  # email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  canvas_widget=ObjectProperty()
  md_nav_layout=ObjectProperty()
  toolbar=ObjectProperty(None)
  child_sm=ObjectProperty(None)
  act_screen_id=ObjectProperty(None)
  def __init__(self,**kwargs):
    super(ParentScreen2,self).__init__(**kwargs)
    print('ParentScreen2 __init__')
    print('self.parent:', self.parent)#None


  def on_enter(self):
    print('ParentScreen2 on_enter')
    print('self.parent:', self.parent)#BaseScreenManager
    print('self.parent.ps1_base_width', self.parent.ps1_base_width)#800

    act_screen = self.children[0].children[1].children[0]
    main_box = act_screen.children[0].children[0].children[1]
    extra_box = act_screen.children[0].children[0].children[0]

  #Assign MainBox and ExtraBox dimensions AND pass ps1_base dimensions
    main_box.ps1_base_width=self.parent.ps1_base_width
    main_box.ps1_base_height=self.parent.ps1_base_height-self.toolbar.height
    print('toolbar height:::', self.toolbar.height)
    main_box.toolbar_height=self.toolbar.height

    extra_box.ps1_base_width=self.parent.ps1_base_width
    extra_box.ps1_base_height=self.parent.ps1_base_height
    extra_box.toolbar_height=self.toolbar.height

  #set MainBox screen name
    main_box.act_screen_screen_name.email=self.parent.email









class ExtraBoxLayout(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  toolbar_height=ObjectProperty(0)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainBoxLayout __init__')
