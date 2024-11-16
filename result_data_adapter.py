
from openpyxl import load_workbook
import pandas as pd
from functions import name_function

# create dataframe for results
columns = ["scenario", "parameter", "process", "sector", "category",
               "specification", "groups", "new", "input_groups",
               "output_groups", "unit", "value"]

results = pd.DataFrame(columns= columns)

data = pd.read_csv("results.csv",
                        sep=",")

# Wendet eine String-Ersetzung auf jeden Wert in der Spalte name an.
data['name'] = data['name'].str.replace(r'--\d+$', '', regex=True)

# Entfernen aller Zeilen, bei denen die Werte in der Spalte "name" mit "helper" beginnen
data = data[~data['name'].str.startswith('helper')]
data.reset_index(drop=True)

# --------------------------------------------------------------------------------------------------------------------->

name_function(data,results,columns)

# --------------------------------------------------------------------------------------------------------------------->
'''
for i in data.index:
    a = data.loc[i, "var_name"].split('_')
    if a[0] == "flow":
        results.loc[i, "para"]
        if a[1] == "in":

'''