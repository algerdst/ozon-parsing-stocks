# ozonparsing@ozon-parsing.iam.gserviceaccount.com
import gspread
import time

import requests
from bs4 import BeautifulSoup

payload = {}
headers = {
    'authority': 'ozon.by',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cookie': '__Secure-ab-group=6; __Secure-ext_xcid=fe39c826aa87867602d50c9144bfc928; cookie_settings=eyJhbGciOiJIUzI1NiIsIm96b25pZCI6Im5vdHNlbnNpdGl2ZSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDY4NjI2MDYsImlzcyI6Im96b25pZCIsInN1YiI6InRva2VuX2tpbmRfZ2Rwcl9jb29raWVzIiwibWFya2V0aW5nIjpmYWxzZSwic3RhdGlzdGljIjpmYWxzZSwicHJlZmVyZW5jZXMiOmZhbHNlfQ.lVVA7DLBpF7kgFHO-1CVr4pigATMYurqS29noz7rCMU; __Secure-user-id=0; xcid=0a88445c0f8d1e23a1f440d6cd77cc1a; __Secure-access-token=4.0.zE3jUL-6RSSW8JY_n12c9Q.6.AaB2DqWVX2qrmaFWE1nG8VQ2CROSq1F0ZySmRDi5pecgqBGC7j4KJew_-Hl023QB-w..20240229084818.oJFVYZopTj7h97igXb-tjMfueCH209MjHnbE1t_a6yA; __Secure-refresh-token=4.0.zE3jUL-6RSSW8JY_n12c9Q.6.AaB2DqWVX2qrmaFWE1nG8VQ2CROSq1F0ZySmRDi5pecgqBGC7j4KJew_-Hl023QB-w..20240229084818.5beNJso_F3sIL8aTaUyui4y27eIS9w66INv8Xi5ZQm4; abt_data=d762f8a5202eb553b04e31e709b058bc:4c40c8851bdad1e35d666beff9ab581eaa697b5b5083bf051ccf743fedc9327580de7800443d080f7ed62b4d44b0ed33ced50894cfca2481da2accfba1bac764af9f76f8280cc20654aafc6374787cab36bc6a9539155634829bba298bec9c3fe045cd29245423f3c6810348c3543b8a867382c154b1fc47653bc9b64dd81c937415d4208127d3e8f01b5de18a1f7999c34d30fa17eab3074cfc6d7335af2ef7f50ee7f41d0f0be74827dff902a64f094747330dd05f592d05645379ebaf9344cef99237d9f11c0aa991aa034d01bc84e83aad7e5e3b1cf34fd6e0edf7d61560a5810654299d31d1b56cbbb5b8a0869e610eb29a25a7f435a1b4f38301ce2f941f3a5f7e721e52ce9d1ac230e9197e3bffb9996ccc4f7a5434448469e8c5e8d31298c2312022af5abe318fdbce93ef30ae4952ac55efc91acbb4e082b9ec9df179adb40ed21da1c6aa1992af74307159a90789c23038b935d01d74dde326ec5aca9c451afdbb7baa4c47d40d506e72e0; __Secure-ab-group=61; __Secure-access-token=4.0.ufHgdLm9Tgm0lZjGpnBdPw.61.AZrjVF4tRzgJ7Og8CcmChTSIF5PHUea9VA6lIK44k5ZdVkZ4Gcc8hBZaS8QvlH9JUg..20240229082840.h6Bvn3ak6eqgO4JsOq-pB5KjQgbcWqo1dW3OCSQNWW8; __Secure-ext_xcid=9d8a30cd4056260795284a9195bae1a6; __Secure-refresh-token=4.0.ufHgdLm9Tgm0lZjGpnBdPw.61.AZrjVF4tRzgJ7Og8CcmChTSIF5PHUea9VA6lIK44k5ZdVkZ4Gcc8hBZaS8QvlH9JUg..20240229082840.13rG3PLEm0JQMZ8dZJU1cEZMxOUTjZthBh7otsxrPV8; __Secure-user-id=0; abt_data=adab2e604fc4c0f235ef3231a664d3fc:9f58ba71a528a42ee6955fd864c2b2a0fb9c08ba8cffa759482461cfd81d154ee6b558bfd78cddb5cdc941db1a07c12c8bd7e2dc7201984f8cbdbdd5bf6f7fbf1ffd2f11a630d4bdef3a3d0e738aa5cc4b9ee372bc410080a4c450b281994143846c1649251cf73ea09b1ea23234ef938e7c59359ae4aab66dddfe7fe6b92ac8c28f19a666d6692fd63367abde549581fae590e538f7f221e8485531416369a9bc274551624e809186dbf975c0b79191781a9b6ce539f6aa626415145de392196713d11ee288740bd249f66e8d32e7c451219a9df871369261ca0b6a87b437f826a5d8f12065d8d730e3ef07d11a8a3d4f3850ef080d10e7b326d8a59f813a1a995a7e800a89c88ddcfd9e21a14f4abad503df685ba113d483c418525c9b28c95022b976dffbe6338ab59b00a9f3a824d1745b50f1004c25ab620de296d70aadd087d68f758898fed3c4b92441dba3eaf82ed79ff165fc6460f019ef050b334894f97e8d5f8eab849020e369291aa8b4; xcid=9d8a30cd4056260795284a9195bae1a6',
    'referer': 'https://www.ozon.ru/ozonid/domain_redirect?domain=ozon.by&redirect_uri=%2Fsearch%2F%3Ffrom_global%3Dtrue%26text%3D1411146194',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
}



with open('table_data.txt', 'r', encoding='utf-8') as file:
    data = [i for i in file]
table_name = data[0].replace('\n', '')
list_name = data[1].replace('\n', '')

# Соединение с гугл таблицей
sa = gspread.service_account(filename='secret.json')
sh = sa.open(table_name)
wks = sh.worksheet(list_name)

items_quantity = int(input('Укажите количество артикулов в таблице'))  # Количество товаров в таблице

column = 12
row = 2
for j in range(items_quantity):
    article = wks.cell(row, column).value
    url = f"https://ozon.by/search/?text={article}&from_global=true"
    time.sleep(0.5)
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f'Ошибка соединения {response.status_code}')
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        stocks = soup.find('div', class_='v3i').find('span', class_='e6144-a4').text.replace('Осталось ',
                                                                                             '').replace(' шт',
                                                                                                         '')
    except:
        stocks = '-'
        print('Остаток не найден')
    wks.update_cell(row, column + 1, stocks)
    print(f'Артикул {article} обработан')
    row += 1
column += 2

