import form_data
import base_case
from database import ConnectMysql
from database import BDCase
import requests
from base_case import BaseCase

procedure_id = int(input("введите id процедуры: "))
sequence_num = int(input("введите порядковый номер заявки: "))


proposal = ConnectMysql().select_one(f'SELECT proposal_id FROM fabrikant_atom_price_request.proposals where procedure_id={procedure_id} and sequence_number = {sequence_num}')
lot_id = ConnectMysql().select_one(f'SELECT lot_id FROM fabrikant_atom_price_request.proposals where procedure_id={procedure_id}')
url_requirements = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_participant_requirements_view&proposal_id={proposal}&lang=RU'
url_proposal = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal&proposal_id={proposal}'


#Выбор УСН на общей форме заявки
requests.post(
    'https://test.fabrikant.ru/trades/atom/PriceRequest/',
     params= {
         'action': 'change_attribute_simplified_tax_system',
         'proposal_id': f'{proposal}',
         'lang': 'RU',
     },
     cookies=base_case.cookies_auth,
     data=form_data.data_tax_system
)


#Заполнение формы "Сводная таблица стоимости"
url_costsummary_type_view = BaseCase.get_link(url_proposal,'proposal_cost_summary_view')
name_page = BaseCase.get_name_page(url_costsummary_type_view)
if name_page == '<h1 class="page_header">Сводная таблица стоимости на оказание услуг</h1>':
    pozition_id = ConnectMysql().select_all(f'SELECT position_id FROM fabrikant_atom_price_request.lot_positions where lot_id={lot_id}')
    for id_p in pozition_id:
        quantity = float(ConnectMysql().select_one(f'SELECT quantity FROM fabrikant_atom_price_request.lot_positions where position_id={id_p[0]}'))
        price_not_vat= quantity * 300.00
        requests.post(
            'https://test.fabrikant.ru/trades/atom/PriceRequest/',
            params={'action': 'proposal_cost_summary_edit','proposal_id': proposal,'id': id_p,'from': '0',},
            cookies=base_case.cookies_auth,
            headers=form_data.headers_sts_2,
            data=f'------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="proposed_quantity"\r\n\r\n{quantity}\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="isFrame"\r\n\r\n0\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="is223FZ"\r\n\r\n1\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="needValidPriceField"\r\n\r\n1\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="form_type"\r\n\r\n2\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="org_price_in_participant_currency"\r\n\r\n366.59\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="trade_type"\r\n\r\natom_price_request\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="isTaxFree"\r\n\r\n0\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unitPriceErrorText"\r\n\r\nÖåíà çà åäèíèöó ïîçèöèè ïðåâûøàåò ðåêîìåíäîâàííîå îðãàíèçàòîðîì çíà÷åíèå (îòïðàâêà çàÿâêè âîçìîæíà)\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unitPriceNotVatErrorText"\r\n\r\nÖåíà çà åäèíèöó ïîçèöèè ïðåâûøàåò ðåêîìåíäîâàííîå îðãàíèçàòîðîì çíà÷åíèå (îòïðàâêà çàÿâêè âîçìîæíà)\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="detailing_stages"\r\n\r\ntest detailing_stages\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unit_price_not_vat"\r\n\r\n300\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="unit_price"\r\n\r\n300\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="price_not_vat"\r\n\r\n{price_not_vat}\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="price"\r\n\r\n{price_not_vat}\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="nds"\r\n\r\n0\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="08c1aa4f0ee46b8c6ba46d6032c3ad6e"\r\n\r\nòåñò íàèìåíîâàíèå ýòàïà\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="56f3793745976b1e8269b656223975c2"\r\n\r\n11.05.2024\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="37818d53cf71d4131720a839b61f444c"\r\n\r\n19.05.2024\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq\r\nContent-Disposition: form-data; name="sbmt"\r\n\r\nÑîõðàíèòü\r\n------WebKitFormBoundaryt9Y5alXysMcqsmHq--\r\n'
            )
