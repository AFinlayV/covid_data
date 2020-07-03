import pandas as pd
import urllib

def load_data():
    url = f'https://covidtracking.com/api/v1/states/daily.json'
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    file = open('covid_data_daily.json', 'w')
    file.write(data)
    file.close()


    url = f'https://covidtracking.com/api/v1/states/current.json'
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    file = open('covid_data_current.json', 'w')
    file.write(data)
    file.close()


    data_cur = pd.read_json('covid_data_current.json')
    data_day = pd.read_json('covid_data_daily.json')
    state_pop = pd.read_csv('SCPRC-EST2019-18+POP-RES.csv')
    state_abrev = pd.read_json('state_abrev.json')

    return {'current_data':data_cur, 'daily_data':data_day, 'state_data':state_pop, 'state_abrev':state_abrev}
