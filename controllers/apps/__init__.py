import fastapi
import pydantic
import typing
import py_thous
def test():
    return "XXX"
class Department(pydantic.BaseModel):
    code:str
    name:str
class Mydata:
    code:str
    department:Department
    departments: typing.List[Department]




@py_thous.web_handler(path="{app_name}/test",method=py_thous.WebMethods.POST)
def register(data:Mydata,v:str,fn = fastapi.Depends(test)):
    """

    :param data: OK dsadas
    :param v:  dsadas
    :return:
    """
    data.Department.code="xxxxxx"
    return data