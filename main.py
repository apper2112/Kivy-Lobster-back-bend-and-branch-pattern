import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from grunt import lobster_back_bend, angle_branch

Window.clearcolor = (1, 1, 1, 1)


class FirstWindow(Screen):

    # ADD CALLBACK IMAGES HERE
    def angleBtn(self):
        sm.current = 'angle'

    def lobsterBtn(self):
        sm.current = "create"

    def hintsBtn(self):
         sm.current = "main"


class lobsterWindow(Screen):
    diameter = ObjectProperty(None)
    centre = ObjectProperty(None)
    divisions = ObjectProperty(None)
    sheet = ObjectProperty(None)
    bend_angle = ObjectProperty(None)
    halves = ObjectProperty(None)

    def calculate_button(self):
        try:
            DM = float(self.diameter.text)
            CT = float(self.centre.text)
            DV = int(self.divisions.text)
            ST = float(self.sheet.text)
            BD = float(self.bend_angle.text)
            HV = int(self.halves.text)
            if DV in [12,24,48] and ST <= 6 and HV in [2,4,6,8,10]:
                return popResults(lobster_back_bend(DM,CT,DV,ST,BD,HV))
            invalidForm()
        except ValueError:
            invalidForm()


    def reset(self):
            self.diameter.text = ''
            self.centre.text = ''
            self.divisions.text = ''
            self.sheet.text = ''
            self.bend_angle.text = ''
            self.halves.text = ''

 
class MainWindow(Screen):
    pass


class AngleBranch(Screen):
    mainDiameter_ = ObjectProperty(None)
    branch_diameter = ObjectProperty(None)
    branch_length = ObjectProperty(None)
    branch_angle = ObjectProperty(None)
    divisions = ObjectProperty(None)
    sheet = ObjectProperty(None)
    
    def calculate_button(self):
        try:
            MD = float(self.mainDiameter.text)
            BD = float(self.branch_diameter.text)
            SL = float(self.branch_length.text)
            BA = float(self.branch_angle.text)
            DV = int(self.divisions.text)
            ST = float(self.sheet.text)
            if DV in [12,24,48] and ST <= 6 and BA <= 90 :
                return popResults(angle_branch(MD,BD,SL,BA,DV,ST))
            invalidForm()
        except ValueError:
            invalidForm()

    def reset(self):
            self.mainDiameter.text = ''
            self.branch_diameter.text = ''
            self.branch_length.text = ''
            self.branch_angle.text = ''
            self.divisions.text = ''
            self.sheet.text = ''


class WindowManager(ScreenManager):
    pass


def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Try again Sucker!.'), size_hint=(None, None), size=(350, 350))
    pop.open()


def popResults(dimensions):
    pop = Popup(title='Results', content=Label(text=dimensions), size_hint=(None, None), size=(350, 1050))
    pop.open()


kv = Builder.load_file("pattern.kv")
sm = WindowManager()

# 4 SCREENS
screens = [FirstWindow(name="menu"), lobsterWindow(name="create"), MainWindow(name="main"), AngleBranch(name="angle")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "menu"


class PatternApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    PatternApp().run()
