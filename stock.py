import yfinance
import requests
import pandas as pd
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res=requests.get("https://api.nasdaq.com/api/quote/list-type/nasdaq100",headers=headers)
main_data=res.json()['data']['data']['rows']

all_company = []
print(main_data[:5])
for i in range(len(main_data)):
    print(main_data[i]['companyName'])
    all_company.append([main_data[i]['companyName'],main_data[i]['symbol']])

df = pd.DataFrame(all_company, columns=['companyName', "symbol"])
df.to_csv("all_data.csv", sep=',')