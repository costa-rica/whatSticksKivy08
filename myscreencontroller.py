from base import BaseScreenManager

class MyScreenController():
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MyScreenController __init__')
    self.view = BaseScreenManager(controller=self)

  def get_screen(self):
    return self.view
