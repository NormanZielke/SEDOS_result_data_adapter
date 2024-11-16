import pandas as pd

# Teilt die Einträge in Spalte "name" von data und entsprechende Zuordnung in Spalten von results
def name_function(data,results,columns):
    for i in data.index:
        a = data.loc[i, "name"].split('_')
        #a = split_string(data.loc[i, "name"])
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