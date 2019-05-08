import pandas as pd
import json
from fuzzywuzzy import fuzz


#=== read and parse file to dataFrame ===================
xl = pd.ExcelFile("object_prop_matrix.xlsx")
df_categories = xl.parse(xl.sheet_names[1])
df_ObjectProperties = xl.parse(xl.sheet_names[0])
#========================================================

#=== dump file ==========================================
data_categories = {}
OP_Col1 = df_ObjectProperties.keys()[0]
OP_Col2 = df_ObjectProperties.keys()[1]
OP_Col3 = df_ObjectProperties.keys()[2]
OP_Col4 = df_ObjectProperties.keys()[3]

# read Categories sheet 
for row in df_categories.index:
    itemData = {}
    cate_col1 = df_categories.keys()[0]

    for col in df_categories.keys()[1:]:
        itemData[col] = df_categories[col][row]

    categoryKey = df_categories[cate_col1][row]
    data_categories[categoryKey] = itemData



# read ObjectProperties
for cateKey in data_categories.keys():
    _catekey = str(cateKey)
    found = False
    for row in df_ObjectProperties.index:
        _proKey = str(df_ObjectProperties[OP_Col1][row])
        
        if  fuzz.ratio(_catekey,_proKey) > 70:
            found = True
            data_categories[cateKey]["Items"] = []
            #print(str(cateKey) + " found " + str(df_ObjectProperties[firstCol][row]))
            for item in range(row+1,df_ObjectProperties.index.size):
                if not pd.isna(df_ObjectProperties[OP_Col2][item]):
                    itemDetail = {}
                    print(df_ObjectProperties[OP_Col2][item]),
                    print(df_ObjectProperties[OP_Col3][item]),
                    print(df_ObjectProperties[OP_Col4][item])
                    itemDetail["Item Name"]  = df_ObjectProperties[OP_Col2][item]
                    itemDetail["Item Code"]  = df_ObjectProperties[OP_Col3][item]
                    itemDetail["Des"]        = df_ObjectProperties[OP_Col4][item]
                    itemDetail["Value Type"] = "value"
                    data_categories[cateKey]["Items"].append(itemDetail)
                else:
                    print('==================================')
                    break
            
        if found :
            break

    # if not found:
    #     print("not found " + _catekey)

#print(df_ObjectProperties[df_ObjectProperties.keys()[1]][1])

with open('categories.json','w') as outFile:
    json.dump(data_categories,outFile)
#========================================================
