import pandas
import numpy




def main_filter(data, user : str,row):
    print(type(main_filter))
    df = data
    u = user
    r = row
    if u.find("lt") != -1:
        u = [sub.split() for sub in u]
        if u[0] == "l" and u[1] == "t":
            x = ""
            for i in range(1, len(u)):
                x = x + u[i]
            x = int(x)
            df = delete_greater(df,row, x)
            return delete_equal(df,row, x)
        else:
            pass
    #>70
    elif(u.find("<=") != -1):
        u = [sub.split for sub in u]
        if(u[0] == "<" and u[1] == "="):
            pass
        else:
            pass
    elif u.find(">") != -1:
        u = [sub.split() for sub in u]
        if u[0] == ">":
            #greater than ___
            x = ""
            for i in range(1,len(u)):
                x = x + u[i]
            x = int(x)
            print(x)
            delete_greater(row, x)
        else:
            pass
    elif u.find("<") != -1:
        u = [sub.split() for sub in u]
        if u[0] == "<":
            # greater than ___
            x = ""
            for i in range(1, len(u)):
                x = x + u[i]
            x = int(x)
            delete_less(row,  x)
        else:
            pass

    if u.find("-c") != -1:
        u.replace("-c","")
        u = int(u)
        return delete_column(df,u)

    if u.find("-r") != -1:
        u.replace("-r","")
        u = int(u)
        print(u)
        return delete_row(df,u)

def testing(df):
    return df
def to_float(df,col):
    df[col] = df[col].astype(float)
    return df
def to_int(df,col):
    df[col] = df[col].astype(int)
    return df
def to_string(df,col):
    df[col] = df[col].astype(str)
    return df
def delete_column(df,index):
    l = list(df.columns)
    df = df.drop([l[index]])
    return df
## 8 < 40
def add_column(df, list_value):
    return
def delete_row(df,index):
    df = df.drop(index)
    return df

def swap_row(df,row1,row2):
    df.iloc[row1], df.iloc[row2] = df.iloc[row2].copy(), df.iloc[row1].copy()
    return df

def swap_column(df, col1,col2):
    if isinstance(col1,str) and isinstance(col2,str):
        columns_titles = [col1,col2]
        df = df.reindex(columns=columns_titles)
        return df
    else:
        return -1
def add_row():
    return
def delete_greater(data,val, col):
    df = data
    u = val
    c = col
    try:
        df = df[df[col] <= val]
        return df
    except Exception as e:
        return e

def delete_less(df,val, row):
    try:
        df = df[df[row] >= val]
        return df
    except Exception as e:
        return e
def delete_equal(df,val,row):
    df = df[df[row] != val]
    return df
def delete_wrong_format(df,index):
    df.dropna()

def delete_duplicate(df):
    return df.drop_duplicates()
## operators: d<,d>,=,$,-r,+r,-c,+c,+-s,-e,-d,-f

