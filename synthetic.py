from langchain.llms import OpenAI
from langchain import prompts
import pandas as pd
from faker import Faker

global Earthquake_df
global Employee_df
global Disease_df
global Econ_df
global Healthcare_df
global Education_df
global Flight_df

Earthquake_df = pd.read_csv("templates/Earthquake_Data.csv")
Employee_df = pd.read_csv("templates/EmployeeData.csv")
Disease_df = pd.read_csv("templates/Disease.csv")

def export_dataframe(data,format):
    df = data
    df_csv = df.to_csv('blank.csv', index=True)
    print(df_csv)

def excel_converter(df):
    df = pd.read_csv(df)
    df = df.to_excel("download.xlsx",sheet_name="Download",index=False)
    print(df)
def csv_converter():
    return
def prompt_gpt(user_input,key):
    try:
        llm = OpenAI(openai_api_key=key,temperature=0.9)
        df = llm.predict(user_input)
        return df
    except:
        print("Rate exceeded or bug found")

def prompt_bard(query):
    API_KEY = ""
    df = google_bard.generate_text(query, api_key=API_KEY)
    return df
def prompt_llama():
    return

def faker_lib():
    return
