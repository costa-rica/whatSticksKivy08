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
import datetime
from pytz import timezone

Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...
class Toolbar(MDToolbar):...


def current_time_util(user_timezone):
    date_time_obj=datetime.datetime.now()
    print('user_timezone:', user_timezone)
    print('date_time_obj:', date_time_obj)
    # user_timezone=MDApp.get_running_app().myscreen.user_timezone
    date_time_obj_tz_aware=timezone(user_timezone).localize(date_time_obj)
    hour_temp=date_time_obj_tz_aware.strftime("%H")
    hour=hour_temp if hour_temp[0]!='0' else hour_temp[1]

    am_pm='AM' if int(hour)<12 else 'PM'

    hour=hour if int(hour)<13 else str(int(hour)-12)
    minute=date_time_obj_tz_aware.strftime("%M")
    # time_thing=date_time_obj_tz_aware.strftime("%H:%M%p")
    time_thing=f'{hour}:{minute} {am_pm}'
    date_thing=date_time_obj_tz_aware.strftime("%m/%d/%Y")

    date_time_now=(date_thing,time_thing)

    return(date_time_now)


class ParentScreen2(Screen):
  # email=StringProperty('')
  # username=StringProperty()
  # user_timezone=StringProperty()
  # canvas_widget=ObjectProperty()
  # md_nav_layout=ObjectProperty()
  toolbar=ObjectProperty(None)
  # child_sm=ObjectProperty(None)
  # act_screen_id=ObjectProperty(None)
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
    # print('ParentScreen2 width:', self.width)
    # print('ParentScreen2 hight:', self.height)
    # print('self.parent:', self.parent)#BaseScreenManager
    # print('self.parent.ps1_base_width', self.parent.ps1_base_width)#800

    act_screen = self.children[0].children[1].children[0]
    main_box = act_screen.children[0].children[0].children[1]
    extra_box = act_screen.children[0].children[0].children[0]
    date_time_box = main_box.children[1].children[0]
  #Get user date from BaseScreenManager
    print('self.user_timezone:', self.parent.user_timezone)
    print('BoxLayoutDateAndTime:', main_box.children[1].children[0])
    date_time_box.date_str, date_time_box.time_str=current_time_util(self.parent.user_timezone)


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
