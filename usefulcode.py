# Libraries
import pandas as pd
import datetime as dt


turnstiles_df["DATE_TIME"] = pd.to_datetime(turnstiles_df.DATE + " " + turnstiles_df.TIME, format="%m/%d/%Y %H:%M:%S")

turnstiles_df["DAYOFWEEK"] =turnstiles_df["DATE_TIME"].dt.dayofweek
