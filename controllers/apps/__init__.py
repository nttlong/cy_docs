import fastapi
import pydantic

import py_thous
def test():
    return "XXX"
class Mydata:
    code:str


@py_thous.web_handler(path="{app_name}/test",method=py_thous.WebMethods.POST)
def register(data:Mydata,v:str,fn = fastapi.Depends(test)):
    """

    :param data: OK dsadas
    :param v:  dsadas
    :return:
    """
    return dict(ok=123)