import pandas as pd
with open("names.txt", "r") as f:
    ans = f.read()
x = 1

y = 2
# ans_ls = ans.replace("\n",",").replace("\t",",")
val = ans.split("\n")
new = []
for a in val:
    if "\t" in a or "Buy" == a:
        continue
    else:
        new.append(a)
print(new)
dict_coins = {}
for i in range(len(new)):
    # print(i)
    # print(x)
    # print(y)
    if i == x:
        # print(new[x])
        # print(new[y])
        dict_coins[new[x]] = new[y]
        x += 3
        y += 3
print(dict_coins)

name = dict_coins.keys()
df = pd.DataFrame({'col':name, 'symbol': dict_coins.values()})
df.to_csv("coin.csv")