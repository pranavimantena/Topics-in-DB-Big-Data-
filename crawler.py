import pandas as pd
import numpy as numpy
import requests
import lxml
import time
import mechanize
from bs4 import BeautifulSoup
import urllib.request as urllib2
import http.cookiejar ## http.cookiejar in python3
cookielib = http.cookiejar
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_cookiejar(cj)
br.open("https://pems.dot.ca.gov/")

br.select_form(nr=0)
br.form['username'] = ''
br.form['password'] = ''
br.submit()
a = br.response().read()
combined_df = pd.DataFrame()
months_url = [str(i) for i in range(1,12)]
dates_url = [str(i) for i in range(1,30)]
li =[]
# For every month in the interval 1-12
for month in months_url:
    # For every date in the interval 1-30
    for date in dates_url:
        if month == '2':
            if date == '29':
                continue
            if date == '30':
                continue
        content = br.open('https://pems.dot.ca.gov/?report_form=1&dnode=Freeway&content=spatial&tab=contours&export=&fwy=101&dir=N&district_id=4&s_time_id=1651363200&s_time_id_f=' + date + '%2F'+ month + '%2F2021&from_hh=0&to_hh=23&start_pm=389.73&end_pm=390.19&lanes=&station_type=ml&q=occ&colormap=30%2C31%2C32&sc=auto&ymin=&ymax=&view_d=2&html.x=52&html.y=13').read()
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', { 'class' : 'inlayTable' })
        df = pd.read_html(str(table))[0]
        for index, row in df.iterrows():
            li.append(date + '/' + month + '/2021')
        combined_df = combined_df.append(df, ignore_index=True)
    print("done")
combined_df['dates'] = li
combined_df = combined_df.dropna()
combined_df.to_csv('data_occ.csv')
