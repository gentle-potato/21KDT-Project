# days = []
# for i in range(1, 367):
#     days.append(i)

# print(days)

from datetime import datetime, timedelta

def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2020-01-01", "2021-06-25")
print(dates)