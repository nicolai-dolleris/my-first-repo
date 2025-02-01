import pandas as pd
import json

file = r"C:\Users\DennePC\OneDrive\Skrivebord\Dokumenter\Personlig\Python projects\Test.xlsx"
data = pd.read_excel(file)

data.head()

analysisID = data["id"].tolist()
filt = data["filt"].tolist()
variable = data["variable"].tolist()

# Convert DataFrame to dictionary dynamically
dictionary = {
    str(row["id"]): {
        "filter": row["filt"],
        "variables": row["filt"]  # Using 'filt' since both keys have the same value
    }
    for _, row in data.iterrows()
}

with open("sample.json", "w") as outfile: 
    json.dump(dictionary, outfile)