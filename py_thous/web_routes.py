class Routers:
    def __init__(self,owner):
        import py_thous
        self.owner : py_thous.WebApplication = owner

    def map_get(self, path,handler):
        return self.owner.app.get(
            path=f"{self.owner.host_dir}/{path}",
        )(handler)

