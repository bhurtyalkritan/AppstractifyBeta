import pandas
import numpy


def main_filter(data, user: str, row):
    print(type(main_filter))
    df = data
    user_input = user
    r = row
    if user_input.find(">=") != -1:
        print(user_input)
        user_input = user_input.split()
        print(user_input)
        if user_input[0][0] == ">" and user_input[0][1] == "=":
            # ['>=50']
            x = ""
            for i in user_input[0]:
                if i.isnumeric():
                    x = x + str(i)
                else:
                    pass
            x = int(x)
            print(x)
            df = delete_greater(df, x, row)
            return delete_equal(df, x, row)
        else:
            pass
    # >70
    elif (user_input.find("=<") != -1) or (user_input.find("<=") != -1):
        if user_input.find("=<") != -1:
            user_input = user_input.split()
        if user_input[0][0] == "=" and user_input[0][1] == "<":
            # 400=>100
            x = ""
            for i in user_input[0]:
                if i.isnumeric():
                    x = x + str(i)
                else:
                    pass
            x = int(x)
            print(x)
            df = delete_less(df, x, row)
            return delete_equal(df, x, row)
        else:
            pass
    elif user_input.find(">") != -1:
        if user_input.find(">") != -1:
            user_input = user_input.split()
        if user_input[0][0] == ">":
            # 400=>100
            x = ""
            for i in user_input[0]:
                if i.isnumeric():
                    x = x + str(i)
                else:
                    pass
            x = int(x)
            print(x)
            df = delete_greater(df, x, row)
            return df
        else:
            pass
    elif user_input.find("<") != -1:
        if user_input.find("<") != -1:
            user_input = user_input.split()
        if user_input[0][0] == "<":
            # 400=>100
            x = ""
            for i in user_input[0]:
                if i.isnumeric():
                    x = x + str(i)
                else:
                    pass
            x = int(x)
            print(x)
            df = delete_less(df, x, row)
            return df
        else:
            pass


    elif user_input.find("-c") != -1:
        delete_column(df,row)

# if user_input.find("-r") != -1:
#    user_input.replace("-r","")
#    user_input = int(user_input)
#   print(u)
#  return delete_row(df,user_input)

def testing(df):
    return df


def to_float(df, col):
    df[col] = df[col].astype(float)
    return df


def to_int(df, col):
    df[col] = df[col].astype(int)
    return df


def to_string(df, col):
    df[col] = df[col].astype(str)
    return df


def delete_column(df, index):
    l = list(df.columns)
    df = df.drop([l[index]])
    return df


## 8 < 40
def add_column(df, list_value):
    return


def delete_row(df, index):
    df = df.drop(index)
    return df


'''
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
'''


def add_row():
    return


def delete_greater(data, val, col):
    df = data
    u = val
    c = col
    try:
        df = df[df[col] <= val]
        return df
    except Exception as e:
        return e


def delete_less(df, val, row):
    try:
        df = df[df[row] >= val]
        return df
    except Exception as e:
        return e


def delete_equal(data, val, col):
    df = data
    u = val
    c = col
    try:
        df = df[df[col] != val]
        return df
    except Exception as e:
        return e
    '''
def delete_wrong_format(df,index):
    df.dropna()
'''
    '''
def delete_duplicate(df):
    return df.drop_duplicates()
## operators: d<,d>,=,$,-r,+r,-c,+c,+-s,-e,-d,-f
'''


print("\n")
