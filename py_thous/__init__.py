from  fastapi import FastAPI
from py_thous.web_routes import Routers
wellknown_app: FastAPI = None
__instance__=None
class __Base__:
    def __init__(self):
        self.bind_ip =None
        self.bind_port = None
        self.host_url = None
        self.host_schema = None
        self.__routers__ = None
        self.app: FastAPI = None
    def start_with_uvicorn(self):
        import uvicorn
        uvicorn.run(f"{self.__module__}:wellknown_app", host=self.bind_ip, port=self.bind_port, log_level="info")
    @property
    def routers(self)->Routers:
        if self.__routers__ is None:
            self.__routers__ = Routers(self)
        return self.__routers__
class WebApplication(__Base__):
    def __new__(cls, *args, **kwargs):
        global __instance__
        if __instance__:
            return __instance__
        else:
            ret= __Base__()
            return cls.__init__(ret,*args, **kwargs)

    def __init__(self,
                 bind:str="0.0.0.0:8011",
                 host_url:str="http://localhost:8011"):
        global wellknown_app
        if  bind.split(":").__len__()<2:
            raise Exception(f"bind in {self.__module__}.{WebApplication.__name__}.__init__ must look like 0.0.0.0:1234")
        self.bind_ip = bind.split(':')[0]
        self.bind_port = int(bind.split(':')[1])
        self.host_url = host_url
        self.host_schema = self.host_url.split(f"://")[0]
        remain = self.host_url[self.host_schema.__len__()+3:]
        self.host_name = remain.split('/')[0].split(':')[0]
        self.host_port=None
        if remain.split('/')[0].split(':').__len__()==2:
            self.host_port = int(remain.split('/')[0].split(':')[1])
            remain = remain[self.host_name.__len__()+str(self.host_port).__len__()+1:]
        self.host_dir = None
        if remain !="":
            self.host_dir = remain
        wellknown_app=FastAPI()
        self.app =wellknown_app
        __instance__=self
        return __instance__
    @property
    def app(self)->FastAPI:
        return wellknown_app





