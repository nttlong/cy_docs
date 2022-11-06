import pathlib
import sys

wokring_dir = pathlib.Path(__file__).parent.__str__()
print(wokring_dir)
sys.path.append(wokring_dir)
from py_thous import WebApp
web_app = WebApp(
    host_url="http://localhost:8011"

)
def test(app_name:str):
    return dict(ok="123",app_name=app_name)
web_app.routers.map_get("{app_name}/test",test)
web_app.start_with_uvicorn()
