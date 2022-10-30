import re

import bson
import cy_doc_fields
field = cy_doc_fields.Field('xx')
print((field.name +1)==3)
print(field.to_mongo_db_expr())

field=(field.code==re.compile('xxx')) & ((field.name +1)!=3)
print(field)