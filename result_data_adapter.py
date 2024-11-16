
from openpyxl import load_workbook
import pandas as pd
from functions import name_function, var_name_function

# Vorbereitung Output

# create dataframe for results
columns = ["scenario", "parameter", "process", "sector", "category",
               "specification", "groups", "new", "input_groups",
               "output_groups", "unit", "value"]

results = pd.DataFrame(columns= columns)

# Vorbereitung Input

data = pd.read_csv("results.csv",
                        sep=",")

# Wendet eine String-Ersetzung auf jeden Wert in der Spalte name an.
data['name'] = data['name'].str.replace(r'--\d+$', '', regex=True)

# Entfernen aller Zeilen, bei denen die Werte in der Spalte "name" mit "helper" beginnen
data = data[~data['name'].str.startswith('helper')]
data.reset_index(drop=True)
# --------------------------------------------------------------------------------------------------------------------->

# Erzeugen von einer test Zeile in data für var_name == invest
test_data = {"name": ["ind_steel_casting_1","ind_steel_casting_2"],
        "var_name": ["invest_out_exo_steel","invest_out_exo_steel"],
        "var_value": [999,888],
        "region": ["DE","DE"],
        "type":[{},{}],
        "carrier": [{},{}],
        "tech":["tech","tech"],
        "unit":["MWh","kg"]
}
df_test = pd.DataFrame(test_data)

data['unit'] = "MWh"

data2 = pd.concat([data, df_test], ignore_index=True)


# --------------------------------------------------------------------------------------------------------------------->

# fill the results dataframe with data

name_function(data,results,columns) # evtl. columns als argument entfernen

var_name_function(data,results)

results.value = data.var_value

results.scenario = "o_steel_tokio"
# --------------------------------------------------------------------------------------------------------------------->

# fill the results dataframe with data incl. testdata

name_function(data2,results,columns) # evtl. columns als argument entfernen

var_name_function(data2,results)

results.value = data2.var_value

results.scenario = "o_steel_tokio"