elif name_page == '<h1 class="page_header">Сводная таблица стоимости на поставку товаров</h1>' or '<h1 class="page_header">Cost summary table for goods delivery</h1>':
    url_costsummary_type1_pozitions_edit = BaseCase.get_link(url_costsummary_type_view[0],'proposal_cost_summary_edit')
    pozition_id = ConnectMysql().select_all(f'SELECT position_id FROM fabrikant_atom_price_request.lot_positions where lot_id={lot_id}')
    for id_p in pozition_id:
        requests.post(
        'https://test.fabrikant.ru/trades/atom/PriceRequest/',
        params={'action': 'proposal_cost_summary_edit','proposal_id': proposal,'id': id_p,'from': '0',},
        cookies=base_case.cookies_auth,
        headers=form_data.headers_sts_1,
        data=form_data.data_sts_1,
    )

#Загрузка документов к форме "Требования к участнику"
urldocs = BaseCase.get_link(url_requirements,'proposal_participant_by_requirement_document_create')
if len(urldocs) != 0:
    for urldoc in urldocs:
        requests.post(urldoc, data=form_data.data_file, files=form_data.files_open,cookies=base_case.cookies_auth)

#Подписание документов на форме "Требования к участнику"
    BDCase().set_sign_docs_participant_requirements(proposal)


#Заполнение формы "Техническое предложение"
url_product_requirements = BaseCase.get_link(url_proposal,'proposal_product_requirements_view')
if len(url_product_requirements) != 0:
    url_technical_proposal = BaseCase.get_link(url_product_requirements[0],'proposal_technical_proposal_view')
    if len(url_technical_proposal) != 0:
        requests.post(
        'https://test.fabrikant.ru/trades/atom/PriceRequest/',
        params={
        'id': lot_id,
        'proposal_id': proposal,
        #'lang': 'RU',
        'action': 'proposal_technical_proposal_create',
        },
        cookies=base_case.cookies_auth,
        files=form_data.files_open,
        data=form_data.data_technical_proposal,
        )

#Подписание документа на форме "Техническое предложение"
id_technical_proposals_document = ConnectMysql().select_one(f'SELECT document_id FROM fabrikant_atom_price_request.technical_proposals where proposal_id={proposal}')
requests.post('https://test.fabrikant.ru/trades/Lib/SignPlugin/ajax_tSignHash.html',cookies=base_case.cookies_sign,)
requests.post(
    'https://test.fabrikant.ru/trades/atom/PriceRequest/',
    params={
    'action': 'add_sign_proposal_technical_proposal',
    'id': id_technical_proposals_document,
    #'lang': 'EN',
    #'back_form_type': 'product_requirements',
    },
    cookies=base_case.cookies_for_sign,
    headers={
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary6Bvf28rBRmA0ETIg',
    'Origin': 'https://test.fabrikant.ru',
    'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=add_sign_proposal_technical_proposal&id={id_technical_proposals_document}&lang=EN&back_form_type=product_requirements',
    },
    data=f'------WebKitFormBoundary6Bvf28rBRmA0ETIg\r\nContent-Disposition: form-data; name="id"\r\n\r\n{id_technical_proposals_document}\r\n------WebKitFormBoundary6Bvf28rBRmA0ETIg\r\nContent-Disposition: form-data; name="formAlias"\r\n\r\n/trades/atom/PriceRequest/Sign_Worker_Document_TechnicalProposal\r\n------WebKitFormBoundary6Bvf28rBRmA0ETIg\r\nContent-Disposition: form-data; name="signatureData"\r\n\r\ntest\r\n------WebKitFormBoundary6Bvf28rBRmA0ETIg\r\nContent-Disposition: form-data; name="signedData"\r\n\r\ntest\r\n------WebKitFormBoundary6Bvf28rBRmA0ETIg\r\nContent-Disposition: form-data; name="doSign"\r\n\r\nSign with the digital signature (fake)\r\n------WebKitFormBoundary6Bvf28rBRmA0ETIg--\r\n',
)
#Заполнение формы "Справка об опыте выполнения договоров"
url_contract_experience_view = BaseCase.get_link(url_requirements, 'proposal_contract_experience_view')
if len(url_contract_experience_view) != 0:
    
    url_contract_experience_edit = BaseCase.get_link(url_contract_experience_view[0], 'contract_experience_add_contract_info')
    requests.post(url_contract_experience_edit[0], cookies=base_case.cookies_auth, data=form_data.data_contract_experience)

