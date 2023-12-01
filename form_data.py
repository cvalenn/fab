
files_open = {'file': ('report.txt', 'some, data, to, send\nanother, row, to, send\n')}


data_login=  {
    "login[username]": 'natashenka351@gmail.com',
    "login[password]": "T6m22k1y" 
  }


data_file=  {
    "id": 602,
    "formAlias": "/trades/atom/Tender/Sign_Worker_ProposalParticipantRequirement_Document",
    "file": files_open,
    "signatureData": "test",
    "signedData": "test",
    "doSign":  "(",
    "title":"23",
    "iban":"88" 
  }


data_tax_system = {
    'simplified_tax_system': '2',
    'sbmt': 'Сохранить',
    'ajax': 'true',
}


data_contract_experience=  {
    "contract_details_number": 1,
    "contract_details_date": "11.07.2023",
    "customer_info_name": "customer info name",
    "customer_info_address": "customer info address",
    "contract_description_description": "contract description description",
    "cost_lot_currency_coincide":  0,
    "cost_lot_currency_coincide": 1,
    "cost_lot_currency_price_not_vat": 1000.56,
    "cost_lot_currency_price_with_vat": 1200.56,
    "cost_contract_currency_currency": 0, 
    "cost_contract_currency_rate": 0,
    "cost_contract_currency_price_not_vat": 0,
    "cost_contract_currency_price_with_vat": 0,
    "additional_price_lot_currency_coincide": 0,
    "additional_price_lot_currency_coincide": 1,
    "additional_price_lot_currency_not_vat": 2300,
    "additional_price_lot_currency_with_vat": 2500,
    "additional_price_contract_currency_currency": 0,
    "additional_price_contract_currency_rate": 0,
    "additional_price_contract_currency_price_not_vat": 0,
    "additional_price_contract_currency_price_with_vat": 0,
    "executing_dates_start": "11.07.2022",
    "executing_dates_end": "14.12.2022",
    "sbmt": "Сохранить"
    }


data_mtr_certificate=  {
    "sequence_number": 1,
    "place": "place",
    "mark": "mark",
    "property": "собственное".encode('cp1251'),
    "owner": "собственник".encode('cp1251'),
    "sbmt": "Сохранить"
    }


data_staff_certificate=  {
    "KINDOFWORK": "KINDOFWORK",
    "STAFF": "STAFF",
    "QUANTITY": "QUANTITY",
    "CONTRACTOR": "CONTRACTOR",
    "NOTES": "NOTES",
    "sbmt": "Сохранить"
    }


data_questionary_organization_info=  {
    "full_name": "ГНУ НИИВ Восточной Сибири Россельхозакадемии".encode('cp1251'),
    "name": "ГНУ НИИВ".encode('cp1251'),
    "type_org": "manufacturer",
    "country": 136,
    "region": "Алтайский край".encode('cp1251'),
    "region_code": 2200000000000,
    "city": "test gorod",
    "post_index": 233454,
    "address": "test adress",
    "directory_type": "oktmo",
    "oktmo": 24310,
    "web": "test.fabrikant.ru",
    "inn": 7534001099,
    "kpp": 753401001
    }


data_questionary_type_works=  {
    "TypeWorkForMTR": 1,
    "ajax": "true"
    }


data_questionary_basis=  {
    "basis_text": "Основание отсутствия адреса",
    "ajax": "true"
    }


data_lean_prod=  {
    "data": "Бережливое производство тест".encode('cp1251'),
    "sbmt": "Сохранить"
    }


headers_sts_1 = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryipegsyyd1hb2VJ61'
}

headers_sts_2 = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryt9Y5alXysMcqsmHq'
}
            

