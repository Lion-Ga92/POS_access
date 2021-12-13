
from guizero import App, Text, PushButton, Box, Picture
from classes import app3, new_Windows

app = App(title="Tamales Garcia D.A.P", layout="grid", width=750, height=600)
box1 = Box(app, layout="grid", grid=[1, 0], align="top")
msg_wlcome = Text(box1, text=">>Bienvenido Al punto de Acesso de Tamales Garcia<<", grid=[0, 0])
box2 = Box(app, layout="grid", grid=[1,1])


def launch_app():
    window_new = new_Windows()
    window_new.gui_layout2()


def launch_app_order():
    window_order = app3()
    window_order.app_3_gui()


buttn_data = PushButton(box2, command=launch_app_order, text="Revisar\nOrdenes", width=15, height=3, grid=[1, 1])
buttn_orders = PushButton(box2, command=launch_app, text="Tomar\nOrdenes", width=15, height=3, grid=[2, 1])
buttn_web = PushButton(box2, command=print("hello"), text="Sitio\nWeb", width=15, height=3,grid=[1, 2])
buttn_server = PushButton(box2, command=print("hello"), text="Sistema\nPagos", width=15, height=3,grid=[2, 2])


img_Logo = Picture(box2, image="~/POS_access/tamalesGa5.png", grid=[2, 3])
info_txt = Text(box2, text="Los botones enlazan\n a diferentes sub-aplicaciones\n del\nPunto de Aceso de \nTamales Garcia.", grid=[1, 3])
app.display()