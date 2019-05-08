import pandas as pd
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#=== Create sql engine ==================================================
engine = create_engine('sqlite:///data2.db', echo=False)
#========================================================================


#========================================================================
class Categories(Base):
    __tablename__ = 'Categories'

    id              = Column(Integer, primary_key = True)
    name            = Column(String)
    description     = Column(String)
    annotationType  = Column(String)
#=========================================================================


#=========================================================================
xl = pd.ExcelFile("object_prop_matrix.xlsx")

df_categories = xl.parse(xl.sheet_names[1])
df_categories.to_sql('Categories', con=engine, if_exists='replace', index_label='id')

df_ObjectProperties = xl.parse(xl.sheet_names[0])
df_ObjectProperties.to_sql('ObjectProperties', con=engine, if_exists='replace', index_label='id')
# for row in categories.index:
#     line = u''
#     for col in categories.keys():
#         line = line + categories[col][row].encode('utf-8') + u' '
#     print(line)

#print(u'dasd' + u'dasda')
#print(categories[u'Description '][16].encode('utf-8'))
#=========================================================================



#========================================================================

#================================================================