data_sts_1 = '------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="proposed_quantity"\r\n\r\n1.000\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="isFrame"\r\n\r\n0\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="is223FZ"\r\n\r\n1\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="needValidPriceField"\r\n\r\n1\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="form_type"\r\n\r\n1\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="org_price_in_participant_currency"\r\n\r\n1010980.88\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="trade_type"\r\n\r\natom_price_request\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="isTaxFree"\r\n\r\n0\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="unitPriceErrorText"\r\n\r\n \r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="unitPriceNotVatErrorText"\r\n\r\n \r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="unit_price_exw_not_vat"\r\n\r\n1 000\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="unit_price_not_vat"\r\n\r\n1 000\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="unit_price"\r\n\r\n1 000\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="price_not_vat"\r\n\r\n1 000\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="price"\r\n\r\n1 000\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="nds"\r\n\r\n-1\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="plant_d0c831135ff38f1d51531f7cc6a9fd09"\r\n\r\n0\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="d0c831135ff38f1d51531f7cc6a9fd09"\r\n\r\n%7B%22isPlant%22%3A1%7D\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="d0c831135ff38f1d51531f7cc6a9fd09"\r\n\r\n%7B%22isPlant%22%3A1%7D\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="inn_d0c831135ff38f1d51531f7cc6a9fd09"\r\n\r\n[]\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="kpp_d0c831135ff38f1d51531f7cc6a9fd09"\r\n\r\n[]\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="country_0a2f75067410fd6ae8dd7c91576fe41c"\r\n\r\n83\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="0a2f75067410fd6ae8dd7c91576fe41c"\r\n\r\n%7B%22country%22%3A%2283%22%2C%22fullAddress%22%3A%22test%22%2C%22asString%22%3A%22%D0%9A%D0%BE%D0%BD%D0%B3%D0%BE%2C%20test%22%7D\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="address_not_russia_0a2f75067410fd6ae8dd7c91576fe41c"\r\n\r\ntest\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="coincides_with_fef5ded31f846a43cc5845aad0ad7290"\r\n\r\non\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="country_fef5ded31f846a43cc5845aad0ad7290"\r\n\r\n83\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="fef5ded31f846a43cc5845aad0ad7290"\r\n\r\n%7B%22country%22%3A%2283%22%2C%22fullAddress%22%3A%22test%22%2C%22asString%22%3A%22%D0%9A%D0%BE%D0%BD%D0%B3%D0%BE%2C%20test%22%2C%22coincidesWith%22%3A1%7D\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="address_not_russia_fef5ded31f846a43cc5845aad0ad7290"\r\n\r\ntest\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="inn_fa03aabf3666370428452a962e215681[0]"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="fa03aabf3666370428452a962e215681"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="kpp_94c78c91eeb8a4f1b3c29ea6b61a872d[0]"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="94c78c91eeb8a4f1b3c29ea6b61a872d"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="71b21ad66c8d0687e7d76a4d542bb06f"\r\n\r\n15\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="0e2c550b4d11f90b4ff62b3e67ccae71"\r\n\r\n3\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="b350f9b83bd6e772794ec32a869b119f"\r\n\r\n33\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="7f41193a18ce16e7f583c1ee5098a28a"\r\n\r\n33\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="014b7d3e426d395b969b73b5096295bf"\r\n\r\n25.04.2023\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="ac3c455844ab1c1a486e49ea21d8a3f9"\r\n\r\nno\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="2b6c7dad9edd797e30266a59fbc6e838"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="bdcf762dd786a5b7a39d5368c8ede5ef"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="e17d85993a9ee782c6de681147ded473"\r\n\r\n3\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61\r\nContent-Disposition: form-data; name="sbmt"\r\n\r\n\r\n------WebKitFormBoundaryipegsyyd1hb2VJ61--\r\n'

data_sts_2 = '------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="proposed_quantity"\r\n\r\n84.000\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="isFrame"\r\n\r\n0\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="is223FZ"\r\n\r\n1\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="needValidPriceField"\r\n\r\n1\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="form_type"\r\n\r\n2\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="org_price_in_participant_currency"\r\n\r\n366.59\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="trade_type"\r\n\r\natom_price_request\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="isTaxFree"\r\n\r\n0\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unitPriceErrorText"\r\n\r\nÖåíà çà åäèíèöó ïîçèöèè ïðåâûøàåò ðåêîìåíäîâàííîå îðãàíèçàòîðîì çíà÷åíèå (îòïðàâêà çàÿâêè âîçìîæíà)\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unitPriceNotVatErrorText"\r\n\r\nÖåíà çà åäèíèöó ïîçèöèè ïðåâûøàåò ðåêîìåíäîâàííîå îðãàíèçàòîðîì çíà÷åíèå (îòïðàâêà çàÿâêè âîçìîæíà)\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="detailing_stages"\r\n\r\ntest detailing_stages\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unit_price_not_vat"\r\n\r\n1 000\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unit_price"\r\n\r\n1 000\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="price_not_vat"\r\n\r\n84 000\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="price"\r\n\r\n84 000\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="nds"\r\n\r\n0\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="08c1aa4f0ee46b8c6ba46d6032c3ad6e"\r\n\r\nòåñò íàèìåíîâàíèå ýòàïà\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="56f3793745976b1e8269b656223975c2"\r\n\r\n11.05.2024\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="37818d53cf71d4131720a839b61f444c"\r\n\r\n19.05.2024\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="sbmt"\r\n\r\nÑîõðàíèòü\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq--\r\n'
        

data_technical_proposal={
    "file": files_open,  
    "title":"technical.txt",
    "description":"22",
    "sbmt": "Загрузить"
}


cookies_admin = {
    'sid': '5ba1386a6f2e4246b6c5dacc2b7f9612',
    'fabrikant': '4187876b80bddc1fca7901d8d2be9061',
    'test': '8f2a60441423f138afc302da830695e7',
    'salt': '8f2a60441423f138afc302da830695e7',
    '_ym_d': '1682788158',
    '_ym_uid': '1682788158437866085',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'isdvlpr': '88fe27a3c5d3ddec8b9f91c1406b9add3fd3082bccb6a0c5fa98b97017167cc2',
}


headers_admin = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'Basic ZS5yb21hbm92YTplLnJvbWFub3Zh',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://test.fabrikant.ru/admin/instructions/?',
}


data_payment_schedule={
    'payment_type': 'advance',
    'payment_term': '11.05.2024',
    'payment_size': '1 000,00',
    'ajax': 'true',
    }

data_delivery_schedule = '------WebKitFormBoundarywog0Dq20HiSvtM2V\r\nContent-Disposition: form-data; name="payment_date"\r\n\r\n25.05.2024\r\n------WebKitFormBoundarywog0Dq20HiSvtM2V\r\nContent-Disposition: form-data; name="payment_size"\r\n\r\n1 000,00\r\n------WebKitFormBoundarywog0Dq20HiSvtM2V\r\nContent-Disposition: form-data; name="ajax"\r\n\r\ntrue\r\n------WebKitFormBoundarywog0Dq20HiSvtM2V--\r\n'



