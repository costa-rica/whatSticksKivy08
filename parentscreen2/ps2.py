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
    print('toolbar height:::', self.toolbar.height)
    main_box.ps1_base_height=self.parent.ps1_base_height-self.toolbar.height
    main_box.size_hint=(None,None)
    main_box.size=(self.parent.ps1_base_width, self.parent.ps1_base_height-self.toolbar.height)
    extra_box.size_hint=(None,None)
    extra_box.size=(self.parent.ps1_base_width, self.parent.ps1_base_height * .25)


  #set MainBox screen name
    main_box.act_screen_screen_name.padding=(
      main_box.width*.01,main_box.height*.01,0,0)#left,top,right,bottom
    main_box.act_screen_screen_name.add_act_name_label.font_size= act_screen.width*.05
    main_box.act_screen_screen_name.email_label.text="  "+self.parent.email
    main_box.act_screen_screen_name.email_label.font_size=act_screen.width*.03



    #set Activity Screen act name label and input
    main_box.act_name_box.padding=(
      main_box.width*.05,main_box.height*.5,main_box.width*.05,0)
    main_box.act_name_box.add_act_name_label.font_size=main_box.width*.05
    main_box.act_name_box.add_act_name.font_size=main_box.width*.03




# class MainBoxLayout(BoxLayout):
#
#   def __init__(self,**kwargs):
#     super().__init__(**kwargs)
#     print('MainBoxLayout __init__')
#     self.size_changed_count=0

  # def on_kv_post(self,*args):#Too early to be useful
  #   print('MainBoxLayout on_kv_post')



  # def size_changed(self,*args):
  #   print('***MainBoxLayout size_change: ', self.size_changed_count)
  #   # print('MDNavigationLayout:',self.parent.parent.parent.parent)
  #   # print('ParentScreen2:',self.parent.parent.parent.parent.parent)
  #   ps2=self.parent.parent.parent.parent.parent
  #   self.ps1_base_width=ps2.ps1_base_width
  #   self.ps1_base_height= ps2.ps1_base_height
  #   print('ps2.ps1_base_height:::', ps2.ps1_base_height)
  #
  #   self.size_changed_count+=1


  # def on_enter(self):#Does nothing
  #   print('MainBoxLayout on_enter')



class ExtraBoxLayout(BoxLayout):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainBoxLayout __init__')
