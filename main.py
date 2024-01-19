import requests
import pandas as pd
import schedule
import time


def job():
    url = "https://statusinvest.com.br/category/advancedsearchresultpaginated"

    querystring = {
        "search": "{\"Sector\":\"\",\"SubSector\":\"\",\"Segment\":\"\",\"my_range\":\"-20;100\",\"forecast\":{\"upsidedownside\":{\"Item1\":null,\"Item2\":null},\"estimatesnumber\":{\"Item1\":null,\"Item2\":null},\"revisedup\":true,\"reviseddown\":true,\"consensus\":[]},\"dy\":{\"Item1\":null,\"Item2\":null},\"p_l\":{\"Item1\":null,\"Item2\":null},\"peg_ratio\":{\"Item1\":null,\"Item2\":null},\"p_vp\":{\"Item1\":null,\"Item2\":null},\"p_ativo\":{\"Item1\":null,\"Item2\":null},\"margembruta\":{\"Item1\":null,\"Item2\":null},\"margemebit\":{\"Item1\":null,\"Item2\":null},\"margemliquida\":{\"Item1\":null,\"Item2\":null},\"p_ebit\":{\"Item1\":null,\"Item2\":null},\"ev_ebit\":{\"Item1\":null,\"Item2\":null},\"dividaliquidaebit\":{\"Item1\":null,\"Item2\":null},\"dividaliquidapatrimonioliquido\":{\"Item1\":null,\"Item2\":null},\"p_sr\":{\"Item1\":null,\"Item2\":null},\"p_capitalgiro\":{\"Item1\":null,\"Item2\":null},\"p_ativocirculante\":{\"Item1\":null,\"Item2\":null},\"roe\":{\"Item1\":null,\"Item2\":null},\"roic\":{\"Item1\":null,\"Item2\":null},\"roa\":{\"Item1\":null,\"Item2\":null},\"liquidezcorrente\":{\"Item1\":null,\"Item2\":null},\"pl_ativo\":{\"Item1\":null,\"Item2\":null},\"passivo_ativo\":{\"Item1\":null,\"Item2\":null},\"giroativos\":{\"Item1\":null,\"Item2\":null},\"receitas_cagr5\":{\"Item1\":null,\"Item2\":null},\"lucros_cagr5\":{\"Item1\":null,\"Item2\":null},\"liquidezmediadiaria\":{\"Item1\":null,\"Item2\":null},\"vpa\":{\"Item1\":null,\"Item2\":null},\"lpa\":{\"Item1\":null,\"Item2\":null},\"valormercado\":{\"Item1\":null,\"Item2\":null}}",
        "orderColumn": "", "isAsc": "", "page": "0", "take": "200", "CategoryType": "1"}

    payload = ""

    headers = {
        "authority": "statusinvest.com.br",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "referer": "https://statusinvest.com.br/acoes/busca-avancada",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    json_res = response.json()

    res = []

    for i in json_res['list']:
        res.append(i)

    dataframe = pd.json_normalize(res)
    dataframe = pd.DataFrame(dataframe)
    dataframe.to_csv('acoesweb.csv', encoding='utf-8', index=False, sep=';', decimal=',')


# Executar o código no fechamento da B3
import schedule
import time

def job():
    print("Job running...")

# Schedule job to run every day at 17:55
schedule.every().day.at("17:55").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


while True:
    schedule.run_pending()
    time.sleep(1)