#Заполнение формы "Справка о материально-технических ресурсах"
url_mtr_certificate_view = BaseCase.get_link(url_requirements, 'proposal_mtr_certificate_view')
if len(url_mtr_certificate_view) != 0:
    url_mtr_certificate_edit = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_mtr_certificate_table_create&proposal_id={proposal}&back_form_type=participant_requirements'
    requests.post(url_mtr_certificate_edit, cookies=base_case.cookies_auth, data=form_data.data_mtr_certificate)


#Заполнение формы "Справка о кадровых ресурсах"
url_staff_certificate_view = BaseCase.get_link(url_requirements, 'proposal_staff_certificate')
print (url_staff_certificate_view)
if len(url_staff_certificate_view) != 0:
    url_staff_certificate_edit= BaseCase.get_action(url_staff_certificate_view[0], 'proposal_staff_certificate_v2_involved_staff_create')
    print(url_staff_certificate_edit)
    requests.post(url_staff_certificate_edit[0], cookies=base_case.cookies_auth, data=form_data.data_staff_certificate)

#Выборка инфы по форме "Анкета"
url_questionary_view = BaseCase.get_link(url_requirements, 'proposal_questionary')
if len(url_questionary_view) != 0:
    url_questionary_edit = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_questionary_add_questionary&proposal_id={proposal}&back_form_type=participant_requirements&context=outside&type=5'
    requests.get(url_questionary_edit, cookies=base_case.cookies_auth)
    questionary_info = ConnectMysql().select_last(f'SELECT type, questionary_id FROM fabrikant_atom_price_request.proposal_forms_questionary where proposal_id={proposal}')
    questionary_id = questionary_info[1]
    questionary_type = questionary_info[0]

#Заполнение блока анкеты "Информация об организации"
    url_questionary_organization_info_edit = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_questionary_organization_info_edit&questionary_id={questionary_id}&back_form_type='
    requests.post(url_questionary_organization_info_edit, cookies=base_case.cookies_auth, files=form_data.files_open, data=form_data.data_questionary_organization_info)

#Заполнение блока анкеты "Вид продукции"
    url_questionary_position_edit = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_questionary_position_edit&questionary_id={questionary_id}&from=0'
    if questionary_type == 5:
        questionary_pozition_id = ConnectMysql().select_one(f'SELECT position_id FROM fabrikant_atom_price_request.lot_positions where lot_id={lot_id} and need_pos_audit = "YMtr"')
    pozition_enable_id = f'position_enable_{questionary_pozition_id}_0'
    mark_id = f'mark_{questionary_pozition_id}_0'
    requests.post(url_questionary_position_edit, cookies=base_case.cookies_auth, data={pozition_enable_id: 1, mark_id: 1, "sbmt": "Сохранить"})

#Заполнение блока анкеты "Работы, необходимые для выполнения требований"
    url_type_works_edit = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_questionary_type_works_update&questionary_id={questionary_id}'
    requests.post(url_type_works_edit, cookies=base_case.cookies_auth, data=form_data.data_questionary_type_works)
    ConnectMysql().update(f'UPDATE fabrikant_atom_price_request.proposal_forms_questionary_adresses SET is_applicable = 0 WHERE (proposal_id = {proposal})')

#Заполнение блока анкеты "Адрес основного производства, всех филиалов и площадок"
    url_basis_edit= f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_questionary_basis_edit&questionary_id={questionary_id}&basis_id='
    requests.post(url_basis_edit, cookies=base_case.cookies_auth, data=form_data.data_questionary_basis)

