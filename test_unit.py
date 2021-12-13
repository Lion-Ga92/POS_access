from guizero import *
from classes import db_Setup_class

app = App(title="Hello World", width=750, height=500)

waf_grid = Waffle(master=app, height=3, width=3, dim=100, pad=5, color="white", dotty=False)

def command_one():
    hello = slide.value
    print(hello)
buttn = PushButton(app, command=command_one, width=200)
app.display()