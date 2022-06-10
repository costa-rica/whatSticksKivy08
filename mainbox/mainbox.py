from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Builder.load_file('mainbox/mainbox.kv')

class MainBoxLayout(BoxLayout):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainBoxLayout __init__')

  def on_enter(self):
    print('MainBox on_enter****')



class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddName***')
    main_box =instance.parent.parent.parent.parent#different hiearchey than TextInputDynamicActNote
    print('main_box:', main_box)
    if value:
      main_box.act_name_box.add_act_name_label.color=(0,0,0,1)
    else:
      main_box.act_name_box.add_act_name_label.color=(.3,.3,.3,1)
