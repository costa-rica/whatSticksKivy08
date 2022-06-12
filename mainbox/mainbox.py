from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from utils import add_activity_util
from kivy.uix.popup import Popup
from utils import current_time_util

Builder.load_file('mainbox/mainbox.kv')


class MainBoxLayout(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  toolbar_height=ObjectProperty(0)
  # date_str=StringProperty()
  # text_size_coef=ObjectProperty(.06)
  # text_size_coef_sm=ObjectProperty(.04)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainBoxLayout __init__')

  def on_enter(self):#Never shows up
    print('MainBox on_enter**** Never Shows up right???????')

  def submit_btn(self):
    print('we just submitted some key life changing information.')
    print('self.parent.parent:', self.parent.parent.parent.parent.parent.parent.parent)
    base_screen = self.parent.parent.parent.parent.parent.parent.parent
    print('base_screen.login_token:',base_screen.login_token)
    try:
      # num=int("String")#Create ValueError
      add_activity_util(
        self.act_name_box.add_act_name.text, #title of activity
        self.act_note_box.add_act_note.txt_input_dy_act_note.text, #not of activity
        base_screen.id,
        base_screen.user_timezone,
        self.box_sub_date_time.date_input.text,
        self.box_sub_date_time.time_input.text,
        base_screen.email,
        base_screen.login_token)

      custom_popup = CustomPopup(
        title="Activity Succesfully Added",
        title_color=(127/255,160/255,189/255),
        separator_color=(127/255,160/255,189/255),
        title_size=self.width*.03
        )
      custom_popup.bind(on_dismiss=self.clear_screen)
      custom_popup.open()

    except ValueError:

      custom_popup = CustomPopup(
        title="Activity NOT Added",
        title_color=(250/255,160/255,127/255),
        separator_color=(250/255,160/255,127/255),
        title_size=self.width*.03
        )
      custom_popup.bind(on_dismiss=self.clear_screen)
      custom_popup.open()

  def clear_screen(self,*args):
    print('clear_screen')
    base_screen = self.parent.parent.parent.parent.parent.parent.parent
    self.act_name_box.add_act_name.text=''
    self.act_note_box.add_act_note.txt_input_dy_act_note.text=''
    self.box_sub_date_time.date_input.text,self.box_sub_date_time.time_input.text=current_time_util(base_screen.user_timezone)

class CustomPopup(Popup):...


class BoxLayoutDateAndTime(BoxLayout):
  date_str=StringProperty()
  time_str=StringProperty()
  # def on_kv_post(self):
  #   print('self.parent:')


class AnchorLayoutScreenName(AnchorLayout):
  email=StringProperty('')
  def __init__(self,**kwargs):
    super().__init__(**kwargs)


class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddName***')
    main_box =instance.parent.parent#different hiearchey than TextInputDynamicActNote
    if value:
      main_box.act_name_box.add_act_name_label.color=(0,0,0,1)
    else:
      main_box.act_name_box.add_act_name_label.color=(.3,.3,.3,1)


class TextInputDynamicActNote(TextInput):
  def on_focus(instance, instance_twice, value):
    print('TextInputDynamicActNote on_focus')
    main_box=instance.parent.parent.parent.parent.parent
    if value:
      main_box.act_note_box.add_act_note_label.color=(0,0,0,1)
    else:
      main_box.act_note_box.add_act_note_label.color=(.3,.3,.3,1)


class TextInputAddDate(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddDate***')
    box_date =instance.parent.parent#different hiearchey than TextInputDynamicActNote
    print('main_box:', box_date)
    print('main_box.children:', box_date.children)
    if value:
      box_date.date_label.color=(0,0,0,1)
    else:
      box_date.date_label.color=(.3,.3,.3,1)


class TextInputAddTime(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddDate***')
    box_date =instance.parent.parent#different hiearchey than TextInputDynamicActNote
    print('main_box:', box_date)
    print('main_box.children:', box_date.children)
    if value:
      box_date.time_label.color=(0,0,0,1)
    else:
      box_date.time_label.color=(.3,.3,.3,1)
