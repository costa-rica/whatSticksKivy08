from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

Builder.load_file('mainbox/mainbox.kv')

class MainBoxLayout(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  toolbar_height=ObjectProperty(0)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MainBoxLayout __init__')

  def on_enter(self):
    print('MainBox on_enter****')

  def extra_btn_(self,*args):
    print('**contents Box BoxLayoutAddActNote*** ')
    print('self.act_note_box.height:', self.act_note_box.height)
    print('self.act_note_box.add_act_note_label.height:', self.act_note_box.add_act_note_label.height)
    print('self.act_note_box.add_act_note.height:',self.act_note_box.add_act_note.height)

    print('**contents of BoxLayoutActNote**')
    print('self.act_note_box.add_act_note.gridlayout_text.height:', self.act_note_box.add_act_note.gridlayout_text.height)
    print('self.act_note_box.add_act_note.txt_input_dy_act_note.height:',self.act_note_box.add_act_note.txt_input_dy_act_note.height)


class BoxLayoutScreenName(BoxLayout):
  email=StringProperty('')
  def __init__(self,**kwargs):
    super().__init__(**kwargs)



class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddName***')
    main_box =instance.parent.parent#different hiearchey than TextInputDynamicActNote
    # print('main_box:', main_box)
    # print('main_box.children:', main_box.children)
    if value:
      main_box.act_name_box.add_act_name_label.color=(0,0,0,1)
    else:
      main_box.act_name_box.add_act_name_label.color=(.3,.3,.3,1)


class TextInputDynamicActNote(TextInput):
  def on_focus(instance, instance_twice, value):
    print('TextInputDynamicActNote on_focus')

    main_box=instance.parent.parent.parent.parent.parent
    # print('main_box:::', main_box)
    # print('main_box.children:::', main_box.children)
    if value:
      main_box.act_note_box.add_act_note_label.color=(0,0,0,1)
    else:
      main_box.act_note_box.add_act_note_label.color=(.3,.3,.3,1)
