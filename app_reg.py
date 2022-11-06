from py_thous import WebApp
WebApp.controller()
@WebApp.controller()
class AppRegister:
    class Input:
        AppName:str
        AppCode:str
    class Ouput:
        Ok:bool
    def __init__(self):
        print("XXX")
