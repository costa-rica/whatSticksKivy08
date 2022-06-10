from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


Builder.load_file('parentscreen1/ps1.kv')


class ParentScreen1(Screen):
  email_text = StringProperty()
  password_text = StringProperty()
  email_field = ObjectProperty()
  password_field = ObjectProperty()
  password_flag_text =ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen1 __init__')
    self.bind(size=self.size_widgets)
    self.call_count=0

  def verify_user(self):
    # self.parent.
    self.parent.current="parent_screen_2"

  def size_widgets(self,*args):
    if self.call_count >0:
      self.ps1_base_width=self.width
      self.ps1_base_height=self.height
      print('size_widgets called')
      print('width:',self.ps1_base_width)
      print('height:',self.ps1_base_height)
      print('self.parent:', self.parent)
      print('self.parent.children:', self.parent.children)

#App Name Anchor
      self.anchor_app_name.size_hint=(1,None)
      self.anchor_app_name.height = self.ps1_base_height *.2
      self.label_app_name.size_hint=(None,None)
      self.label_app_name.size = self.label_app_name.texture_size
      self.label_app_name.font_size=self.ps1_base_width*.1
      # print('ps1.label_app_name.height:',self.label_app_name.height)

#Email Anchor
      # print('Before Email Anchor Height:',self.anchor_email.height)
      self.anchor_email.size_hint=(1,None)
      self.anchor_email.height=self.ps1_base_height *.2
      # print('Anchor Email Height (after being set):', self.anchor_email.height)
      self.anchor_email.padding=(self.ps1_base_width * .06,
        0,self.ps1_base_width * .06,0)
      self.md_txt_field_email.font_size=self.ps1_base_width*.06
      # print('ps1.md_txt_field_email.height :',self.md_txt_field_email.height)

#Password Anchor
      self.anchor_password.size_hint=(1,None)
      self.anchor_password.height=self.ps1_base_height * .2
      # print('Anchor Password Height (after being set):', self.anchor_password.height)
      self.anchor_password.padding=(self.ps1_base_width * .06,
        0,self.ps1_base_width * .06,0)
      self.md_txt_field_password.font_size=self.ps1_base_width*.06

#Show Password BoxLayout
      self.box_show_password.size_hint=(1,None)
      self.box_show_password.height=self.ps1_base_height * .1

#Show Password Checkbox
      self.anchor_checkbox_show_password.anchor_x="right"
      self.md_checkbox_show_password.size_hint=(None,None)
      self.md_checkbox_show_password.size=self.md_checkbox_show_password.texture_size

#Show Password Label
      self.anchor_label_show_password.anchor_x="left"
      self.label_show_password.font_size = self.ps1_base_width*.05
      self.label_show_password.size_hint=(None,None)
      self.label_show_password.size=self.label_show_password.texture_size
      self.label_show_password.color=(.3,.3,.3,1)

#Anchor Submit
      self.btn_login.size_hint=(.5,.35)
      self.btn_login.font_size=self.ps1_base_width*.06
      self.btn_login.md_bg_color=(.2,.2,.2,1)
      self.anchor_login.anchor_x="right"
      self.anchor_login.padding=(0,0,self.ps1_base_width * .06,0)

#Anchor Exit
      self.btn_exit.size_hint=(.25,.35)
      self.btn_exit.font_size=self.ps1_base_width*.06
      self.btn_exit.md_bg_color=(.5,.5,.5,1)
      self.anchor_exit.anchor_x="right"
      self.anchor_exit.anchor_y="top"
      self.anchor_exit.padding=(0,0,self.ps1_base_width * .06,0)



    self.call_count+=1


  def get_heights(self):
    for i in self.children:
      print(i, i.height)

  def show_password(self, checkbox, value):
    if value:
      self.label_show_password.text="Hide password"
      self.md_txt_field_password.password=False
    else:
      self.label_show_password.text="Show password"
      self.md_txt_field_password.password = True


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
