import pandas as pd

# Testet ob im "name" am Ende ein Zahl steht
def split_name(name):
    a = name.split('_')
    if len(a) == 1:
        return a
    if len(a) > 1:
        parts = name.rsplit('_', 1)  # Trennt den String in zwei Teile
        if parts[1].isdigit():  # Überprüft, ob der letzte Teil eine Zahl ist
            return parts[0].split('_') + [int(parts[1])]
        else:
            return name.split('_')

# Teilt die Einträge in Spalte "name" von data und entsprechende Zuordnung in Spalten von results
def name_function(data,results,columns):
    for i in data.index:
        a = split_name(data.loc[i, "name"])
        # verschieden verzweigungen, abhängig von den Einträgen in der Spalte "name"
        if len(a) == 1:
            results.loc[i, columns[2]] = data.loc[i, "name"]
            continue
        if isinstance(a[-1], int):
            results.loc[i, columns[2]] = data.loc[i, "name"]
            results.loc[i, columns[3]] = a[0]
            a = a[1:]
            results.loc[i, columns[4]] = a[0]
            a = a[1:]
            results.loc[i, columns[7]] = a[-1]
            a = a[:-1]
            results.loc[i, columns[5]] = a
        else:
            results.loc[i, columns[2]] = data.loc[i, "name"]
            results.loc[i, columns[3]] = a[0]
            a = a[1:]
            results.loc[i, columns[4]] = a[0]
            a = a[1:]
            results.loc[i, columns[5]] = a

def var_name_function(data,results):
    energy_units = ["MWh","kWh","PJ"]
    weighted_units = ["Mt","Mt/a","kg"]
    for i in data.index:
        a = data.loc[i, "var_name"].split('_')
        # verschieden verzweigungen, abhängig von den Einträgen in der Spalte "var_name"
        # invest - Verzweigung
        if a[0] == "invest":
            if data.loc[i,"unit"] in energy_units:
                results.loc[i, "parameter"] = "capacity_p_inst"
                continue
            if data.loc[i,"unit"] in weighted_units:
                results.loc[i, "parameter"] = "capacity_w_inst"
                continue
        # flow - Verzweigung
        if a[0] == "flow":
            results.loc[i, "parameter"] = "flow_volume"
            if a[1] == "in":
                a = a[2:]
                results.loc[i, "input_groups"] = '_'.join(a)
                continue
            if a[1] == "out":
                a = a[2:]
                results.loc[i, "output_groups"] = '_'.join(a)
                continue
        # system - Verzweigung
        else:
            results.loc[i, "process"] = '_'.join(a[:2])
            results.loc[i, "parameter"] = a[-1]