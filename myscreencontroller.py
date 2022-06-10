from base import BaseScreenManager

class MyScreenController():
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MyScreenController __init__')
    self.view = BaseScreenManager(controller=self)
    # self.ps1_base_width=1
    # self.ps1_base_height=1
    # self.ps1_size_count=0

  def get_screen(self):
    return self.view
