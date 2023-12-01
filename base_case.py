from bs4 import BeautifulSoup
import form_data
import re
import requests


session = requests.Session()
session.post('https://test.fabrikant.ru/personal/login', data=form_data.data_login)
cookies_auth = session.cookies


#session.post(
   #'https://test.fabrikant.ru/admin/ajax_check.php', 
   # cookies=.cookies_sign,
    #data='------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="id"\r\n\r\n90\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="formAlias"\r\n\r\n/trades/atom/PriceRequest/ProposalForms_Questionary_Sign_Worker_AdressInnDocument\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="signatureData"\r\n\r\ntest\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="signedData"\r\n\r\ntest\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="doSign"\r\n\r\nÏîäïèñàòü ÝÖÏ (êàê áû)\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ--\r\n'.encode(),
#)
auth_for_sign = session.cookies['auth']

set_admin = requests.get('https://test.fabrikant.ru/admin/', params= '', cookies=form_data.cookies_admin, headers=form_data.headers_admin)
admin_cookies_test = set_admin.cookies['test']

cookies_sign = {
    'sid': '5ba1386a6f2e4246b6c5dacc2b7f9612',
    'fabrikant': '4187876b80bddc1fca7901d8d2be9061',
    'salt': '8f2a60441423f138afc302da830695e7',
    '_ym_d': '1682788158',
    '_ym_uid': '1682788158437866085',
    '_ym_isad': '2',
    'isdvlpr': '88fe27a3c5d3ddec8b9f91c1406b9add3fd3082bccb6a0c5fa98b97017167cc2',
    'admin_id': 'EPoF42PDuWtdn3a4GXTflQ',
    'test': admin_cookies_test,
    '_ym_visorc': 'w',
    'auth': auth_for_sign,
    'uid': '842258',
}
cookies_for_sign = {
    'test': admin_cookies_test,
    'uid': '842258',
    '_ym_visorc': 'w',
    'salt': 'fc7dc4ed3f410d33627828b24e4429bc',
    'admin_id': 'EPoF42PDuWtdn3a4GXTflQ',
    'auth': auth_for_sign,
    'isdvlpr': '48104557ac44050b641e0d4b6846673f0a3854ae0087f03fbb5040246013292e',
    '_ym_isad': '2',
    'fabrikant': 'a6350d6607b5dd482078237e75947252',
    'sid': '95a7960e52cc4795bce0ffe66e614be5',
    '_ga': 'GA1.2.1540891609.1682360402',
    '_ga_TKBJ6SDH2W': 'GS1.1.1682786830.4.0.1682786831.59.0.0',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22e7a6eb6c-c164-4da3-9d83-a42793df1b70%22%7D',
    'mindboxDeviceUUID': 'e7a6eb6c-c164-4da3-9d83-a42793df1b70',
    '_ym_d': '1682330035',
    '_ym_uid': '1632911550653485953',
}


class BaseCase:

    def get_link(url_page, url_form):
        links = []
        soup = BeautifulSoup((requests.get(url_page, cookies=cookies_auth)).text, "html.parser")
        for soup_links in soup.find_all(href = re.compile(url_form)):
            link = (f'https://test.fabrikant.ru{soup_links.get("href")}')
            links.append(link)
        
        return links


    def get_action(url_page, url_form):
        actions = []
        soup = BeautifulSoup((requests.get(url_page, cookies=cookies_auth)).text, "html.parser")
        for soup_links in soup.find_all(action = re.compile(url_form)):
            action = (f'https://test.fabrikant.ru{soup_links.get("action")}')
            actions.append(action)
        
        return actions

    def get_name_page(url_page):
        soup = BeautifulSoup((requests.get(url_page, cookies=cookies_auth)).text, "html.parser")
        page_name = soup.find('h1', {'class': 'page_header'})
        return str(page_name)



