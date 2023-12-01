import requests
import form_data


session = requests.Session()


agg = session.post('https://test.fabrikant.ru/personal/login', data=form_data.data_login)
cookies_auth = session.cookies