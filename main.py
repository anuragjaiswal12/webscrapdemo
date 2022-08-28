from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

url="https://en.wikipedia.org/wiki/The_Best_FIFA_Men%27s_Player"
player_data={
  1:{
    'name':[],
    'team':[],
    'year':[]
  },
  2:{
    'name':[],
    'team':[],
    'year':[]
  },
  3:{
    'name':[],
    'team':[],
    'year':[]
  }
}
page=requests.get(url)
if page.status_code == requests.codes.ok:
  page_data=BeautifulSoup(page.text,'lxml')
  table_data=page_data.find('table',class_='wikitable')
  fetched_year=0
  year=0
  for i in [1,5,9,13,17,21]:
    for j in [1,2,3]:
      if j==1:
        row=table_data.find_all('tr')[i] 
        row_data=row.find_all('td')
        fetched_year=row_data[0].text
        year=fetched_year.replace('\n','')
        if year:
          player_data[j]['year'].append(year)
        else:
          player_data[j]['year'].append('none')
        name=row_data[2].find_all('a')[1].text
        if name:
          player_data[j]['name'].append(name)
        else:
          player_data[j]['name'].append('none')
        country=row_data[3].find_all('a')[1].text
        if country:
          player_data[j]['team'].append(country)
        else:
          player_data[j]['team'].append('none')
      elif j==2:
        row=table_data.find_all('tr')[i+1]
        row_data=row.find_all('td')
        if year:
          player_data[j]['year'].append(year)
        else:
          player_data[j]['year'].append('none')
        name=row_data[1].find_all('a')[1].text
        if name:
          player_data[j]['name'].append(name)
        else:
          player_data[j]['name'].append('none')
        country=row_data[2].find_all('a')[1].text
        if country:
          player_data[j]['team'].append(country)
        else:
          player_data[j]['team'].append('none')
      else:
        row=table_data.find_all('tr')[i+2]
        row_data=row.find_all('td')
        if year:
          player_data[j]['year'].append(year)
        else:
          player_data[j]['year'].append('none')
        name=row_data[1].find_all('a')[1].text
        if name:
          player_data[j]['name'].append(name)
        else:
          player_data[j]['name'].append('none')
        country=row_data[2].find_all('a')[1].text
        if country:
          player_data[j]['team'].append(country)
        else:
          player_data[j]['team'].append('none')
  for i in [1,2,3]:
    player_table=pd.DataFrame(player_data[i])
    player_table.to_csv(f'player_data_{i}.csv',sep=',',index=False,encoding='utf-8')
else:
  print("Page not loaded")