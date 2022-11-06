class Routers:
    def __init__(self,owner):
        import py_thous
        self.owner : py_thous.WebApp = owner

    def map_get(self, path,handler):

        if self.owner.host_dir is None:
            return self.owner.app.get(
                path=f"/{path}",
            )(handler)

        return self.owner.app.get(
            path=f"{self.owner.host_dir}/{path}",
        )(handler)
    def controller(self,cls:type):
        print(cls)
