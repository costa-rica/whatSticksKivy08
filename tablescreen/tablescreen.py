from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('tablescreen/tablescreen.kv')

class TableScreen(Screen):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('TableScreen __init__')

  def on_kv_post(self,*args):
    #get count of row_data_list
    print('Need table grid:::', self.children[0].children[0].children[0].children[1].children[0])
    self.table_grid = self.children[0].children[0].children[0].children[1].children[0]
    count=len(self.table_grid.row_data_list)
    #populate record_count_label with count
    self.record_count_label.text="User Entries Count: " +str(count)



class TableGrid(GridLayout):
  row_count=StringProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('TableGrid __init__')
    self.cols=1
    # self.spacing=5
    self.size_hint=(1,None)
    # self.row_data_list=MainApp.get_running_app().row_data_list
    #Get the row_data_list
    ###Get's called in NavMenu when View Logged Activites clicked: ps2.get_table_data()
    self.row_data_list=[]
    self.table_size='20'
    self.row_count_showing="0"
    ###Get's called in NavMenu when View Logged Activites clicked: ps2.get_table_data()
    self.button_dict={'ID':0,'Date/Time':0,'Activity Name':0,'All/Last 20':0,'Showing':0}
    self.on_size_count=0
    self.sort_util_flag=False#reduce the numbrer of times rowbox_font_size_util get's called



  def on_kv_post(self,*args):
    print('TableGrid on_kv_post')
    self.table_screen= self.parent.parent.parent.parent.parent
    self.table_screen.fancy_header.delete_column.text =f"Showing {self.table_size} entries"



  def delete_act(self,widget):
    #CAll to api for delete
    self.row_data_list=[x for x in self.row_data_list if widget.name not in x]
    self.row_count_showing=str(len(self.row_data_list))
    self.table_screen.record_count_label.text="Row Count: " +self.row_count_showing
    self.clear_widgets()
    self.build_table()

  def build_table(self):
    print('TableGrid build_table')

    ###Get ps1_base_width and ps1_base_height from parent
    print('self.table_screen.width:',self.table_screen.width)

    row_data_list = self.row_data_list[0:20] if self.table_size=='20' else self.row_data_list
    self.row_count_showing=str(len(row_data_list))
    self.rowbox_dict={}
    # print('TableGrid build_table -- row_data_list:', len(row_data_list), type(row_data_list))
    # print('%%%%%%%%%%%%%%')
    for h,i in enumerate(row_data_list):

      rowbox = RowBox(size_hint=(1,None))
      rowbox.act_id.text=i[0]
      rowbox.act_id.color=(.5,.1,.1,1)
      rowbox.act_date.text=i[1]
      rowbox.act_name.text=i[2]
      rowbox.act_delete.text="delete"
      rowbox.act_delete.name = i[0]
      self.add_widget(rowbox)
      self.rowbox_dict[h]=rowbox

    self.sort_util_flag=True
    self.rowbox_font_size_util()
    self.sort_util_flag=False


  def sort_util(self,widget):
    if widget.text[:2]=="ID":

      self.button_dict['ID']+=1
      if self.button_dict['ID']%3==0:#no sort
        self.table_screen.fancy_header.id_btn.text="ID"
        self.table_screen.fancy_header.id_btn.background_color=(1,1,1,1)
        self.row_data_list.sort(key=lambda k: (k[4]))

      elif self.button_dict['ID']%3==1:#ascending
        self.table_screen.fancy_header.id_btn.text="ID \n ascending"
        self.table_screen.fancy_header.id_btn.background_color=(.3,.3,.3,1)
        self.row_data_list.sort(key=lambda k: k[0])


      elif self.button_dict['ID']%3==2:#descending
        self.table_screen.fancy_header.id_btn.text="ID \n descending"
        self.table_screen.fancy_header.id_btn.background_color=(.3,.3,.3,1)
        self.row_data_list.sort(key=lambda k: k[0],reverse=True)


      self.table_screen.fancy_header.date_btn.text="Date/Time"
      self.table_screen.fancy_header.date_btn.background_color=(1,1,1,1)
      self.table_screen.fancy_header.act_btn.text="Activity Name"
      self.table_screen.fancy_header.act_btn.background_color=(1,1,1,1)

    if widget.text[:2]=='Da':
      self.button_dict['Date/Time']+=1
      if self.button_dict['Date/Time']%3==0:#no sort
        self.table_screen.fancy_header.date_btn.text="Date/Time"
        self.table_screen.fancy_header.date_btn.background_color=(1,1,1,1)
        self.row_data_list.sort(key=lambda k:k[4])
      elif self.button_dict['Date/Time']%3==1:#ascending
        self.table_screen.fancy_header.date_btn.text="Data/Time \n ascending"
        self.table_screen.fancy_header.date_btn.background_color=(.3,.3,.3,1)
        self.row_data_list.sort(key=lambda k:k[3])
      elif self.button_dict['Date/Time']%3==2:#descending
        self.table_screen.fancy_header.date_btn.text="Data/Time \n descending"
        self.table_screen.fancy_header.date_btn.background_color=(.3,.3,.3,1)
        self.row_data_list.sort(key=lambda k:k[3],reverse=True)

      self.table_screen.fancy_header.id_btn.text="ID"
      self.table_screen.fancy_header.id_btn.background_color=(1,1,1,1)
      self.table_screen.fancy_header.act_btn.text="Activity Name"
      self.table_screen.fancy_header.act_btn.background_color=(1,1,1,1)

    if widget.text[:2]=='Ac':
      # print('Activity Name button pressed')
      self.button_dict['Activity Name']+=1
      if self.button_dict['Activity Name']%3==0:#no sort
        self.table_screen.fancy_header.act_btn.text="Activity Name"
        self.table_screen.fancy_header.act_btn.background_color=(1,1,1,1)
        self.row_data_list.sort(key=lambda k:k[4])
      elif self.button_dict['Activity Name']%3==1:#ascending
        self.table_screen.fancy_header.act_btn.text="Activity Name \n ascending"
        self.table_screen.fancy_header.act_btn.background_color=(.3,.3,.3,1)
        self.row_data_list.sort(key=lambda k:k[2])
      elif self.button_dict['Activity Name']%3==2:#descending
        self.table_screen.fancy_header.act_btn.text="Activity Name \n descending"
        self.table_screen.fancy_header.act_btn.background_color=(.3,.3,.3,1)
        self.row_data_list.sort(key=lambda k:k[2],reverse=True)

      self.table_screen.fancy_header.id_btn.text="ID"
      self.table_screen.fancy_header.id_btn.background_color=(1,1,1,1)
      self.table_screen.fancy_header.date_btn.text="Date/Time"
      self.table_screen.fancy_header.date_btn.background_color=(1,1,1,1)

    if widget.text[:2]=='Sh':
      self.button_dict['Showing']+=1
      if self.button_dict['Showing']%2==0:
        self.table_size='20'
        self.build_table()
        self.table_screen.fancy_header.delete_column.text =f"Showing {self.row_count_showing} entries"
        # self.table_screen.record_count_label.text="Row Count: " +str(len(self.row_data_list))
      elif self.button_dict['Showing']%2==1:
        self.table_size='All'
        self.build_table()
        self.table_screen.fancy_header.delete_column.text =f"Showing {self.row_count_showing} \n (All) entries"
        # self.table_screen.record_count_label.text="Row Count: " +str(len(self.row_data_list)) +'\n (All)'

    self.clear_widgets()
    self.build_table()
    # self.sort_util_flag=True
    # self.rowbox_font_size_util()
    # self.sort_util_flag=False


  def rowbox_font_size_util(self,*args):
    print('TableGrid in rowbox_font_size_util: ', self.on_size_count)
    if self.on_size_count==2 or self.sort_util_flag:
      print('*****Font size adjusted*******')
      print('self.ps1_base_width:', self.ps1_base_width)
      table_font_size=self.ps1_base_width*.015

      print('self.table_screen.width::::', self.table_screen.width)
      print('table_font_size:::', table_font_size)
      # print('rowbox_dict[0]:')
      # print(self.rowbox_dict[0])
      # print(len(self.rowbox_dict))
      for i,j in self.rowbox_dict.items():
        j.act_id.font_size=table_font_size
        j.act_date.font_size=table_font_size
        j.act_name.font_size=table_font_size
        j.act_delete.font_size=table_font_size
    self.on_size_count+=1

    #Table side bar font size:::
    self.table_screen.nav_top.font_size=self.ps1_base_width*.02
    self.table_screen.nav_middle.font_size=self.ps1_base_width*.02
    self.table_screen.nav_bottom.font_size=self.ps1_base_width*.02
    #Table FancyHeader font sizes:::
    self.table_screen.fancy_header.id_btn.font_size=self.ps1_base_width*.02
    self.table_screen.fancy_header.date_btn.font_size=self.ps1_base_width*.02
    self.table_screen.fancy_header.act_btn.font_size=self.ps1_base_width*.02
    self.table_screen.fancy_header.delete_column.font_size=self.ps1_base_width*.02




class RowBox(BoxLayout):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
