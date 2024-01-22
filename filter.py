import pandas as pd
import json
import re
import requests
from requests.models import Response
from datetime import datetime
import logging

date = datetime.today()
date = datetime.strftime(date,"%d-%b-%Y")
logging.basicConfig(filename=f"logs//{date}.log",format='%(asctime)s %(message)s',filemode='a',encoding="utf-8")


class getTickets:


    def __init__(self) -> None:
        self.resp = Response()
        self.resp.status_code = 400
        self.ec = 0

    def get_incidents(self):
        logging.info("Fetching tickets....")
        try:
            if (self.ec<5):
                self.ec += 1
                result = requests.get(url="http://127.0.0.1:5000/incidents/all",verify=False)
                print(result.status_code)
                self.resp = result.json()
            else:
                self.resp.status_code = 409
            
        except json.JSONDecodeError as json_err:
            logging.error(f"\n{json_err}")
        except requests.exceptions.ConnectTimeout as con_err:
            logging.info(f"\n Connection timed out retrying {self.ec} times... {con_err}")
            self.get_incidents(self.ec)
        except requests.exceptions.TooManyRedirects as red_err:
            logging.error(f"\n Bad or invalid URL {red_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"\n Request Exception {req_err}")
            self.resp.status_code = 409
            


class filter(getTickets):

    data = pd.DataFrame()

    def __init__(self) -> None:
        # self.df = pd.read_csv(r"C:\Users\rudkhan\OneDrive - Capgemini\CodeRepo\Flask\tickets\open_tickets.csv")
        # self.df["description"].fillna("0",inplace=True)
        # self.df = self.df[["number","short_description","description"]]
        self.data = pd.DataFrame()
        super().__init__()


    def load_data_to_df(self,resp:dict):
        try:
                
            df = pd.json_normalize(resp)
            df["description"].fillna("Empty",inplace=True)
            df = df[["number","opened_by","resolved_by","opened_at","closed_at","cmdb_ci","assignment_group","short_description","description","closed_by","assigned_to","close_notes"]]
            # df.to_csv(self.open_tasks,mode="a",index=False,header=False)
            print("Data appended")
            self.data = df
        except Exception as err:
            logging.error(f"\n Error while trying to load data into df {err}")
            self.data = pd.DataFrame()
        # return df

    def filter_tickets(self):
        try:
                
            print(self.data)
            #Filtering the tickets
            with open(r"C:\Users\rudkhan\OneDrive - Capgemini\CodeRepo\Flask\tickets\tasks\tasks-config.json","r") as config:
                config = json.load(config)
            # print(self.resp)

            df_new = pd.DataFrame()
            for i in config:
                val = [x for x in i["freeText"]]
                if (len(val)>1):
                        
                    for j in val:
                        p = re.compile(j, flags=re.IGNORECASE)
                        new_df_1 = self.data[[bool(p.search(x)) for x in self.data["description"]]]
                        new_df_1.insert(0,"usecase",i["usecase"])
                        df_new = pd.concat([df_new,new_df_1],ignore_index=True)
                        # print(new_df_1.head())

                elif (len(val)==1):
                    p = re.compile(val[0], flags=re.IGNORECASE)
                    new_df_1 = self.data[[bool(p.search(x)) for x in self.data["description"]]]
                    new_df_1.insert(0,"usecase",i["usecase"])
                    df_new = pd.concat([df_new,new_df_1],ignore_index=True)

                else:
                    pass
            df_new["Status"] = "Waiting"
            # print(df_new.head(10))
            return df_new
        except Exception as err:
            logging.error(f"\n Error at filter_tickets while parsing the config files or filtering tickets. Error: {err}")
            self.data = pd.DataFrame()

    def main(self):
        self.get_incidents()
        
        print(type(self.resp))
        self.load_data_to_df(self.resp)
        data_filtered = self.filter_tickets()
        return data_filtered


# fl1 = filter()
# fl1.filter_tickets()