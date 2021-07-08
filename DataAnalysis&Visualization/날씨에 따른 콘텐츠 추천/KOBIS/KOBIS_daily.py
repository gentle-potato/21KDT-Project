import csv
import requests
from bs4 import BeautifulSoup

from datetime import datetime, timedelta

def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2019-12-31", "2021-06-25")




# url = "https://www.kobis.or.kr/kobis/business/stat/online/onlineDailyBoxRank.do?CSRFToken=DYwya7O-TBSnY9etNknJFPADlolemloKwYOfVrQpEbM&loadEnd=0&searchType=search&sSearchFrom=2020-01-01&sSearchTo=2020-01-07"

filename = "KOBIS_daily.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv. writer(f)

title = "daily_rank poster title week release_date country genre director act runtime audience".split()
writer.writerow(title)

for date in dates:
    url = f"https://www.kobis.or.kr/kobis/business/stat/online/onlineDailyBoxRank.do?CSRFToken=DYwya7O-TBSnY9etNknJFPADlolemloKwYOfVrQpEbM&loadEnd=0&searchType=search&sSearchFrom={date}&sSearchTo={date}"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"tbl_comm"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)