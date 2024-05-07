import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

##____________________________________________________________

url = 'https://www.livechennai.com/gold_silverrate.asp'
a = requests.get(url)
#print(a.status_code)

b = BeautifulSoup(a.text, 'html.parser')
c = b.find_all(class_='table table-bordered table-striped gold-rates')
#print(c)
column_name = []
for d in c:
    e = d.find_all("th")
    for f in e:
        column_name.append(f.text)
#print(column_name)

##_______row data
row_data =[]
for g in c:
    h = g.find_all("tr")
    for i in h[1:]:
        j = i.find_all("td")
        for k in j:
            row_data.append(k.text)
    
        
#print(row_data)
#print(len(row_data))

##_________________________________________ Row data creation

row_data1 = row_data[0:5]
row_data2 = row_data[5:10]
row_data3 = row_data[10:15]
row_data4 = row_data[15:20]
row_data5 = row_data[20:25]
row_data6 = row_data[25:30]
row_data7 = row_data[30:35]
row_data8 = row_data[35:40]
row_data9 = row_data[40:45]
row_data10 = row_data[45:50]


column_names = ["DATE","GOLD_RATE(1gm-24K)","GOLD_RATE(8gm-24K)","GOLD_RATE(1gm-22K)","GOLD_RATE(8gm-22K)"]       
full_data = [row_data1,row_data2,row_data3,row_data4,row_data5,row_data6,row_data7,row_data8,row_data9,row_data10]

last_10days_data = pd.DataFrame(columns= column_names,data= full_data)

##_________________________________________ str to numeric convert
last_10days_data['GOLD_RATE(1gm-22K)'] = pd.to_numeric(last_10days_data['GOLD_RATE(1gm-22K)'].str.replace(',', ''))


#print((last_10days_data["GOLD_RATE(1gm-22K)"].dtype))



#print(last_10days_data)


##__________________________________________to create new column PRICE_CHANGE

new_variable = last_10days_data['GOLD_RATE(1gm-22K)'].copy()

#print(type(new_variable))
new_variable2 = new_variable.tolist()     ## converting panda series data to list data
#print(type(new_variable2))
#print(new_variable2)

new_variable3 = new_variable2[0] - new_variable2[1]
#print(new_variable3)

new_variable5 = []
for i in range(len(new_variable2) - 1):
    change = new_variable2[i] - new_variable2[i + 1]
    new_variable5.append(change)

#print(new_variable5)


last_10days_data = last_10days_data.iloc[:-1]  ## to eliminate last row data
last_10days_data['PRICE_CHANGE(1gm-22K)'] = new_variable5

# Convert int64_column to int
last_10days_data['PRICE_CHANGE(1gm-22K)'] = last_10days_data['PRICE_CHANGE(1gm-22K)'].astype(int)

print(last_10days_data)

##_____________________________to save data in excel

# Save DataFrame to Excel
#last_10days_data.to_csv('last_10days_gold_data.csv', index=False)

##____________

def analyze_gold(last_10days_data):
    last_10days_data_check = last_10days_data.iloc[0]

    if last_10days_data_check["PRICE_CHANGE(1gm-22K)"] < -75:
         print("Yes! it is good to buy GOLD today!!!")
         print(f"GOLD_RATE for 1gm-22K is {last_10days_data_check['GOLD_RATE(1gm-22K)']}, PRICE_CHANGE for 1gm-22K is {last_10days_data_check['PRICE_CHANGE(1gm-22K)']}")
    else:
        print("It is good to wait for 2 more days to buy GOLD!")
        print(f"Because GOLD_RATE for 1gm-22K is {last_10days_data_check['GOLD_RATE(1gm-22K)']}, PRICE_CHANGE for 1gm-22K is {last_10days_data_check['PRICE_CHANGE(1gm-22K)']}")

#analyze_gold(last_10days_data)