#Заполнение блока анкеты "Применение в организации Бережливого производства"
    url_lean_prod_edit = f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_questionary_lean_prod_update&questionary_id={questionary_id}&back_form_type=participant_requirements'
    requests.post(url_lean_prod_edit,cookies=base_case.cookies_auth,data=form_data.data_lean_prod)


#Прикрепление документа к анкете и его подпись
    id_inn_document = ConnectMysql().select_one(f'SELECT document_id FROM fabrikant_atom_price_request.proposal_forms_questionary_adresses_inn_documents where questionary_id={questionary_id}')
    requests.post('https://test.fabrikant.ru/trades/Lib/SignPlugin/ajax_tSignHash.html',cookies=base_case.cookies_for_sign,)
    requests.post(
        'https://test.fabrikant.ru/trades/atom/PriceRequest/',
        params={'action': 'sign_proposal_questionary_adresses_inn_document_add','id': f'{id_inn_document}',},
        cookies=base_case.cookies_for_sign, 
        headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryuV9xXflq99B3JYsQ','Origin': 'https://test.fabrikant.ru',
        'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=sign_proposal_questionary_adresses_inn_document_add&id={id_inn_document}',},
        data='------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="id"\r\n\r\n90\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="formAlias"\r\n\r\n/trades/atom/PriceRequest/ProposalForms_Questionary_Sign_Worker_AdressInnDocument\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="signatureData"\r\n\r\ntest\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="signedData"\r\n\r\ntest\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ\r\nContent-Disposition: form-data; name="doSign"\r\n\r\nÏîäïèñàòü ÝÖÏ (êàê áû)\r\n------WebKitFormBoundaryuV9xXflq99B3JYsQ--\r\n'.encode(),
        )


#Заполнение формы "План распределения видов и объемов выполнения работ/ оказания услуг"
url_distribution_of_volumes_view = BaseCase.get_link(url_requirements, 'proposal_distribution_of_volumes_view')
print (url_distribution_of_volumes_view)
if len(url_distribution_of_volumes_view) != 0:
    requests.post(
        'https://test.fabrikant.ru/trades/atom/PriceRequest/',
        params={
        'action': 'proposal_distribution_of_volumes_create',
        'proposal_id': proposal,
        'type': 'supplier',
        'lang': 'RU',
        'back_form_type': 'participant_requirements',
        },
        cookies=base_case.cookies_auth,
        headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://test.fabrikant.ru',
        'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_distribution_of_volumes_create&proposal_id={proposal}&type=supplier&lang=RU&back_form_type=participant_requirements',
      },
        data='select_positions_value=&is_resident_organization=&is_sub_44_fz=&product_name=test&subcontractors=0&organization_name=test&inn=123456789123&kpp=123456789&ogrn=&individual=0&msp_status=none&percent=100&date_start=23.05.2024&date_end=13.09.2024&sbmt=%D1%EE%F5%F0%E0%ED%E8%F2%FC',
    )

#Заполнение формы "График оплаты"
url_payment_schedule_view = BaseCase.get_link(url_proposal, 'proposal_payment_schedule_view')
if len(url_payment_schedule_view) != 0:
    for id_p in pozition_id:
        requests.post(
            'https://test.fabrikant.ru/trades/atom/PriceRequest/',
            params={'action': 'proposal_payment_schedule_payment_create','proposal_id': proposal,'position_id': id_p,'type': 'advance',},
            cookies=base_case.cookies_auth,
            headers={'Content-Type': 'application/x-www-form-urlencoded','Host': 'test.fabrikant.ru','Origin': 'https://test.fabrikant.ru',
            'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_payment_schedule_view&proposal_id={proposal}&id={lot_id}',},
            data=form_data.data_payment_schedule,
        )

