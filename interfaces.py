import twint
import csv
import nest_asyncio
nest_asyncio.apply()
import pandas as pd
import os
import os.path

filename = "/Users/lorenzo/.atom/interfaces/example.csv"

if os.path.exists(filename):
    os.remove(filename)

c = twint.Config()

c.Username = "pankary"
c.Limit = 1000
c.Store_csv = True
c.Output = filename

twint.run.Search(c)

df = pd.read_csv(filename)

fulltext = " ".join(df["tweet"])
print(fulltext)
