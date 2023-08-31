#from langchain import OpenAI
#from langchain import prompts
import pandas as pd
import faker


# declaring template values
Earthquake_df = pd.read_csv("templates/Earthquake_Data.csv")
Employee_df = pd.read_csv("templates/EmployeeData.csv")
Disease_df = pd.read_csv("templates/Disease.csv")
Econ_df = ""
Healthcare_df = ""
Education_df = ""
Population_df = ""
Machine_df = ""
Research_df = ""
Flight_df = ""


def export_dataframe(data):
    df = data
    df_csv = df.to_csv('blank.csv',index=True)
    print(df_csv)


def prompt_gpt(user_input):
    #llm = OpenAI.llm

def prompt_bard():
    pass

def prompt_llama():
    pass

def faker_lib():
    pass
