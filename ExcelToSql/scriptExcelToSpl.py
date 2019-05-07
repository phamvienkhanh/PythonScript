import pandas as pd
import sqlite3 as sql



#=========================================================================
xl = pd.ExcelFile("object_prop_matrix.xlsx")

categories = xl.parse(xl.sheet_names[1])
for row in categories.index:
    for col in categories.keys():
        print(categories[col][row])

#=========================================================================



#========================================================================
sqlConnect = sql.connect("data.db")

sqlCur = sqlConnect.cursor()

sqlCur.execute('drop table if exists Categories')

sqlCur.execute('''create table Categories (
                            ID int primary key not null, 
                            Name char(50) not null,
                            Description text,
                            AnnotationType char(50)
                        )''')

sqlConnect.commit()

sqlCur.execute('select * from Categories')
sqlConnect.commit()
#print(sqlCur.fetchall())
sqlConnect.close()
#================================================================