#Заполнение формы "График поставки"
url_delivery_schedule_view = BaseCase.get_link(url_proposal, 'proposal_delivery_schedule_view')
if len(url_delivery_schedule_view) != 0:
    for id_p in pozition_id:
        requests.post(
            'https://test.fabrikant.ru/trades/atom/PriceRequest/',
            params={'action': 'proposal_delivery_schedule_add_payment','proposal_id': proposal,'id': id_p,'bid_price': '2',},
            cookies=base_case.cookies_auth,
            headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarywog0Dq20HiSvtM2V','Host': 'test.fabrikant.ru','Origin': 'https://test.fabrikant.ru',
            'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal_delivery_schedule_view&proposal_id={proposal}&id={lot_id}',},
            data=form_data.data_delivery_schedule,
        )
  
#Заполнение формы "Заявка участника (нового типа)"
requests.post(
    'https://test.fabrikant.ru/trades/atom/PriceRequest/',
    params={'action': 'participant_request_edit','proposal_id': proposal,},
    cookies=base_case.cookies_auth,
    headers={
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary38TTZ2bDI10w4qHt','Host': 'test.fabrikant.ru','Origin': 'https://test.fabrikant.ru',
    'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=proposal&id={lot_id}&lang=RU',},
    data='------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="field_point_5_1[0]"\r\n\r\n37\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="label_point_5_1"\r\n\r\ntyrty\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_5_1"\r\n\r\n37\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_7"\r\n\r\ntest adress\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_12"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_13"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_18_1"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n41943040\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="file"; filename="7.txt"\r\nContent-Type: text/plain\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_18_2"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_18_3"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_18_4"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_18_4_1"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="field_point_19[0]"\r\n\r\nself\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="field_point_19[1]"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_19"\r\n\r\n{"0":["self","yes"]}\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_26"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_28"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_29"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_1"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_2"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_3"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="field_point_30_4[0]"\r\n\r\nself\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="field_point_30_4[1]"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_4"\r\n\r\n{"0":["self","yes"]}\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_5"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_5_1"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_5_2_1"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_5_2_2"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_6"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_6_1"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_6_2_1"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_30_6_2_2"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_32"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_33"\r\n\r\nno\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="field_point_38_payment_provision_return_details_select"\r\n\r\nyes\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="receiver_point_38[0]"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="bank_point_38[0]"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="point_38"\r\n\r\n\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt\r\nContent-Disposition: form-data; name="save"\r\n\r\nÑîõðàíèòü\r\n------WebKitFormBoundary38TTZ2bDI10w4qHt--\r\n'.encode(),
)
id_participant_request_documents = ConnectMysql().select_one(f'SELECT document_id FROM fabrikant_atom_price_request.proposal_forms_participant_request_documents where lot_id={lot_id}')
   # подписание файла на форме "Заявка участника (нового типа)"
requests.post(
    'https://test.fabrikant.ru/trades/atom/PriceRequest/',
    params={'action': 'sign_participant_request_document_add','id': id_participant_request_documents,},
    cookies=base_case.cookies_for_sign,
    headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8a74GvamXKbpOdfH','Host': 'test.fabrikant.ru','Origin': 'https://test.fabrikant.ru',
    'Referer': f'https://test.fabrikant.ru/trades/atom/PriceRequest/?action=sign_participant_request_document_add&id={id_participant_request_documents}',},
    data='------WebKitFormBoundary8a74GvamXKbpOdfH\r\nContent-Disposition: form-data; name="id"\r\n\r\n80\r\n------WebKitFormBoundary8a74GvamXKbpOdfH\r\nContent-Disposition: form-data; name="formAlias"\r\n\r\n/trades/atom/PriceRequest/Sign\\Worker\\ProposalForms\\ParticipantRequest\\Document\r\n------WebKitFormBoundary8a74GvamXKbpOdfH\r\nContent-Disposition: form-data; name="signatureData"\r\n\r\ntest\r\n------WebKitFormBoundary8a74GvamXKbpOdfH\r\nContent-Disposition: form-data; name="signedData"\r\n\r\ntest\r\n------WebKitFormBoundary8a74GvamXKbpOdfH\r\nContent-Disposition: form-data; name="doSign"\r\n\r\nÏîäïèñàòü ÝÖÏ (êàê áû)\r\n------WebKitFormBoundary8a74GvamXKbpOdfH--\r\n'.encode(),
)