import yfinance
import requests
import pandas as pd
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res=requests.get("https://api.nasdaq.com/api/quote/list-type/nasdaq100",headers=headers)
main_data=res.json()['data']['data']['rows']

all_company = []
for i in range(len(main_data)):
    print(main_data[i]['companyName'])
    all_company.append(main_data[i]['companyName'])

df = pd.DataFrame({'col':all_company})
df.to_csv("all_data.csv", sep=',')