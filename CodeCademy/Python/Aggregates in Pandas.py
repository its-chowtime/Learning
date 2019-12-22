import pandas as pd

#1
user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())

#2
click_source = user_visits.groupby('utm_source').count().reset_index()

#3
print(click_source)

#4
click_source_by_month = user_visits.groupby(['utm_source','month']).count().reset_index()
print(click_source_by_month)

#5
click_source_by_month_pivot = click_source_by_month.pivot(
    columns = 'month',
    index = 'utm_source',
    values = 'id').reset_index()
print(click_source_by_month_pivot)