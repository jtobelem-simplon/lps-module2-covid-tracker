# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

import requests

from pandas.io.json import json_normalize


url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"name":"france"}

headers = {
    'x-rapidapi-key': "e2b300e502msh7789d032cb75624p1f092ejsnf3ffe0faf06a",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

df = json_normalize(data)
df['date'] = pd.to_datetime(df.lastUpdate).map(pd.Timestamp.date)


daily_fr_df = df


# Write recipe outputs
daily_fr = dataiku.Dataset("daily")
daily_fr.write_with_schema(daily_fr_df)
