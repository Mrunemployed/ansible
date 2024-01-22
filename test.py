import pandas as pd
import json
import re
import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

df = pd.read_csv(r"C:\Users\rudkhan\OneDrive - Capgemini\CodeRepo\Flask\tickets\open_tickets.csv")
df["description"].fillna("0",inplace=True)
df = df[["number","short_description","description"]]
# print(df["description"].head(30))

#Filtering the tickets

with open(r"C:\Users\rudkhan\OneDrive - Capgemini\CodeRepo\Flask\tickets\tasks\tasks-config.json","r") as config:
    config = json.load(config)

df_new = pd.DataFrame()
for i in config:
    val = [x for x in i["freeText"]]
    if (len(val)>1):
            
        for j in val:
            p = re.compile(j, flags=re.IGNORECASE)
            new_df_1 = df[[bool(p.search(x)) for x in df["description"]]]
            new_df_1.insert(0,"usecase",i["usecase"])
            df_new = pd.concat([df_new,new_df_1],ignore_index=True)
            # print(new_df_1.head())
    elif (len(val)==1):
        p = re.compile(val[0], flags=re.IGNORECASE)
        new_df_1 = df[[bool(p.search(x)) for x in df["description"]]]
        new_df_1.insert(0,"usecase",i["usecase"])
        df_new = pd.concat([df_new,new_df_1],ignore_index=True)
    else:
        pass
df_new["Status"] = "Waiting"

def task1(task_det):
    print(task_det[["description","usecase","number"]],"\n")
    duration = random.randrange(3,10)
    time.sleep(duration)
    print("Completed {} in {} secs".format(task_det["usecase"],duration))
    print("\n================================ \n")
    return "Completed"

def task2(task_det):
    print(task_det[["description","usecase","number"]],"\n")
    duration = random.randrange(5,8)
    time.sleep(duration)
    print("Completed {} in {} secs".format(task_det["usecase"],duration))
    print("\n ================================ \n")
    return "Completed"

heads = len(df_new["usecase"].unique())

# def dispatcher(heads,df):
    


task_name = ""

while "Waiting" in df_new["Status"].unique():

    for i,j in df_new.iterrows():
        # print(j)
        if df_new["Status"][i] == "Waiting":
            # tasks_executing = df_new[[df_new["Status"].str.contains("In-Progress")]]
            # tasks_open = tasks_executing["usecase"].unique()
            if df_new["usecase"][i] != task_name:
                
                task_name = j["usecase"]
                df_new.loc[i,"Status"] = "In-Progress"
        print(df_new[["usecase","Status"]])
        # break


df_new.to_excel("sample.xlsx")
# for i,j in df.iterrows():
#     print(df["number"][i])
    # if df["short_description"][i].
    
