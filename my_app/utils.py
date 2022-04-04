from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def read_table():
    table = pd.read_excel('my_app/static/ipca_com_tratativa 2.xlsx', 'Sheet1')

    return table


def find_values_of_the_last_months(table, months_number):
    final_sum = 0

    today = datetime.today()
    months = relativedelta(months=months_number)

    for value in table.values:
        time_object = datetime.strptime(value[0], '%d/%m/%Y')
        if time_object > (today - months):
            final_sum += value[1]

    return str(round(final_sum, 2)).replace('.', ',') + '%'
    