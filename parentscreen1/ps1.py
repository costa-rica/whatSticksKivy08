from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton

import requests
import json


Builder.load_file('parentscreen1/ps1.kv')


class ParentScreen1(Screen):
  # email_text = StringProperty()
  # # password_text = StringProperty()
  # email_field = ObjectProperty()
  # password_field = ObjectProperty()
  # password_flag_text =ObjectProperty()
  md_txt_field_email=ObjectProperty()
  md_txt_field_password=ObjectProperty()
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)

  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen1 __init__')
    self.bind(size=self.size_widgets)
    self.call_count=0

  def size_widgets(self,*args):
    if self.call_count >0:
      self.ps1_base_width=self.width
      self.ps1_base_height=self.height
      print('size_widgets called')
      print('self.ps1_base_width:',self.ps1_base_width)
      print('self.ps1_base_height:',self.ps1_base_height)
      self.md_txt_field_email.text='nickapeed@yahoo.com'
      self.md_txt_field_password.text='test'
    self.call_count+=1


  def verify_user(self):
    base_url = 'https://api.what-sticks-health.com'
    response_login = requests.request('GET',base_url + '/login',
        auth=(self.md_txt_field_email.text,self.md_txt_field_password.text))
    print('response_login.status_code:::', response_login.status_code)
    if response_login.status_code ==200:
      login_token = json.loads(response_login.content.decode('utf-8'))['token']

      url_user_data = base_url + "/user_account_data"
      headers = {'x-access-token': login_token,'Content-Type': 'application/json'}
      response_user_data = requests.request("GET", url_user_data, headers=headers)
      user_data_dict = json.loads(response_user_data.text)

      self.parent.ps1_base_width=self.ps1_base_width
      self.parent.ps1_base_height=self.ps1_base_height

      self.parent.email = self.md_txt_field_email.text
      self.parent.login_token = login_token
      self.parent.id = user_data_dict['id']
      self.parent.username=user_data_dict['username']
      self.parent.user_timezone = user_data_dict['user_timezone']


    self.parent.current="parent_screen_2"




  def show_password(self,toggle_widget):
    print('toggle_widget:', toggle_widget.state)
    if toggle_widget.state=='down':
      self.show_password_toggle.text="Hide password"
      self.md_txt_field_password.password=False
    else:
      self.show_password_toggle.text="Show password"
      self.md_txt_field_password.password = True



class ShowPasswordToggle(MDFillRoundFlatButton, MDToggleButton):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.background_down = self.theme_cls.primary_light

# class CanvasWidget(Widget):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         with self.canvas:
#             Color(127/255,160/255,189/255,1)
#             self.rect=Rectangle(pos=self.pos,size=self.size)
#             self.bind(pos=self.update_rect,
#                           size=self.update_rect)
#     def update_rect(self, *args):
#         self.rect.pos = self.pos
#         self.rect.size = self.size
