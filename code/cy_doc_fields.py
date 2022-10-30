import datetime
import json
import uuid
from typing import List, Union
from re import Pattern,IGNORECASE
import bson
def get_mongodb_text(data):
    if isinstance(data,dict):
        ret = {}
        for k,v in data.items():
            ret[k]=get_mongodb_text(v)
        return ret
    elif isinstance(data,List):
        ret= []
        for x in data:
            ret+=[get_mongodb_text(x)]
        return ret
    elif isinstance(data,str):
        return data
    elif isinstance(data,datetime.datetime):
        return data
    elif isinstance(data,uuid.UUID):
        return data.__str__()
    elif isinstance(data,int):
        return data
    elif isinstance(data,float):
        return data
    elif isinstance(data,complex):
        return dict(
            imag=data.imag,
            real =data.real
        )
    elif isinstance(data,bson.ObjectId):
        return f"ObjectId({data.__str__()})"
    elif isinstance(data, Pattern):
        if (data.flags & IGNORECASE).value != 0:
            return {"$regex": f"{data.pattern}/i"}
        else:
           return {"$regex": data.pattern}
    elif hasattr(type(data),"__str__"):
        fn = hasattr(type(data),"__str__")
        if callable(fn):
            return data.__str__()
        else:
            return data
    else:
        try:
            ret=data.__str__()
            return ret
        finally:
            return data
class __BaseField__:
    def __init__(self,init_value:Union[str,dict],oprator:str = None):
        self.__field_name__ =None
        self.__data__ = None
        self.__oprator__ = oprator
        if isinstance(init_value,str):
            self.__field_name__= init_value
        elif isinstance(init_value,dict):
            self.__data__ =init_value
        else:
            raise Exception("init_value must be str or ditc")

    def __getattr__(self, item):
        return self.__dict__.get(item)
    def to_mongo_db(self)->Union[str,dict]:
        if self.__data__ is not None:
            return self.__data__
        else:
            return self.__field_name__
    def to_mongo_db_expr(self)->Union[str,dict]:
        if self.__data__ is not None:
            return self.__data__
        else:
            return "$"+self.__field_name__

class Field(__BaseField__):
    def __init__(self,init_value:Union[str,dict],oprator:str = None):
        """
        Init a base field
        :param name:
        """
        __BaseField__.__init__(self,init_value,oprator)
    def __getattr__(self, item):
        if isinstance(item,str):
            if item[0:2]=="__" and item[-2:]=="__":
                return __BaseField__.__getattr__(self,item)
            else:
                return Field(f"{self.__field_name__}.{item}")
        else:
            return __BaseField__.__getattr__(self, item)
    def __repr__(self):
        if self.__data__ is not None:
            ret= get_mongodb_text(self.__data__)
            return json.dumps(ret)
        else:
            return self.__field_name__

    #all compare operator
    def __eq__(self, other):
        op = "$eq"
        if isinstance(other,Field):
            return Field(
                {
                    op:[
                        self.to_mongo_db_expr(),
                        other.to_mongo_db_expr()
                    ]
                },op
            )
        elif self.__data__ is None:
            return Field({
                self.__field_name__:other
            },op)
        else:
            if isinstance(other, Field):
                return Field(
                    {
                        op: [
                            self.to_mongo_db_expr(),
                            other.to_mongo_db_expr()
                        ]
                    }, op
                )
            else:
                return Field(
                    {
                        op: [
                            self.to_mongo_db_expr(),
                            other
                        ]
                    }, op
                )
    def __ne__(self, other):
        op = "$ne"
        if isinstance(other, Field):
            return Field(
                {
                    op: [
                        self.to_mongo_db_expr(),
                        other.to_mongo_db_expr()
                    ]
                }, op
            )
        elif self.__data__ is None:
            return Field({
                self.__field_name__: {
                    "$ne":other
                }
            }, op)
        else:
            if isinstance(other, Field):
                return Field(
                    {
                        op: [
                            self.to_mongo_db_expr(),
                            other.to_mongo_db_expr()
                        ]
                    }, op
                )
            else:
                return Field(
                    {
                        op: [
                            self.to_mongo_db_expr(),
                            other
                        ]
                    }, op
                )
    #all logical
    def __and__(self, other):
        if not isinstance(other,Field):
            raise Exception(f"and operation require 2 Field. While {type(other)}")
        return Field(
            {
                "$and": [
                    self.to_mongo_db_expr(),
                    other.to_mongo_db_expr()
                ]
            },"$and"
        )
    def __or__(self, other):
        if not isinstance(other,Field):
            raise Exception(f"and operation require 2 Field")
        return Field(
            {
                "$or": [
                    self.to_mongo_db_expr(),
                    other.to_mongo_db_expr()
                ]
            },"$or"
        )
    # all math operator:
    def __add__(self, other):
        if isinstance(other,Field):
            return Field({
                "$add":[
                    self.to_mongo_db_expr(),
                    other.to_mongo_db_expr()
                ]
            },"$add")
        else:
            return Field({
                "$add": [
                    self.to_mongo_db_expr(),
                    other
                ]
            },"$add")










