from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import db_fetch as db
from kivy.properties import ListProperty


Builder.load_file("main.kv")

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f"You Selected: {value}"   
		
    def spinner_update(self):
        string=""
        equipments = db.run_process()
        r = ListProperty()
        r = [str(t[1]) for t in equipments]
        print(r)

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
    equipments = db.run_process()
    r = ListProperty()
    r = [str(t[1]) for t in equipments]
    
    
if __name__=="__main__":
    AwesomeApp().run()