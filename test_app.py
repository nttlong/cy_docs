import pathlib
import os
from py_thous import WebApp
web_app = WebApp(
    working_dir= pathlib.Path(__file__).parent.__str__(),
    host_url="http://localhost:8011",
    controller_dirs=[
        "./controllers"
    ]
)
web_app.start_with_uvicorn()